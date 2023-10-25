import concurrent
from functools import partial
from itertools import combinations_with_replacement
from typing import Tuple

import numpy as np
from ase import Atoms
from numpy.typing import NDArray

from dynasor.logging_tools import logger
from dynasor.trajectory import Trajectory, WindowIterator
from dynasor.sample import DynamicSample, StaticSample
from dynasor.post_processing import fourier_cos
from dynasor.core.time_averager import TimeAverager
from dynasor.core.reciprocal import calc_rho_q, calc_rho_j_q
from dynasor.qpoints.tools import get_index_offset


def compute_dynamic_structure_factors(
    traj: Trajectory,
    q_points: NDArray[float],
    dt: float,
    window_size: int,
    window_step: int = 1,
    calculate_currents: bool = False,
    calculate_incoherent: bool = False,
) -> DynamicSample:
    """Compute dynamic structure factors.  The results are returned in the
    form of a :class:`DynamicSample <dynasor.sample.DynamicSample>`
    object.

    Parameters
    ----------
    traj
        Input trajectory
    q_points
        Array of q-points in units of 2π/Å with shape ``(N_qpoints, 3)`` in Cartesian coordinates
    dt
        Time difference in femtoseconds between two consecutive snapshots
        in the trajectory. Note that you should *not* change :attr:`dt` if you change
        :attr:`frame_step <dynasor.trajectory.Trajectory.frame_step>` in :attr:`traj`.
    window_size
        Length of the trajectory frame window to use for time correlation calculation.
        It is expressed in terms of the number of time lags to consider
        and thus determines the smallest frequency resolved.
    window_step
        Window step (or stride) given as the number of frames between consecutive trajectory
        windows. This parameter does *not* affect the time between consecutive frames in the
        calculation. If, e.g., :attr:`window_step` > :attr:`window_size`, some frames will not
        be used.
    calculate_currents
        Calculate the current correlations. Requires velocities to be available in :attr:`traj`.
    calculate_incoherent
        Calculate the incoherent part (self-part) of :math:`F_incoh`.
    """
    # sanity check input args
    if q_points.shape[1] != 3:
        raise ValueError('q-points array has the wrong shape.')
    if dt <= 0:
        raise ValueError(f'dt must be positive: dt= {dt}')
    if window_size <= 2:
        raise ValueError(f'window_size must be larger than 2: window_size= {window_size}')
    if window_size % 2 != 0:
        raise ValueError(f'window_size must be even: window_size= {window_size}')
    if window_step <= 0:
        raise ValueError(f'window_step must be positive: window_step= {window_step}')

    # define internal parameters
    n_qpoints = q_points.shape[0]
    delta_t = traj.frame_step * dt
    N_tc = window_size + 1

    # log all setup information
    dw = 2 * np.pi / (window_size * delta_t)
    w_max = dw * window_size
    f_N = 1 / (2 * delta_t)  # Nyquist frequency
    conv = 658.2119  # conversion from 2pi/fs to meV
    logger.info(f'Spacing between samples (frame_step): {traj.frame_step}')
    logger.info(f'Time between consecutive frames in input trajectory (dt): {dt} fs')
    logger.info(f'Time between consecutive frames used (dt * frame_step): {delta_t} fs')
    logger.info(f'Time window size (dt * frame_step * window_size): {delta_t * window_size:.1f} fs')
    logger.info(f'Angular frequency resolution: dw = {dw:.6f} 2pi/fs = {dw * conv:.3f} meV')
    logger.info(f'Maximum angular frequency (dw * window_size):'
                f' {w_max:.6f} 2pi/fs = {w_max * conv:.3f} meV')
    logger.info(f'Nyquist angular frequency (2pi / frame_step / dt / 2):'
                f' {f_N * 2 * np.pi:.3f} 2pi/fs = {f_N * 2 * np.pi * conv:.1f} meV')

    if calculate_currents:
        logger.info('Calculating current (velocity) correlations')
    if calculate_incoherent:
        logger.info('Calculating incoherent part (self-part) of correlations')

    # log some info regarding q-points
    logger.info(f'Number of q-points: {n_qpoints}')

    q_directions = q_points.copy()
    q_distances = np.linalg.norm(q_points, axis=1)
    nonzero = q_distances > 0
    q_directions[nonzero] /= q_distances[nonzero].reshape(-1, 1)

    # setup functions to process frames
    def f2_rho(frame):
        rho_qs_dict = dict()
        for atom_type in frame.positions_by_type.keys():
            x = frame.positions_by_type[atom_type]
            rho_qs_dict[atom_type] = calc_rho_q(x, q_points)
        frame.rho_qs_dict = rho_qs_dict
        return frame

    def f2_rho_and_j(frame):
        rho_qs_dict = dict()
        jz_qs_dict = dict()
        jper_qs_dict = dict()

        for atom_type in frame.positions_by_type.keys():
            x = frame.positions_by_type[atom_type]
            v = frame.velocities_by_type[atom_type]
            rho_qs, j_qs = calc_rho_j_q(x, v, q_points)
            jz_qs = np.sum(j_qs * q_directions, axis=1)
            jper_qs = j_qs - (jz_qs[:, None] * q_directions)

            rho_qs_dict[atom_type] = rho_qs
            jz_qs_dict[atom_type] = jz_qs
            jper_qs_dict[atom_type] = jper_qs

        frame.rho_qs_dict = rho_qs_dict
        frame.jz_qs_dict = jz_qs_dict
        frame.jper_qs_dict = jper_qs_dict
        return frame

    if calculate_currents:
        element_processor = f2_rho_and_j
    else:
        element_processor = f2_rho

    # setup window iterator
    window_iterator = WindowIterator(traj, width=N_tc, window_step=window_step,
                                     element_processor=element_processor)

    # define all pairs
    pairs = list(combinations_with_replacement(traj.atom_types, r=2))
    particle_counts = {key: len(val) for key, val in traj.atomic_indices.items()}
    logger.debug('Considering pairs:')
    for pair in pairs:
        logger.debug(f'  {pair}')

    # setup all time averager instances
    F_q_t_averager = dict()
    for pair in pairs:
        F_q_t_averager[pair] = TimeAverager(N_tc, n_qpoints)
    if calculate_currents:
        Cl_q_t_averager = dict()
        Ct_q_t_averager = dict()
        for pair in pairs:
            Cl_q_t_averager[pair] = TimeAverager(N_tc, n_qpoints)
            Ct_q_t_averager[pair] = TimeAverager(N_tc, n_qpoints)
    if calculate_incoherent:
        F_s_q_t_averager = dict()
        for pair in traj.atom_types:
            F_s_q_t_averager[pair] = TimeAverager(N_tc, n_qpoints)

    # define correlation function
    def calc_corr(window, time_i):
        # Calculate correlations between two frames in the window without normalization 1/N
        f0 = window[0]
        fi = window[time_i]
        for s1, s2 in pairs:
            Fqt = np.real(f0.rho_qs_dict[s1] * fi.rho_qs_dict[s2].conjugate())
            if s1 != s2:
                Fqt += np.real(f0.rho_qs_dict[s2] * fi.rho_qs_dict[s1].conjugate())
            F_q_t_averager[(s1, s2)].add_sample(time_i, Fqt)

        if calculate_currents:
            for s1, s2 in pairs:
                Clqt = np.real(f0.jz_qs_dict[s1] * fi.jz_qs_dict[s2].conjugate())
                Ctqt = 0.5 * np.real(np.sum(f0.jper_qs_dict[s1] *
                                            fi.jper_qs_dict[s2].conjugate(), axis=1))
                if s1 != s2:
                    Clqt += np.real(f0.jz_qs_dict[s2] * fi.jz_qs_dict[s1].conjugate())
                    Ctqt += 0.5 * np.real(np.sum(f0.jper_qs_dict[s2] *
                                                 fi.jper_qs_dict[s1].conjugate(), axis=1))

                Cl_q_t_averager[(s1, s2)].add_sample(time_i, Clqt)
                Ct_q_t_averager[(s1, s2)].add_sample(time_i, Ctqt)

        if calculate_incoherent:
            for atom_type in traj.atom_types:
                xi = fi.positions_by_type[atom_type]
                x0 = f0.positions_by_type[atom_type]
                Fsqt = np.real(calc_rho_q(xi - x0, q_points))
                F_s_q_t_averager[atom_type].add_sample(time_i, Fsqt)

    # run calculation
    with concurrent.futures.ThreadPoolExecutor() as tpe:
        # This is the "main loop" over the trajectory
        for window in window_iterator:
            logger.debug(f'processing window {window[0].frame_index} to {window[-1].frame_index}')

            # The map conviniently applies calc_corr to all time-lags. However,
            # as everything is done in place nothing gets returned so in order
            # to start and wait for the processes to finish we must iterate
            # over the None values returned
            for _ in tpe.map(partial(calc_corr, window), range(len(window))):
                pass

    # collect results into dict with numpy arrays (n_qpoints, N_tc)
    data_dict_corr = dict()
    time = delta_t * np.arange(N_tc, dtype=float)
    data_dict_corr['q_points'] = q_points
    data_dict_corr['time'] = time

    F_q_t_tot = np.zeros((n_qpoints, N_tc))
    S_q_w_tot = np.zeros((n_qpoints, N_tc))
    for pair in pairs:
        key = '_'.join(pair)
        F_q_t = 1 / traj.n_atoms * F_q_t_averager[pair].get_average_all()
        w, S_q_w = zip(*[fourier_cos(F, delta_t) for F in F_q_t])
        w = w[0]
        S_q_w = np.array(S_q_w)
        data_dict_corr['omega'] = w
        data_dict_corr[f'Fqt_coh_{key}'] = F_q_t
        data_dict_corr[f'Sqw_coh_{key}'] = S_q_w

        # sum all partials to the total
        F_q_t_tot += F_q_t
        S_q_w_tot += S_q_w
    data_dict_corr['Fqt_coh'] = F_q_t_tot
    data_dict_corr['Sqw_coh'] = S_q_w_tot

    if calculate_currents:
        Cl_q_t_tot = np.zeros((n_qpoints, N_tc))
        Ct_q_t_tot = np.zeros((n_qpoints, N_tc))
        Cl_q_w_tot = np.zeros((n_qpoints, N_tc))
        Ct_q_w_tot = np.zeros((n_qpoints, N_tc))
        for pair in pairs:
            key = '_'.join(pair)
            Cl_q_t = 1 / traj.n_atoms * Cl_q_t_averager[pair].get_average_all()
            Ct_q_t = 1 / traj.n_atoms * Ct_q_t_averager[pair].get_average_all()
            Cl_q_w = np.array([fourier_cos(C, delta_t)[1] for C in Cl_q_t])
            Ct_q_w = np.array([fourier_cos(C, delta_t)[1] for C in Ct_q_t])
            data_dict_corr[f'Clqt_{key}'] = Cl_q_t
            data_dict_corr[f'Ctqt_{key}'] = Ct_q_t
            data_dict_corr[f'Clqw_{key}'] = Cl_q_w
            data_dict_corr[f'Ctqw_{key}'] = Ct_q_w

            # sum all partials to the total
            Cl_q_t_tot += Cl_q_t
            Ct_q_t_tot += Ct_q_t
            Cl_q_w_tot += Cl_q_w
            Ct_q_w_tot += Ct_q_w
        data_dict_corr['Clqt'] = Cl_q_t_tot
        data_dict_corr['Ctqt'] = Ct_q_t_tot
        data_dict_corr['Clqw'] = Cl_q_w_tot
        data_dict_corr['Ctqw'] = Ct_q_w_tot

    if calculate_incoherent:
        Fs_q_t_tot = np.zeros((n_qpoints, N_tc))
        Ss_q_w_tot = np.zeros((n_qpoints, N_tc))
        for atom_type in traj.atom_types:
            Fs_q_t = 1 / traj.n_atoms * F_s_q_t_averager[atom_type].get_average_all()
            Ss_q_w = np.array([fourier_cos(F, delta_t)[1] for F in Fs_q_t])
            data_dict_corr[f'Fqt_incoh_{atom_type}'] = Fs_q_t
            data_dict_corr[f'Sqw_incoh_{atom_type}'] = Ss_q_w

            # sum all partials to the total
            Fs_q_t_tot += Fs_q_t
            Ss_q_w_tot += Ss_q_w

        data_dict_corr['Fqt_incoh'] = Fs_q_t_tot
        data_dict_corr['Sqw_incoh'] = Ss_q_w_tot

        data_dict_corr['Fqt'] = data_dict_corr['Fqt_coh'] + data_dict_corr['Fqt_incoh']
        data_dict_corr['Sqw'] = data_dict_corr['Sqw_coh'] + data_dict_corr['Sqw_incoh']
    else:
        data_dict_corr['Fqt'] = data_dict_corr['Fqt_coh'].copy()
        data_dict_corr['Sqw'] = data_dict_corr['Sqw_coh'].copy()

    # finalize results with additional meta dat
    result = DynamicSample(data_dict_corr, atom_types=traj.atom_types, pairs=pairs,
                           particle_counts=particle_counts, cell=traj.cell,
                           nyquist_frequency=f_N, max_frequency=w_max, frequency_resolution=dw)

    return result


