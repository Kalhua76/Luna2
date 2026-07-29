from luna.core.service_registry import ServiceRegistry
from luna.core.service_manager import ServiceManager

class Dummy: ...

def test_registry_register():
    sm=ServiceManager()
    reg=ServiceRegistry(sm)
    obj=Dummy()
    reg.register("dummy",obj)
    assert reg.get("dummy") is obj
