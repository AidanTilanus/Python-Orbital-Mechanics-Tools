from .units import u
from .bodies import Body

MERCURY = Body(mass=3.3011e23 * u.kg, radius=2439.7 * u.km)
VENUS   = Body(mass=4.8675e24 * u.kg, radius=6051.8 * u.km)
EARTH   = Body(mass=5.9724e24 * u.kg, radius=6378.137 * u.km)
MOON    = Body(mass=7.342e22  * u.kg, radius=1737.4 * u.km)
MARS    = Body(mass=6.4171e23 * u.kg, radius=3396.2 * u.km)
JUPITER = Body(mass=1.8982e27 * u.kg, radius=71492 * u.km)
SATURN  = Body(mass=5.6834e26 * u.kg, radius=60268 * u.km)
URANUS  = Body(mass=8.6810e25 * u.kg, radius=25559 * u.km)
NEPTUNE = Body(mass=1.02413e26 * u.kg, radius=24764 * u.km)
