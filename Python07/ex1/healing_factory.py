from ex0.creature import Creature
from ex0.creature_factory import CreatureFactory
from .healing_creatures import   Bloomelle, Spourtling

class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Spourtling()

    def create_evolved(self) -> Creature:
        return Bloomelle()