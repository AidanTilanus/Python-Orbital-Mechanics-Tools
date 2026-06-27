from pint import Quantity

from .units import u
from .utils import require_dimension

class BurnVector:
    def __init__(self, prograde=0.0 * u.m / u.s, normal=0.0 * u.m / u.s, radial=0.0 * u.m / u.s):
        require_dimension(prograde, "[length] / [time]", "prograde")
        require_dimension(normal, "[length] / [time]", "normal")
        require_dimension(radial, "[length] / [time]", "radial")

        self._prograde = prograde
        self._normal = normal
        self._radial = radial
        
    def __repr__(self) -> str:
        return f"BurnVector(prograde={self._prograde}, normal={self._normal}, radial={self._radial})"
    
    def __add__(self, other: "BurnVector") -> "BurnVector":
        return BurnVector(
            prograde=self._prograde + other._prograde,
            normal=self._normal + other._normal,
            radial=self._radial + other._radial
        )
    
    def __sub__(self, other: "BurnVector") -> "BurnVector":
        return BurnVector(
            prograde=self._prograde - other._prograde,
            normal=self._normal - other._normal,
            radial=self._radial - other._radial
        )
    
    def total_dv(self) -> Quantity:
        return (self._prograde**2 + self._normal**2 + self._radial**2)**0.5
    
    #SECTION Getters and Setters for BurnVector Components    
    @property
    def prograde(self):
        return self._prograde

    @prograde.setter
    def prograde(self, value):
        self._prograde = value

    @property
    def retrograde(self):
        return -self._prograde

    @retrograde.setter
    def retrograde(self, value):
        self._prograde = -value

    @property
    def radial_out(self):
        return self._radial

    @radial_out.setter
    def radial_out(self, value):
        self._radial = value

    @property
    def radial_in(self):
        return -self._radial

    @radial_in.setter
    def radial_in(self, value):
        self._radial = -value

    @property
    def normal(self):
        return self._normal

    @normal.setter
    def normal(self, value):
        self._normal = value

    @property
    def antinormal(self):
        return -self._normal

    @antinormal.setter
    def antinormal(self, value):
        self._normal = -value
