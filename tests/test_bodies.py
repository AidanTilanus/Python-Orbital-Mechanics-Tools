import orbital_mechanics as om

def test_body_creation():
    body = om.Body(mass=100 * om.u.kg, radius=10 * om.u.m)
    assert body.mass.magnitude == 100
    assert body.radius.magnitude == 10


def test_gravitational_parameter():
    body = om.Body(mass=100 * om.u.kg, radius=10 * om.u.m)
    assert body.gravitational_parameter == om.G * body.mass


def test_altitude_to_r():
    body = om.Body(mass=100 * om.u.kg, radius=10 * om.u.m)
    r = body.altitude_to_r(5 * om.u.m)
    assert r.to("m").magnitude == 15
