from pint import UnitRegistry, Quantity
u = UnitRegistry()

#SECTION Define Physical Constants

G: Quantity = 6.6743e-11 * (u.m**3 / (u.kg * u.s**2))
GRAVITANTIONAL_CONSTANT: Quantity = G

G0: Quantity = 9.80665 * (u.m / u.s**2)
standard_gravity = G0
