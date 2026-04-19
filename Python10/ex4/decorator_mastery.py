#!/usr/bin/env python3
from collections.abc import Callable
from functools import wraps
from typing import Any
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = args[-1]
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    RESET: str = "\033[0m"
    RED: str = "\033[31m"
    GREEN = "\033[92m"

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"{RED}Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts}){RESET}"
                    )
            return (
                f"{GREEN}Spell casting failed after"
                f" {max_attempts} attempts{RESET}"
            )
        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        length: int = len(name)
        if length < 3:
            return False
        return name.replace(" ", "").isalpha()

    GREEN = "\033[92m"
    RESET: str = "\033[0m"

    @power_validator(10)
    def cast_spell(self: Any, spell_name: str, power: int) -> str:
        return f"{GREEN}Successfully cast "
        f"{spell_name} with {power} power{RESET}"


if __name__ == "__main__":
    RESET: str = "\033[0m"
    RED: str = "\033[31m"
    PURPLE: str = "\033[38;2;229;208;255m"
    GREEN = "\033[92m"

    @spell_timer
    def firball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    print(f"{PURPLE}Testing spell timer...{RESET}")
    result = firball()
    print(f"Result: {result}")
    print(f"\n{PURPLE}Testing retrying spell...{RESET}")

    @retry_spell(3)
    def unstable_spell() -> None:
        raise Exception("spell unstable")

    print(unstable_spell())
    print("Waaaaaaagh spelled !")

    print(f"\n{PURPLE}Testing MageGuild...{RESET}")
    obj = MageGuild()
    print(MageGuild.validate_mage_name("Alix"))
    print(MageGuild.validate_mage_name("Al"))
    print(obj.cast_spell("Lightning", 15))
    print(obj.cast_spell("Lightning", 5))
    print(f"\n{PURPLE}Testing Power validator...{RESET}")

    @power_validator(10)
    def valid(power: int) -> str:
        return "its valid"
    print(valid(17))
    print(valid(5))
