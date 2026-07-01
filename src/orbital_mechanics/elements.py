from pint import Quantity
from numpy import pi

from .units import u
from .utils import require_dimension
from .orbit import Orbit

def vis_viva(mu, orbit: Orbit, r):

    return (mu * (2 / r - 1 / orbit.semi_major_axis)) ** 0.5

def circular_orbit_speed(mu, r):

    return (mu / r) ** 0.5

def escape_velocity(mu, r):

    return (2 * mu / r) ** 0.5
