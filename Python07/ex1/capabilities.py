from abc import ABC, abstractmethod

class HealCapability(ABC):
    @abstractmethod
    def heal() -> str:
        ...
class TransformCapability(ABC):
    def __init__(self) -> None:
        
    @abstractmethod
    def transform(self) -> str:
        ...
    @abstractmethod
    def revert(self) -> str:
        ...