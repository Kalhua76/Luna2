from luna.ai.conversation_engine import ConversationEngine
from luna.ai.prompt_manager import PromptManager
from luna.ai.llm_provider import LLMProvider

class DummyProvider(LLMProvider):
    @property
    def name(self): return "dummy"
    def generate(self,prompt:str)->str: return "response"

def test_engine():
    assert ConversationEngine(DummyProvider(),PromptManager()).chat("SYS",[],"Hi")=="response"
