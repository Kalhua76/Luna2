from datetime import datetime
from luna.memory.long_term_memory import LongTermMemory
from luna.memory.memory_record import MemoryRecord

def test_long_term_memory():
    mem=LongTermMemory()
    rec=MemoryRecord("project","Luna",datetime.utcnow())
    mem.remember(rec.key,rec)
    assert mem.recall("project").value=="Luna"
