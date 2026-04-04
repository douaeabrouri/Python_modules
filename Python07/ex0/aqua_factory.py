from .creature_factory import CreatureFactory
from .aqua_creatures import Aquabub, Torragon


class AquaFactory(CreatureFactory):
    def create_base(self):
        return Aquabub()

    def create_evolved(self):
        return Torragon()
