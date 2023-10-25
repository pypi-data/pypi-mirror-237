from ase import io
from dynasor.trajectory.abstract_trajectory_reader import AbstractTrajectoryReader
from dynasor.trajectory.trajectory_frame import ReaderFrame
from itertools import count


class ASETrajectoryReader(AbstractTrajectoryReader):
    """Read ASE trajectory file

    ...

    Parameters
    ----------
    filename
        Name of input file.
    x_factor
        Conversion factor between the length unit used in the trajectory and the internal
        dynasor length unit.
    t_factor
        Conversion factor between the time unit used in the trajectory and the internal
        dynasor time unit.
    """

    def __init__(self,
                 filename: str,
                 x_factor: float = 0.1,
                 t_factor: float = 1.0):
        self.x_factor = x_factor
        self.t_factor = t_factor
        self.v_factor = x_factor / t_factor
        self._frame_index = count(0)
        self._atoms = io.iread(filename, index=':')

    def __iter__(self):
        return self

    def close(self):
        if not self._fh.closed:
            self._fh.close()

    def __next__(self):
        ind = self._frame_index
        next(self._frame_index)
        a = next(self._atoms)
        return ReaderFrame(
            frame_index=ind,
            n_atoms=len(a),
            cell=self.x_factor * a.cell.array.copy('F'),
            positions=self.x_factor * a.get_positions(),
            velocities=self.v_factor * a.get_velocities(),
        )
