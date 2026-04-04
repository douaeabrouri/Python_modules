from abc import ABC, abstractmethod


class CreatureFactory(ABC):
    @abstractmethod
    # flaming/aquabub
    def create_base(self):
        pass

    # pyrodon/ torragon
    @abstractmethod
    def create_evolved(self):
        pass
