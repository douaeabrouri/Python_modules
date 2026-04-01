#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard as creat
from ex1.ArtifactCard import ArtifactCard as artifact
from ex1.SpellCard import SpellCard as spell
from ex1.Deck import Deck


if __name__ == "__main__":
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    dragon = creat("Fire Dragon", 5, "Legendary", 7, 5)
    bolt = spell("Lighting Bolt", 3 ,"Common", "deal 3 damage to target")
    crystal = artifact("Mana Crystal", 2, "Rare",7,  "+1 mana per turn")
    deck = Deck()
    deck.add_cards(bolt)
    deck.add_cards(crystal)
    deck.add_cards(dragon)
    print(f"Deck stats: {deck.get_deck_stats()}")
    print("\nDrawing and playing cards:\n")
    while True:
        card = deck.draw_card()
        if card is None:
            break
        print(f"drew: {card.name} ({card.get_card_info()['type']})")
        print(f"Play result: {card.play()}\n")
        
    print("Polymorphism in action: Same interface, different card behaviors!")