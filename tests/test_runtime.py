from luna.runtime import LunaRuntime


def test_runtime_creation():
    runtime = LunaRuntime()
    assert runtime is not None
