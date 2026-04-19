#!/usr/bin/env python3
from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
from typing import Any
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        sum: int = reduce(operator.add, spells)
        return sum
    if operation == "max":
        max_nb: int = reduce(lambda x, y: x if x > y else y, spells)
        return max_nb
    if operation == "min":
        min_nb: int = reduce(lambda x, y: x if x < y else y, spells)
        return min_nb
    if operation == "multiply":
        mul = reduce(operator.mul, spells)
        return mul
    else:
        raise ValueError(f"unknow operation: {operation}")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = partial(base_enchantment, 50, "fire")
    ice = partial(base_enchantment, 50, "ice")
    thunder = partial(base_enchantment, 50, "thunder")
    return {
        "fire": fire,
        "ice": ice,
        "thunder": thunder,
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast(spell: Any) -> str:
        return "Unknow spell type"

    @cast.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return cast


if __name__ == "__main__":
    PURPLE: str = "\033[38;2;229;208;255m"
    RESET: str = "\033[0m"
    RED: str = "\033[31m"
    YELLOW: str = "\033[33m"
    print(f"\n{PURPLE}Testing spell reducer...{RESET}")
    liste: list[int] = [2, 4, 7, 8]
    print(f"sum: {spell_reducer(liste, 'add')}")
    print(f"product: {spell_reducer(liste, 'multiply')}")
    try:
        print(f"max: {spell_reducer(liste, 'maxx')}")
    except ValueError as e:
        print(f"{RED}Error caught: {e}{RESET}")
    print(f"\n{PURPLE}Testing partial enchante...{RESET}")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{element} enchantment on {target} with {power} power"

    enchanters = partial_enchanter(base_enchantment)
    print(enchanters["fire"]("Sword"))
    print(f"\n{PURPLE}Testing memoized fibonacci...{RESET}")
    print(f"{YELLOW}Fib(0){RESET}: {memoized_fibonacci(0)}")
    print(f"{YELLOW}Fib(1){RESET}: {memoized_fibonacci(1)}")
    print(f"{YELLOW}Fib(10){RESET}: {memoized_fibonacci(10)}")
    print(f"{YELLOW}Fib(15){RESET}: {memoized_fibonacci(15)}")
    print(f"\n{PURPLE}Testing spell dispatcher...{RESET}")
    cast = spell_dispatcher()
    print(cast(42))
    print(cast("fireball"))
    liste2: list = [1, 4, 5]
    print(cast(liste2))
    print(cast(cast))
