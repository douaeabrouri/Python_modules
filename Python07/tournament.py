#!/usr/bin/env python3
from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy


def battle(opponents: list):
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i, (factory1, strategy1) in enumerate(opponents):
        for j, (factory2, strategy2) in enumerate(opponents):
            if i >= j:
                continue
            print("\n* Battle *")
            player1 = factory1.create_base()
            player2 = factory2.create_base()
            print(player1.describe())
            print("vs.")
            print(player2.describe())
            print(" now fight!")
            try:
                strategy1.act(player1)
                strategy2.act(player2)
            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    normal = NormalStrategy()
    defensive = DefensiveStrategy()
    aggressive = AggressiveStrategy()
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(FlameFactory(), normal), (HealingCreatureFactory(), defensive)])

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(FlameFactory(), aggressive),
            (HealingCreatureFactory(), defensive)])

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(
        [
            (AquaFactory(), normal),
            (HealingCreatureFactory(), defensive),
            (TransformCreatureFactory(), aggressive),
        ]
    )
