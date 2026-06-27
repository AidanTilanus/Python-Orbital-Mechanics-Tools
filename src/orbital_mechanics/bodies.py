from pint import Quantity
from numpy import pi

from .units import u
from .constants import G
from .utils import require_dimension

class Body:
    def __init__(self, mass: Quantity, radius: Quantity, rotation_period: Quantity = 0 * u.s):
        require_dimension(mass, "[mass]", "mass")
        require_dimension(radius, "[length]", "radius")
        require_dimension(rotation_period, "[time]", "rotation_period")

        self.mass = mass
        self.radius = radius
        self.rotation_period = rotation_period
    
    def __repr__(self) -> str:
        return f"Body(mass={self.mass}, radius={self.radius})"
    
    @property
    def gravitational_parameter(self) -> Quantity:
        return G * self.mass
    
    @property
    def geostationary_orbit_radius(self) -> Quantity:
        if self.rotation_period == 0 * u.s:
            raise ValueError("Body has no rotation period, cannot calculate geostationary orbit radius.")
        return (self.gravitational_parameter * self.rotation_period**2 / (4 * pi**2))**(1/3)
    
    def altitude_to_r(self, altitude: Quantity) -> Quantity:
        require_dimension(altitude, "[length]", "altitude")
        return self.radius + altitude
