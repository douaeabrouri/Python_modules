from typing import Dict
from ex0.Card import Card

class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        
    def get_card_info(self) -> Dict:
        info: dict = super().get_card_info()
        info['type'] = "artifact"
        info['durability'] = self.durability
        info['effect'] = self.effect
        return info 

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}"
        }
    
    def activate_ability(self) -> dict:
        if self.durability <= 0:
            return {"activated": False, "reason": "Artifact destroyed"}
        self.durability -= 1
        return {
            "artifact": self.name,
            "effect": self.effect,
            "durability_remaining": self.durability,
            "activated": True
		}