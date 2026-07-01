import numpy as np

from .constants import G0

class Stage:
    def __init__(self, isp: float, wett_mass: float, dry_mass: float):
        self.isp = isp
        self.wett_mass = wett_mass
        self.dry_mass = dry_mass
    
    def __repr__(self) -> str:
        return f"Stage(isp={self.isp}, wett_mass={self.wett_mass}, dry_mass={self.dry_mass})"

    @property
    def max_dv(self):
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
    def max_dv(self):
        return sum((stage.max_dv for stage in self.stages), start=0)

    @property
    def wett_mass(self):
        return sum((s.wett_mass for s in self.stages), start=0)

    @property
    def dry_mass(self):
        return sum((s.dry_mass for s in self.stages), start=0)
