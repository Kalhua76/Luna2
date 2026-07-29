from luna.memory.memory_manager import MemoryManager

def test_memory_manager_store():
    mm=MemoryManager()
    mm.put("short_term","hello","world")
    assert mm.get("short_term","hello")=="world"
