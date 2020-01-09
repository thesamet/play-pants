from com.actioniq.play.register import global_subsystems


def test_global_subsystems():
    assert global_subsystems() == set()
