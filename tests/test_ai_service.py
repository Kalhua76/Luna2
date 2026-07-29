from luna.ai.ai_service import AIService
from luna.ai.conversation_engine import ConversationEngine
from luna.ai.prompt_manager import PromptManager
from luna.ai.llm_provider import LLMProvider

class DummyProvider(LLMProvider):
    @property
    def name(self): return "dummy"
    def generate(self, prompt:str)->str: return "ok"

def test_ai_service():
    svc=AIService(ConversationEngine(DummyProvider(), PromptManager()))
    assert svc.ask("SYS", [], "Hello")=="ok"
