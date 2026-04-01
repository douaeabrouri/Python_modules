from ex0.Card import Card

class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.used = False
        self.effect_type = effect_type

    def play(self) -> dict:
        self.used = True
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Deal 3 damage to target"
        }

    def resolve_effect(self, targets: list[str])-> dict:
        return {
            'spell': self.name,
            'effect_type': self.effect_type,
            'targets': targets,
            'resolved': True
		}
    
    def get_card_info(self) -> None:
        info = super().get_card_info()
        info['type'] = "spell"
        info['effect_type'] = self.effect_type
        return info
