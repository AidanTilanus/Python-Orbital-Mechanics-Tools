from .bodies import Body

SUN = Body(mass=1.9885e30, radius=695_700,
           rotation_period=2_164_320)           # 25.05 days (sidereal, equatorial)
MERCURY = Body(mass=3.3011e23, radius=2439.7,
                rotation_period=5_067_031.68)   # 58.6462 days
VENUS   = Body(mass=4.8675e24, radius=6051.8,
                rotation_period=20_997_152.64)  # 243.0226 days, retrograde
EARTH   = Body(mass=5.9724e24, radius=6378.137,
                rotation_period=86164.0905)     # sidereal day
MOON    = Body(mass=7.342e22, radius=1737.4,
                rotation_period=2_360_591.5)    # 27.321661 days, tidally locked
MARS    = Body(mass=6.4171e23, radius=3396.2,
                rotation_period=88_642.66)      # 1.025957 days
JUPITER = Body(mass=1.8982e27, radius=71492,
                rotation_period=35_730)         # 9h 55m 30s
SATURN  = Body(mass=5.6834e26, radius=60268,
                rotation_period=38_018)         # 10h 33m 38s
URANUS  = Body(mass=8.6810e25, radius=25559,
                rotation_period=62_064)         # 17h 14m, retrograde
NEPTUNE = Body(mass=1.02413e26, radius=24764,
                rotation_period=57_996)         # 16h 6m
