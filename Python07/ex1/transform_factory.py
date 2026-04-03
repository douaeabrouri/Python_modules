from ex0 import CreatureFactory  # import from ex0
from .transform_creatures import Shiftling, Morphagon

class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()