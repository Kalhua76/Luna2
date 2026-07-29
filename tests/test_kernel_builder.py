from luna.core.kernel import LunaKernel

def test_builder_exists():
    k=LunaKernel()
    assert k.builder is not None
