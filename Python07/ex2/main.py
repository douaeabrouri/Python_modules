#!/usr/bin/env python3

from ex2.EliteCard import EliteCard


def main():
    print("=== DataDeck Ability System ===")

    card = EliteCard("Arcane Warrior", 6, "Legendary", 5, 8, 4)

    print("\nEliteCard capabilities:")
    print(f"- Card: {['play', 'get_card_info', 'is_playable']}")
    print(f"- Combatable: {['attack', 'defend', 'get_combat_stats']}")
    print(f"- Magical: {['cast_spell', 'channel_mana', 'get_magic_stats']}")

    print("\nPlaying Arcane Warrior (Elite Card):")
    print(f"Play result: {card.play({})}")

    print("\nCombat phase:")
    print(f"Attack result: {card.attack('Enemy')}")
    print(f"Defense result: {card.defend(2)}")

    print("\nMagic phase:")
    print(f"Spell cast: {card.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {card.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()