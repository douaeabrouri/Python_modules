#!/usr/bin/env python3
from collections.abc import Callable
from typing import Any

def mage_counter() -> Callable:
    count: int = 0

    def count_calls() -> int:
        nonlocal count
        count += 1
        return count

    return count_calls


def spell_accumulator(initial_power: int) -> Callable:
    total: int = initial_power

    def accumulate_power(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return accumulate_power


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, Any] = {}

    def store(key: str, value: int) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        if key in memory:
            return memory[key]
        else:
            return "Memory not found"

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    PURPLE: str = "\033[38;2;229;208;255m"
    RESET: str = "\033[0m"
    print(f"{PURPLE}Testing mage counter...{RESET}")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print(f"\n{PURPLE}Testing spell accumulator...{RESET}")
    base: int = 100
    result = spell_accumulator(base)
    print(f"Base {base}, add 20: {result(20)}")
    print(f"Base {base}, add 30: {result(30)}")
    print(f"\n{PURPLE}Testing enchantment factory...{RESET}")
    first_word: str = "1337"
    secand_word: str = "The"
    enchantment = enchantment_factory(first_word)
    print(enchantment("med"))
    obj = enchantment_factory(secand_word)
    print(obj("best"))
    print(f"\n{PURPLE}Testing memory vault...{RESET}")
    print("Store 'secret' = 42")
    vault: dict[str, Any] = memory_vault()
    vault["store"]("secret", 42)
    result = vault["recall"]("secret")
    unknow = vault["recall"]("unknow")
    print(f"Recall 'secret': {result}")
    print(f"Recall 'unknown': {unknow}")
