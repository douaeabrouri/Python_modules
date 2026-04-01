from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random

class Deck:
    def __init__(self) -> None:
        self.cards: list = []
    def add_cards(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.card:
            if card_name == card.name:
                self.add_cards.remove(card)
                return True
        return False
    def shuffle(self) -> None:
        random.shuffle(self.cards)
    def draw_card(self) -> Card:
        if not self.cards:
            return None
        return self.cards.pop(0)
    def get_deck_stats(self) -> dict:
        total: int = len(self.cards)
        creature_count: int = 0
        spell_count: int = 0
        artifact_count: int = 0
        for card in self.cards:
            if isinstance(card, CreatureCard):
               creature_count += 1
            elif isinstance(card, SpellCard):
                spell_count += 1
            elif isinstance(card, ArtifactCard):
               artifact_count += 1
        avg_cost = sum(c.cost for c in self.cards) / total if total > 0 else 0
        return {
            'total_cards': total,
            'creatures': creature_count,
            'spells': spell_count,
            'artifacts': artifact_count,
            'avg_cost': round(avg_cost, 1)
        }
