from dataclasses import dataclass
from enum import Enum


class KernelState(str, Enum):
    CREATED = "created"
    RUNNING = "running"
    STOPPED = "stopped"


@dataclass
class CognitiveKernel:
    """Minimal lifecycle foundation for the AMIE platform kernel."""

    state: KernelState = KernelState.CREATED

    def start(self) -> None:
        if self.state is KernelState.STOPPED:
            raise RuntimeError("A stopped kernel cannot be restarted.")
        self.state = KernelState.RUNNING

    def stop(self) -> None:
        self.state = KernelState.STOPPED

    @property
    def running(self) -> bool:
        return self.state is KernelState.RUNNING
