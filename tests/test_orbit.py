import orbital_mechanics as om

def test_orbit_creation():
    orbit = om.Orbit(100 * u.km, 80 * u.km)
    assert orbit.apo == 100
    assert orbit.peri == 80

def test_body_semi_major_axis():
    orbit = om.Orbit(100 * u.km, 80 * u.km)
    assert orbit.semi_major_axis == ((100 + 80) / 2) * u.km

def test_body_eccentricity():
    orbit = om.Orbit(100 * u.km, 80 * u.km)
    assert orbit.eccentricity == (100 - 20) / (100 + 80) * u.km
