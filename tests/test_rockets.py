import orbital_mechanics as om

def test_stage_creation():
    stage = om.Stage(isp=300, wett_mass=1000, dry_mass=200)
    assert stage.isp == 300
    assert stage.wett_mass == 1000
    assert stage.dry_mass == 200

def test_stage_max_dv_is_positive():
    stage = om.Stage(isp=300, wett_mass=1000, dry_mass=200)
    assert stage.max_dv > 0

def test_rocket_with_two_stages():
    stage = om.Stage(isp=300, wett_mass=1000, dry_mass=200)
    rocket = om.Rocket([stage, stage])
    assert len(rocket) == 2
    assert rocket.wett_mass == 2000
    