from pint import Quantity

from .units import u
from .utils import require_dimension

class Orbit:
    def __init__(self, r_apo: Quantity, r_peri: Quantity):
        require_dimension(r_apo,  "[length]", "r_apoapsis")
        require_dimension(r_peri, "[length]", "r_periapsis")
        
        self.r_apo  = r_apo
        self.r_peri = r_peri
        
    @property
    def semi_major_axis(self) -> Quantity:
        return (self.r_apo + self.r_peri) / 2
    
    @property
    def eccentricity(self) -> Quantity:
        return (self.r_apo - self.r_peri) / (self.r_apo + self.r_peri)
