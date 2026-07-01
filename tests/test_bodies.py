import orbital_mechanics as om

def test_body_creation():
    body = om.Body(mass=100, radius=10)
    assert body.mass == 100
    assert body.radius == 10

def test_gravitational_parameter():
    body = om.Body(mass=100, radius=10)
    assert body.gravitational_parameter == om.G * body.mass

def test_altitude_to_r():
    body = om.Body(mass=100, radius=10)
    r = body.altitude_to_r(5)
    assert r == 15
