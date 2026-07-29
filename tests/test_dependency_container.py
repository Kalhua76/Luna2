from luna.core.dependency_container import DependencyContainer

class Demo: ...

def test_register_resolve():
    c=DependencyContainer()
    obj=Demo()
    c.register_instance(Demo,obj)
    assert c.resolve(Demo) is obj
