#!/usr/bin/env python3

from ex0.CreatureCard import CreatureCard

if __name__ == "__main__":
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")
    dragon: dict = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print("CreatureCard Info:")
    print(dragon.get_card_info())
    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"playable: {dragon.is_playable(6)}")
    print(f"Play result: {dragon.play()}")
    print("\nFire Dragon attacks Goblin Warrior:")
    goblin: dict = CreatureCard("Goblin Warrior", 2, "Common", 2, 1)
    print(f"Playable: {dragon.attack_target(goblin)}")
    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {goblin.is_playable(1)}")
    print("\nAbstract pattern successfully demonstrated!")
