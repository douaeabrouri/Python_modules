from ex0.creature_factory import CreatureFactory
from ex0.creature import Creature
from .transform_creatures import Shiftling, Morphagon

class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()