from luna.core.service_manager import ServiceManager

class Dummy:
    def __init__(self):
        self.started=False
    def initialize(self):
        self.started=True
    def shutdown(self):
        self.started=False

def test_register_and_initialize():
    sm=ServiceManager()
    d=Dummy()
    sm.register("dummy", d)
    sm.initialize_all()
    assert d.started
    sm.shutdown_all()
    assert not d.started
