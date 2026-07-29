from luna.memory.knowledge_base import KnowledgeBase, KnowledgeEntry
from luna.memory.semantic_search import SemanticSearch

def test_search():
    kb=KnowledgeBase()
    kb.add(KnowledgeEntry("1","Projet Luna","Assistant IA"))
    engine=SemanticSearch(kb)
    assert engine.search("Luna")[0].identifier=="1"
