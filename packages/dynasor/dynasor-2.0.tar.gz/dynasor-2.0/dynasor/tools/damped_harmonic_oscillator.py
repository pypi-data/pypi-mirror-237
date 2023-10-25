import numpy as np
from numpy.typing import NDArray


def acf_position_dho(t: NDArray[float], w0: float, gamma: float, A: float = 1.0):
    r"""
    The damped damped harmonic oscillator (DHO) autocorrelation function for the position
    in the under-damped case.

    .. math::
        F(t) = A \exp{ (-\Gamma t/2)} \left [ \cos(\omega_e t) + \frac{\Gamma}{2\omega_e}
               \sin(\omega_e t) \right ]

    with

    .. math::
        \omega_e = \sqrt{\omega_0^2 - \Gamma^2 / 4}


    Parameters
    ----------
    t
        time array
    w0
        natural angular frequency of the DHO
    gamma
        Damping of DHO
    A
        amplitude of the DHO
    """
    we = np.sqrt(w0**2 - gamma**2 / 4.0)
    return A * np.exp(-gamma * np.abs(t) / 2.0) * (
        np.cos(we * t) + 0.5 * gamma / we * np.sin(we * np.abs(t)))


def spectra_position_dho(w: NDArray[float], w0: float, gamma: float, A: float = 1.0):
    r"""
    The damped harmonic oscillator (DHO) spectral function (i.e.,
    the Fourier transform of the autocorrelation function) for the position.

    .. math::
        S(\omega) = \frac{2 A \omega_0^2 \Gamma} {(\omega^2 - \omega_0^2)^2 + (\omega \Gamma)^2}

    Parameters
    ----------
    w
        angular frequency array
    w0
        natural angular frequency of the DHO
    gamma
        Damping of DHO
    A
        amplitude of the DHO
    """
    return 2 * w0**2 * A * gamma / ((w**2 - w0**2)**2 + (w * gamma)**2)
