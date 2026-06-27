import numpy as np
from pint import Quantity

from .units import u
from .constants import G0
from .utils import require_dimension

class Stage:
    def __init__(self, isp: Quantity, wett_mass: Quantity, dry_mass: Quantity):
        require_dimension(isp, "[time]", "isp")
        require_dimension(wett_mass, "[mass]", "wett_mass")
        require_dimension(dry_mass, "[mass]", "dry_mass")
        
        self.isp = isp
        self.wett_mass = wett_mass
        self.dry_mass = dry_mass
    
    def __repr__(self) -> str:
        return f"Stage(isp={self.isp}, wett_mass={self.wett_mass}, dry_mass={self.dry_mass})"

    @property
    def max_dv(self) -> Quantity:
        return self.isp * G0 * np.log(self.wett_mass / self.dry_mass)

class Rocket:
    def __init__(self, stages: list[Stage]):
        self.stages = stages
    
    def __repr__(self) -> str:
        return f"Rocket(stages={self.stages})"
    
    def __len__(self) -> int:
        return len(self.stages)
    
    def __getitem__(self, index: int) -> Stage:
        return self.stages[index]
    
    def __iter__(self):
        return iter(self.stages)

    @property
    def max_dv(self) -> Quantity:
        return sum((stage.max_dv for stage in self.stages), start=0 * u.m / u.s)
    
    @property
    def wett_mass(self) -> Quantity:
        return sum((s.wett_mass for s in self.stages), start=0 * u.kg)

    @property
    def dry_mass(self) -> Quantity:
        return sum((s.dry_mass for s in self.stages), start=0 * u.kg)
