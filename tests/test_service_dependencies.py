from luna.core.service_manager import ServiceManager

events=[]
class A:
    def initialize(self): events.append("A")
class B:
    def initialize(self): events.append("B")

def test_dependency_order():
    sm=ServiceManager()
    sm.register("a",A())
    sm.register("b",B(),["a"])
    sm.initialize_all()
    assert events==["A","B"]
