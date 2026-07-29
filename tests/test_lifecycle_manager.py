from luna.core.lifecycle_manager import LifecycleManager
from luna.core.lifecycle import ApplicationState

def test_lifecycle():
    lm=LifecycleManager()
    lm.starting()
    assert lm.state==ApplicationState.STARTING
    lm.running()
    assert lm.state==ApplicationState.RUNNING
