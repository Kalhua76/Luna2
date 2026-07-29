from luna.ai.chat_pipeline import ChatPipeline
from luna.ai.session import ConversationSession
from luna.ai.ai_service import AIService
from luna.ai.conversation_engine import ConversationEngine
from luna.ai.prompt_manager import PromptManager
from luna.ai.llm_provider import LLMProvider

class Dummy(LLMProvider):
    @property
    def name(self): return "dummy"
    def generate(self,prompt:str)->str: return "Bonjour"

def test_pipeline():
    pipe=ChatPipeline(AIService(ConversationEngine(Dummy(),PromptManager())))
    s=ConversationSession(system_prompt="SYS")
    assert pipe.process(s,"Salut")=="Bonjour"
    assert len(s.history)==2
