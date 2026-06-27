from pint import Quantity
from numpy import pi

from .units import u
from .utils import require_dimension

def semi_major_axis(r_apo: Quantity, r_peri: Quantity) -> Quantity:
    """Calculate the semi-major axis of an orbit.

    Parameters
    ----------
    r_apo : Quantity
        Distance from the center of the central body to the apoapsis.
    r_peri : Quantity
        Distance from the center of the central body to the periapsis.

    Returns
    -------
    Quantity
        Semi-major axis of the orbit.
    """
    require_dimension(r_apo, u.m, "r_apo")
    require_dimension(r_peri, u.m, "r_peri")
    return (r_apo + r_peri) / 2

def eccentricity(r_apo: Quantity, r_peri: Quantity) -> float:
    """Calculate the eccentricity of an orbit.

    Parameters
    ----------
    r_apo : Quantity
        Distance from the center of the central body to the apoapsis.
    r_peri : Quantity
        Distance from the center of the central body to the periapsis.

    Returns
    -------
    float
        Eccentricity of the orbit.
    """
    require_dimension(r_apo, u.m, "r_apo")
    require_dimension(r_peri, u.m, "r_peri")
    return (r_apo - r_peri) / (r_apo + r_peri)

def vis_viva(mu: Quantity, r: Quantity, a: Quantity) -> Quantity:
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
    require_dimension(a, u.m, "a")
    return (mu * (2 / r - 1 / a)) ** 0.5

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

def orbital_period(mu: Quantity, a: Quantity) -> Quantity:
    """Calculate the orbital period of an orbit.

    Parameters
    ----------
    mu : Quantity
        Standard gravitational parameter of the central body.
    a : Quantity
        Semi-major axis of the orbit.

    Returns
    -------
    Quantity
        Orbital period of the orbit.
    """
    require_dimension(mu, u.m**3 / u.s**2, "mu")
    require_dimension(a, u.m, "a")
    return 2 * pi * (a**3 / mu) ** 0.5
