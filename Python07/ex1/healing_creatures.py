from ex1.capabilities import HealCapability
from battle import Creature

class Spourtling(Creature, HealCapability):
	def __init__(self) -> None:
		super().__init__("Sproutling", "Grass")

	def attack(self) -> str:
		return "Sproutling uses Vine Whip!"

	def heal() -> str:
		return "Sproutling heals itself for a small amount"

class Bloomelle(Creature, HealCapability):
	def __init__(self) -> None:
		super().__init__("Bloomelle", "Grass/Fairy")

	def attack(self) -> str:
		return "Bloomelle uses Petal Dance!"
	
	def heal(self) -> str:
		return "Bloomelle heals itself and others for a large amount"