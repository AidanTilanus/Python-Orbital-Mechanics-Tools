import orbital_mechanics as om

def test_orbit_creation():
    orbit = om.Orbit(100, 80)
    assert orbit.r_apo  == 100
    assert orbit.r_peri == 80

def test_body_semi_major_axis():
    orbit = om.Orbit(100, 80)
    assert orbit.semi_major_axis == ((100 + 80) / 2)

def test_body_eccentricity():
    orbit = om.Orbit(100, 80)
    assert orbit.eccentricity == (100 - 80) / (100 + 80)

def test_body_inclination():
    orbit = om.Orbit(100, 80, inclination=30)
    assert orbit.inclination == 30
