"""
This module provides an implementation of Filon's integration formula.
For information about Filon's formula, see e.g.
`Abramowitz and Stegun, Handbook of Mathematical Functions,
section 25 <http://mathworld.wolfram.com/FilonsIntegrationFormula.html>`_ or
Allen and Tildesley, *Computer Simulation of Liquids*, Appendix D :cite:`AllTil87`.

Integration is performed along one dimension (default ``axis=0``), e.g.,

.. code::

    [F0[0]  F1[0] ..  FN[0] ]     [f0[0]  f1[0] ..  fN[0] ]
    [   .      .         .  ]     [   .      .         .  ]
    [F0[.]  F1[.] ..  FN[.] ] = I([f0[.]  f1[.] ..  fN[.] ], dx, [q[0] .. q[Nq]])
    [   .      .         .  ]     [   .      .         .  ]
    [F0[Nq] F1[Nq] .. FN[Nq]]     [f0[Nx] f1[Nx] .. fN[Nx]]

where ``q`` and ``Fj`` have end index ``Nq``, and ``fj`` has end index ``Nx``.
``Nq`` is automatically set by the length of ``q``. Due to the algorithm,
``fj[Nx]`` must be of odd length (``Nx`` must be an even number), and should
correspond to a linearly spaced set of data points (separated by ``dx`` along the
integration axis).

:func:`sin_integral` and :func:`cos_integral` allow for shifted integration
intervals by the optional argument ``x0``.

"""

__all__ = ['fourier_cos', 'sin_integral', 'cos_integral']

from numpy import sin, cos, linspace, pi, arange
import numpy as np
import numba
from numpy.typing import NDArray
from typing import Tuple, Callable


def fourier_cos(f: NDArray[float],
                dx: float,
                q: NDArray[float] = None,
                axis: int = 0) -> Tuple[NDArray[float], NDArray[float]]:
    r"""Calculates the direct Fourier cosine transform :math:`F(q)` of a
    function :math:`f(x)` using Filon's integration method.

    The array values ``f[0]..f[2n]`` are expected to correspond to
    :math:`f(0.0)\ldots f(2n\Delta x)`. Hence, ``f`` should contain an odd
    number of elements.

    The transform is approximated by the integral
    :math:`F(q) = 2\int_{0}^{x_{max}} f(x) \cos(q x) dx`,
    where :math:`x_{max} = 2n \Delta x`.

    Parameters
    ----------
    f
        function values; must contain an odd number of elements
    dx
        spacing of x-axis (:math:`\Delta x`)
    q
        values of reciprocal axis, at which to evaluate transform;
        if ``q`` is not provided, ``linspace(0.0, 2*pi/dx, f.shape[axis])``,
        will be used.
    axis
        axis along which to carry out integration

    Returns
    -------
        tuple of ``q`` and ``F`` values

    Example
    -------
    A common use case is

    .. code-block:: python

        q, F = fourier_cos(f, dx)
    """

    if q is None:
        q = linspace(0.0, 2 * pi / dx, f.shape[axis])

    return q, 2 * cos_integral(f, dx, q, x0=0.0, axis=axis)


def cos_integral(f: NDArray[float],
                 dx: float,
                 q: NDArray[float],
                 x0: float = 0.0,
                 axis: int = 0) -> NDArray[float]:
    r"""Calculates the integral
    :math:`\int_{x_0}^{2n\Delta x} f(x) \cos(q x) dx`.

    Parameters
    ----------
    f
        function values; must contain an odd number of elements
    dx
        spacing of x-axis (:math:`\Delta x`)
    q
        values of reciprocal axis, at which to evaluate transform;
        if ``q`` is not provided, ``linspace(0.0, 2*pi/dx, f.shape[axis])``,
        will be used.
    x0
        offset for integration interval
    axis
        axis along which to carry out integration

    Returns
    -------
        Integral values
    """

    return _gen_sc_int(f, dx, q, x0, axis, cos)


