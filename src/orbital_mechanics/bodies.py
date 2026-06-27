from pint import Quantity

from .units import u
from .constants import G
from .utils import require_dimension

class Body:
    def __init__(self, mass: Quantity, radius: Quantity):
        require_dimension(mass, "[mass]", "mass")
        require_dimension(radius, "[length]", "radius")

        self.mass = mass
        self.radius = radius
    
    def __repr__(self) -> str:
        return f"Body(mass={self.mass}, radius={self.radius})"
    
    @property
    def gravitational_parameter(self) -> Quantity:
        return G * self.mass
    
    def altitude_to_r(self, altitude: Quantity) -> Quantity:
        require_dimension(altitude, "[length]", "altitude")
        return self.radius + altitude