def compute_static_structure_factors(
        traj: Trajectory,
        q_points: NDArray[float],
) -> StaticSample:
    r"""Compute static structure factors.  The results are returned in the
    form of a :class:`StaticSample <dynasor.sample.StaticSample>`
    object.

    Parameters
    ----------
    traj
        Input trajectory
    q_points
        Array of q-points in units of 2π/Å with shape ``(N_qpoints, 3)`` in Cartesian coordinates
    """
    # sanity check input args
    if q_points.shape[1] != 3:
        raise ValueError('q-points array has the wrong shape.')

    n_qpoints = q_points.shape[0]
    logger.info(f'Number of q-points: {n_qpoints}')

    # define all pairs
    pairs = list(combinations_with_replacement(traj.atom_types, r=2))
    particle_counts = {key: len(val) for key, val in traj.atomic_indices.items()}
    logger.debug('Considering pairs:')
    for pair in pairs:
        logger.debug(f'  {pair}')

    # processing function
    def f2_rho(frame):
        rho_qs_dict = dict()
        for atom_type in frame.positions_by_type.keys():
            x = frame.positions_by_type[atom_type]
            rho_qs_dict[atom_type] = calc_rho_q(x, q_points)
        frame.rho_qs_dict = rho_qs_dict
        return frame

    # setup averager
    Sq_averager = dict()
    for pair in pairs:
        Sq_averager[pair] = TimeAverager(1, n_qpoints)  # time average with only timelag=0

    # main loop
    for frame in traj:
        # process_frame
        f2_rho(frame)
        logger.debug(f'Processing frame {frame.frame_index}')

        for s1, s2 in pairs:
            # compute correlation
            Sq_pair = np.real(frame.rho_qs_dict[s1] * frame.rho_qs_dict[s2].conjugate())
            if s1 != s2:
                Sq_pair += np.real(frame.rho_qs_dict[s2] * frame.rho_qs_dict[s1].conjugate())
            Sq_averager[(s1, s2)].add_sample(0, Sq_pair)

    # collect results
    data_dict = dict()
    data_dict['q_points'] = q_points
    S_q_tot = np.zeros((n_qpoints, 1))
    for s1, s2 in pairs:
        Sq = 1 / traj.n_atoms * Sq_averager[(s1, s2)].get_average_at_timelag(0).reshape(-1, 1)
        data_dict[f'Sq_{s1}_{s2}'] = Sq
        S_q_tot += Sq
    data_dict['Sq'] = S_q_tot

    # finalize results
    result = StaticSample(data_dict, atom_types=traj.atom_types, pairs=pairs,
                          particle_counts=particle_counts, cell=traj.cell)
    return result


