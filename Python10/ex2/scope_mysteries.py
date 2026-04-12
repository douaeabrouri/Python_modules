#!/usr/bin/env python3
from collections.abc import Callable


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
	memory: dict[str, Callable] = {}
	def store(key: str, value: int):
		memory[key] = value
	def recall(key: str):
		if key in memory:
			return memory[key]
		else:
			return "Memory not found"
	return {'store': store, 'recall': recall}

if __name__ == "__main__":
    PURPLE: str = "\033[38;2;229;208;255m"
    RESET: str = "\033[0m"
    print(f"{PURPLE}Testing mage counter...{RESET}")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print(f"{PURPLE}Testing spell accumulator...{RESET}")
    base: int = 100
    result = spell_accumulator(base)
	result 
