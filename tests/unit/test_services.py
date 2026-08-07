from app.platform.services import ServiceRegistry


def test_service_registry():
    registry = ServiceRegistry()
    service = object()

    registry.register("example", service)

    assert registry.contains("example")
    assert registry.get("example") is service
