from luna.memory.knowledge_base import KnowledgeBase, KnowledgeEntry

def test_knowledge_base():
    kb=KnowledgeBase()
    entry=KnowledgeEntry("luna","Projet Luna","Assistant IA",["projet"])
    kb.add(entry)
    assert kb.get("luna").title=="Projet Luna"
