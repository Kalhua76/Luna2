from luna.container import ServiceContainer
from luna.kernel import LunaKernel


def test_container_register():

    container = ServiceContainer()

    kernel = LunaKernel()

    container.register(kernel)

    assert container.contains(LunaKernel)

    assert container.get(LunaKernel) is kernel