from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str ,attack: int, health: int, mana: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.mana = cost

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.mana,
            'effect': 'Elite card summoned with combat and magic abilities'
        }
    
    def attack(self, target: dict) -> dict:
        return {
            'attacker': self.name,
            'target': target.name,
            'damege': self.attack,
            'combat_type': "melee"
        }
    def defend(self, incoming_damage: int) -> dict:
        return {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': self.health // 2,
            'stile_alive': incoming_damage - self.health
        }