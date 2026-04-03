from abc import ABC, abstractmethod

class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...
    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...