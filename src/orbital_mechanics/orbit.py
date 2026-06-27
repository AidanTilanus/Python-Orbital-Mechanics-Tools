from pint import Quantity

from .units import u
from .utils import require_dimension

class Orbit:
    def __init__(self, apo: Quantity, peri: Quantity):
        require_dimension(apo,  "[length]", "apoapsis")
        require_dimension(peri, "[length]", "periapsis")
        
        self.apo  = apo
        self.peri = peri
        
        @property
        def semi_major_axis(self) -> Quantity:
            return (apo + peri) / 2
        
        @property
        def eccentricity(self) -> Quantity:
            return (apo - peri) / (apo + peri)
