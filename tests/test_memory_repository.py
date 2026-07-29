from luna.memory.memory_repository import MemoryRepository

def test_memory_repository():
    repo=MemoryRepository("database/test_memory.db")
    repo.initialize()
    repo.save("project","Luna")
    assert repo.load("project")=="Luna"
    repo.shutdown()
