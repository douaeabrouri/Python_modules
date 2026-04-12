#!/usr/bin/env python3
from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combine(target: str, power: int) -> tuple:
        result1 = spell1(target, power)
        result2= spell2(target, power)
        return (result1, result2)
    return combine

def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> str:
        mul: int = power * multiplier
        result = base_spell(target, mul)
        return result
    return amplifier

def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return caster

def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        sequen: list = []
        for spell in spells:
            sequen.append(spell(target, power))
        return sequen
    return sequence

if __name__ == "__main__":
    PURPLE: str = "\033[38;2;229;208;255m"
    RESET: str = "\033[0m"
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"
    
    def power_spell(target: str, power: int) -> str:
        return str(power)

    print(f"\n{PURPLE}Testing spell combiner...{RESET}")
    combiner = spell_combiner(fireball, heal)
    result = combiner('Dragon', 50)
    print(f"Combined spell result: {result[0]}, {result[1]}")
    
    print(f"\n{PURPLE}Testing power amplifier...{RESET}")
    mega = power_amplifier(power_spell, 3)
    print(f"Original: 10, Amplified: {mega('Dragon', 10)}")

    print(f"\n{PURPLE}Testing conditional caster...{RESET}")
    is_powerful = lambda target, power: power > 50
    cast = conditional_caster(is_powerful, fireball)
    print(f"conditional caster result: {cast('Dragon', 40)}")

    print(f"\n{PURPLE}Testing spell sequence...{RESET}")
    sequence_test = spell_sequence([fireball, heal])
    results = sequence_test('Dragon', 50)
    for result in results:
        print(result)
