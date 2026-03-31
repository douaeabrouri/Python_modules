from ex0.Card import Card

class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int):
        self.attack = attack
        self.health = health
        super().__init__(name, cost, rarity)

        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive!")

    def play(self) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summond to battlefied",
        }

    def get_card_info(self) -> dict:
        info: dict = super().get_card_info()
        info["type"] = "Creature"
        info["attack"] = self.attack
        info["health"] = self.health
        return info

    def attack_target(self, target: list) -> dict:
        return {
            "attacker": self.name,
            "target": target.name if hasattr(target, "name") else target,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }
