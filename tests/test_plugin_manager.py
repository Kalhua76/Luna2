from luna.core.plugin_manager import PluginManager
from luna.plugins.plugin import Plugin

class DemoPlugin(Plugin):
    @property
    def name(self): return "demo"

def test_register_plugin():
    pm=PluginManager()
    pm.register(DemoPlugin())
    assert pm.list_plugins()==["demo"]
