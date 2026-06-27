import orbital_mechanics as om

def test_stage_creation():
    stage = om.Stage(isp=300 * om.u.s, wett_mass=1000 * om.u.kg, dry_mass=200 * om.u.kg)
    assert stage.isp.magnitude == 300
    assert stage.wett_mass.magnitude == 1000
    assert stage.dry_mass.magnitude == 200

def test_stage_max_dv_is_positive():
    stage = om.Stage(isp=300 * om.u.s, wett_mass=1000 * om.u.kg, dry_mass=200 * om.u.kg)
    assert stage.max_dv.magnitude > 0

def test_rocket_with_two_stages():
    stage = om.Stage(isp=300 * om.u.s, wett_mass=1000 * om.u.kg, dry_mass=200 * om.u.kg)
    rocket = om.Rocket([stage, stage])
    assert len(rocket) == 2
    assert rocket.wett_mass.to("kg").magnitude == 2000
    