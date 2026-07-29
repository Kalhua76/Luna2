from luna.core.application import LunaApplication

def test_create():
    app=LunaApplication()
    assert app is not None
