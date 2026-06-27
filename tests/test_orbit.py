import orbital_mechanics as om

def test_orbit_creation():
    orbit = om.Orbit(100 * om.u.km, 80 * om.u.km)
    assert orbit.apo == 100 * om.u.km
    assert orbit.peri == 80 * om.u.km

def test_body_semi_major_axis():
    orbit = om.Orbit(100 * om.u.km, 80 * om.u.km)
    assert orbit.semi_major_axis == ((100 + 80) / 2) * om.u.km

def test_body_eccentricity():
    orbit = om.Orbit(100 * om.u.km, 80 * om.u.km)
    assert orbit.eccentricity == (100 - 80) / (100 + 80)
