from numpy import pi

class Orbit:
    def __init__(self, r_apo: float, r_peri: float):
        self.r_apo  = r_apo
        self.r_peri = r_peri
        
    @property
    def semi_major_axis(self):
        return (self.r_apo + self.r_peri) / 2
    
    @property
    def eccentricity(self):
        return (self.r_apo - self.r_peri) / (self.r_apo + self.r_peri)
    
    def orbital_period(self, mu: float) -> float:
        """ Returns the orbital period of the orbit.
        
        Args:
            mu (float): Standard gravitational parameter of the central body.
        
        Returns:
            float: Orbital period in seconds.
        """
        return 2 * pi * (self.semi_major_axis**3 / mu) ** 0.5
