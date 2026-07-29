from luna.ai.provider_registry import ProviderRegistry
from luna.ai.llm_provider import LLMProvider

class Dummy(LLMProvider):
    @property
    def name(self): return "dummy"
    def generate(self,prompt:str)->str: return "ok"

def test_registry():
    r=ProviderRegistry()
    r.register(Dummy())
    assert r.available()==["dummy"]
