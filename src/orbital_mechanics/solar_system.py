from .units import u
from .bodies import Body

SUN = Body(mass=1.9885e30 * u.kg, radius=695_700 * u.km,
           rotation_period=2_164_320 * u.s)   # 25.05 days (sidereal, equatorial)
MERCURY = Body(mass=3.3011e23 * u.kg, radius=2439.7 * u.km,
                rotation_period=5_067_031.68 * u.s)   # 58.6462 days
VENUS   = Body(mass=4.8675e24 * u.kg, radius=6051.8 * u.km,
                rotation_period=20_997_152.64 * u.s)  # 243.0226 days, retrograde
EARTH   = Body(mass=5.9724e24 * u.kg, radius=6378.137 * u.km,
                rotation_period=86164.0905 * u.s)     # sidereal day
MOON    = Body(mass=7.342e22  * u.kg, radius=1737.4 * u.km,
                rotation_period=2_360_591.5 * u.s)    # 27.321661 days, tidally locked
MARS    = Body(mass=6.4171e23 * u.kg, radius=3396.2 * u.km,
                rotation_period=88_642.66 * u.s)      # 1.025957 days
JUPITER = Body(mass=1.8982e27 * u.kg, radius=71492 * u.km,
                rotation_period=35_730 * u.s)         # 9h 55m 30s
SATURN  = Body(mass=5.6834e26 * u.kg, radius=60268 * u.km,
                rotation_period=38_018 * u.s)         # 10h 33m 38s
URANUS  = Body(mass=8.6810e25 * u.kg, radius=25559 * u.km,
                rotation_period=62_064 * u.s)         # 17h 14m, retrograde
NEPTUNE = Body(mass=1.02413e26 * u.kg, radius=24764 * u.km,
                rotation_period=57_996 * u.s)         # 16h 6m
