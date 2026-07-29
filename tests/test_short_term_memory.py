from luna.memory.short_term_memory import ShortTermMemory

def test_short_term_memory():
    mem=ShortTermMemory(max_items=3)
    mem.add("A")
    mem.add("B")
    assert mem.latest()==["A","B"]
