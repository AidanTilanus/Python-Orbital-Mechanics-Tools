from pint import Quantity
from numpy import pi

from .units import u
from .utils import require_dimension
from .orbit import Orbit

def vis_viva(mu: Quantity, orbit: Orbit, r: Quantity) -> Quantity:
    """Calculate the orbital speed using the vis-viva equation.

    Parameters
    ----------
    mu : Quantity
        Standard gravitational parameter of the central body.
    r : Quantity
        Distance from the center of the central body to the orbiting object.
    a : Quantity
        Semi-major axis of the orbit.

    Returns
    -------
    Quantity
        Orbital speed at distance r.
    """
    require_dimension(mu, u.m**3 / u.s**2, "mu")
    require_dimension(r, u.m, "r")
    return (mu * (2 / r - 1 / orbit.semi_major_axis)) ** 0.5

def circular_orbit_speed(mu: Quantity, r: Quantity) -> Quantity:
    """Calculate the orbital speed for a circular orbit.

    Parameters
    ----------
    mu : Quantity
        Standard gravitational parameter of the central body.
    r : Quantity
        Radius of the circular orbit.

    Returns
    -------
    Quantity
        Orbital speed for a circular orbit at radius r.
    """
    require_dimension(mu, u.m**3 / u.s**2, "mu")
    require_dimension(r, u.m, "r")
    return (mu / r) ** 0.5

def escape_velocity(mu: Quantity, r: Quantity) -> Quantity:
    """Calculate the escape velocity from a given distance.

    Parameters
    ----------
    mu : Quantity
        Standard gravitational parameter of the central body.
    r : Quantity
        Distance from the center of the central body.

    Returns
    -------
    Quantity
        Escape velocity at distance r.
    """
    require_dimension(mu, u.m**3 / u.s**2, "mu")
    require_dimension(r, u.m, "r")
    return (2 * mu / r) ** 0.5
