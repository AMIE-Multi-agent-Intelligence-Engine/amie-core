from abc import ABC, abstractmethod


class Service(ABC):
    """Base interface for platform services."""

    @abstractmethod
    def start(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def stop(self) -> None:
        raise NotImplementedError
