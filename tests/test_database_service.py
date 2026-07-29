from luna.services.database_service import DatabaseService

def test_database_initialize():
    service = DatabaseService("database/test.db")
    service.initialize()
    assert service.connection is not None
    service.shutdown()