def compute_spectral_energy_density(
    traj: Trajectory,
    ideal_supercell: Atoms,
    primitive_cell: Atoms,
    q_points: NDArray[float],
    dt: float,
) -> Tuple[NDArray[float], NDArray[float]]:
    r"""
    Compute the spectral energy density (SED) at specific q-points.
    The results are returned in the form of a tuple, which comprises the
    angular frequencies in an array of length ``N_times`` in units of 2π/fs
    and the SED in units of Da*(Å/fs)² as an array of shape ``(N_qpoints, N_times)``.

    More details can be found in Thomas *et al.*, Physical Review B **81**, 081411 (2010),
    which should be cited when using this function along with the dynasor reference.

    **Note 1:**
    SED analysis is only suitable for crystalline materials without diffusion as
    atoms are assumed to move around fixed reference positions throughout the entire trajectory.

    **Note 2:**
    This implementation reads the full trajectory and can thus consume a lot of memory.

    Parameters
    ----------
    traj
        Input trajectory
    ideal_supercell
        Ideal structure defining the reference positions
    primitive_cell
        Underlying primitive structure. Must be aligned correctly with :attr:`ideal_supercell`.
    q_points
        Array of q-points in units of 2π/Å with shape ``(N_qpoints, 3)`` in Cartesian coordinates
    dt
        Time difference in femtoseconds between two consecutive snapshots in
        the trajectory. Note that you should not change :attr:`dt` if you change
        :attr:`frame_step <dynasor.trajectory.Trajectory.frame_step>` in :attr:`traj`.
    """

    delta_t = traj.frame_step * dt

    # logger
    logger.info('Running SED')
    logger.info(f'Time between consecutive frames (dt * frame_step): {delta_t} fs')

    # check that the ideal supercell agrees with traj
    if traj.n_atoms != len(ideal_supercell):
        raise ValueError('ideal_supercell must contain the same number of atoms as the trajectory.')

    # colllect all velocities
    velocities = []
    for it, frame in enumerate(traj):
        logger.debug(f'Reading frame {it}')
        if frame.velocities_by_type is None:
            raise ValueError(f'Could not read velocities from frame {it}')
        v = frame.get_velocities_as_array(traj.atomic_indices)
        velocities.append(v)

    velocities = np.array(velocities)
    velocities = velocities.transpose(1, 2, 0).copy()
    velocities = np.fft.fft(velocities, axis=2)

    # calculate SED
    masses = primitive_cell.get_masses()
    indices, offsets = get_index_offset(ideal_supercell, primitive_cell)

    pos = np.dot(q_points, np.dot(offsets, primitive_cell.cell).T)
    exppos = np.exp(1.0j * pos)
    density = np.zeros((len(q_points), velocities.shape[2]))
    for alpha in range(3):
        for b in range(len(masses)):
            tmp = np.zeros(density.shape, dtype=complex)
            for i in range(len(indices)):
                index = indices[i]
                if index != b:
                    continue
                tmp += np.outer(exppos[:, i], velocities[i, alpha])

            density += masses[b] * np.abs(tmp)**2

    # frequencies
    w = np.linspace(0.0, 2 * np.pi / delta_t, density.shape[1])  # units of 2pi/fs

    return w, density
