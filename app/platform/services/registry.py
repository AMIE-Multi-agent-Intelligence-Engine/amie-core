from dataclasses import dataclass, field
from typing import Dict


@dataclass
class ServiceRegistry:
    """Simple in-process registry; replaceable by a distributed implementation later."""

    _services: Dict[str, object] = field(default_factory=dict)

    def register(self, name: str, service: object) -> None:
        if not name:
            raise ValueError("Service name cannot be empty.")
        self._services[name] = service

    def get(self, name: str) -> object:
        return self._services[name]

    def contains(self, name: str) -> bool:
        return name in self._services
