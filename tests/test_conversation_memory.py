from luna.memory.conversation_memory import ConversationMemory

def test_conversation_memory():
    mem=ConversationMemory()
    mem.add("user","Bonjour")
    mem.add("assistant","Salut !")
    assert len(mem.history())==2
    assert mem.last().role=="assistant"