def sin_integral(f: NDArray[float],
                 dx: float,
                 q: NDArray[float],
                 x0: float = 0.0,
                 axis: int = 0) -> NDArray[float]:
    r"""Calculates the integral
    :math:`\int_{x_0}^{2n\Delta x} f(x) \sin(q x) dx`.

    Parameters
    ----------
    f
        function values; must contain an odd number of elements
    dx
        spacing of x-axis (:math:`\Delta x`)
    q
        values of reciprocal axis, at which to evaluate transform;
        if ``q`` is not provided, ``linspace(0.0, 2*pi/dx, f.shape[axis])``,
        will be used.
    x0
        offset for integration interval
    axis
        axis along which to carry out integration

    Returns
    -------
        Integral values
    """
    return _gen_sc_int(f, dx, q, x0, axis, sin)


def _gen_sc_int(f: NDArray[float],
                dx: float,
                q: NDArray[float],
                x0: float,
                axis: int,
                sc: Callable) -> NDArray[float]:
    """ General sin/cos integral

    Due to numba sin or cos are sent in as strings
    """
    if sc == np.sin:
        sc = 'sin'
    else:
        assert sc == np.cos
        sc = 'cos'

    # Let numpy handle the axis juggling
    integral = np.apply_along_axis(_gen_sc_int_1D, axis, f, dx, q, x0, sc)

    return integral


@numba.njit(fastmath=False, parallel=True)
def _gen_sc_int_1D(f: NDArray, dx: float, k: NDArray, x0: float, sc: str) -> NDArray[float]:
    """Calculate filon for a 1D array

    Parameters
    ----------
    f
        function values; must contain an odd number of elements
    dx
        spacing of x-axis
    k
        values of reciprocal axis, at which to evaluate transform
    x0
        offset for integration interval
    sc
        sin or cos

    Returns
    -------
    integral
        integral of f at points k
    """

    # Keep it simple
    assert f.ndim == 1
    assert k.ndim == 1

    assert sc in ['sin', 'cos']

    Nk = len(k)
    Nx = len(f)

    assert Nx >= 3 and Nx % 2 == 1  # Nx odd and not one

    x = x0 + dx * arange(Nx)

    integral = np.empty(Nk)

    for i in numba.prange(Nk):
        integral[i] = filon_single_k(f, x, k[i], sc)

    return integral


@numba.njit(fastmath=False)
def filon_single_k(f: NDArray, x: NDArray, k: float, sc: str) -> float:
    """performs the integral at a single k-point"""

    dx = x[1] - x[0]

    alpha, beta, gamma = _alpha_beta_gamma_single(dx * k)

    if sc == 'sin':
        sc_x = np.sin(k * x)
    else:
        sc_x = np.cos(k * x)

    sc_x[0] *= 0.5
    sc_x[-1] *= 0.5

    Nx = len(x)
    B, C = 0.0, 0.0
    for i in range(0, Nx, 2):
        B += sc_x[i] * f[i]
    for i in range(1, Nx, 2):
        C += sc_x[i] * f[i]

    if sc == 'sin':
        A = f[0] * np.cos(k * x[0]) - f[-1] * np.cos(k * x[-1])
    else:
        A = f[-1] * np.sin(k * x[-1]) - f[0] * np.sin(k * x[0])

    integral = dx * (alpha * A + beta * B + gamma * C)

    return integral


@numba.njit(fastmath=False)
def _alpha_beta_gamma_single(t: float):
    # From theta, calculate alpha, beta, and gamma

    if t == 0:
        alpha, beta, gamma = 0.0, 2/3, 4/3
    else:
        alpha = (t**2 + t * np.sin(t) * np.cos(t) - 2 * np.sin(t)**2) / t**3
        beta = 2 * (t * (1 + np.cos(t)**2) - 2 * np.sin(t) * np.cos(t)) / t**3
        gamma = 4 * (np.sin(t) - t * np.cos(t)) / t**3

    return alpha, beta, gamma
