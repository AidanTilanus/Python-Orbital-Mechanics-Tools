from .orbit import Orbit

def vis_viva(mu, orbit: Orbit, r):
    """ Calculates the orbital speed at a given distance from the central body using the vis-viva equation.
    
    Args:
        mu (float): Standard gravitational parameter of the central body.
        orbit (Orbit): The orbit of the object.
        r (float): Distance from the center of the central body in meters.
    
    Returns:
        float: Orbital speed in meters per second.
    """
    return (mu * (2 / r - 1 / orbit.semi_major_axis)) ** 0.5

def circular_orbit_speed(mu, r):
    """ Calculates the speed of an object in a circular orbit.
    
    Args:
        mu (float): Standard gravitational parameter of the central body.
        r (float): Distance from the center of the central body in meters.
    
    Returns:
        float: Orbital speed in meters per second.
    """
    return (mu / r) ** 0.5

def escape_velocity(mu, r):
    """ Calculates the escape velocity from a given distance from the central body.
    
    Args:
        mu (float): Standard gravitational parameter of the central body.
        r (float): Distance from the center of the central body in meters.
    
    Returns:
        float: Escape velocity in meters per second.
    """
    return (2 * mu / r) ** 0.5
