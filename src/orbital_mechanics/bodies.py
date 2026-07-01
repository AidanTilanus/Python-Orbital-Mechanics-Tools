from numpy import pi

from .constants import G

class Body:
    def __init__(self, mass: float, radius: float, rotation_period: float = 0):
        self.mass = mass
        self.radius = radius
        self.rotation_period = rotation_period
    
    def __repr__(self) -> str:
        return f"Body(mass={self.mass}, radius={self.radius})"
    
    @property
    def gravitational_parameter(self):
        return G * self.mass
    
    @property
    def synchronous_orbit_radius(self):
        if self.rotation_period == 0:
            raise ValueError("Body has no rotation period, cannot calculate geostationary orbit radius.")
        return (self.gravitational_parameter * self.rotation_period**2 / (4 * pi**2))**(1/3)
    
    def altitude_to_r(self, altitude: float):
        """ Converts altitude above the surface to the distance from the center of the body.
        
        Args:
            altitude (float): Altitude above the surface in meters.
        
        Returns:
            float: Distance from the center of the body in meters.
        """
        return self.radius + altitude
