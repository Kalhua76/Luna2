from luna.ai.llm_provider import LLMProvider

class DummyProvider(LLMProvider):
    @property
    def name(self): return "dummy"
    def generate(self,prompt:str)->str:
        return "ok"

def test_dummy_provider():
    p=DummyProvider()
    assert p.generate("hello")=="ok"
