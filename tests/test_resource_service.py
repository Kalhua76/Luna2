from luna.services.resource_service import ResourceService

def test_resource_path():
    rs = ResourceService()
    assert str(rs.get_path("logo.png")).endswith("assets/logo.png")
