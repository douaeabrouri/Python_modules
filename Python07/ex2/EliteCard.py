from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str ,attack: int, health: int, mana: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.mana,
            'effect': 'Elite card summoned with combat and magic abilities'
        }
    
    def attack(self, target: dict) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack,
            'combat_type': "melee"
        }
    def defend(self, incoming_damage: int) -> dict:
        return {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': self.health // 2,
            'stile_alive': incoming_damage < self.health
        }
    def get_combat_stats(self) -> dict:
        return {
            'name': self.name,
            'attack': self.attack,
            'health': self.health
        }
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': self.cost
        }
    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            'channeled': amount,
            'total_mana':  self.mana
        }
    def get_magic_stats(self) -> dict:
        return {
            'name': self.name,
            'mana': self.mana
        }
