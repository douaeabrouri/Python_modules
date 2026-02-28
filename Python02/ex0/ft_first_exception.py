#!/usr/bin/env python3


def check_temperature(temp_str: str) -> int:
    """Validate a temperature string and return it if in range (0-40)."""
    try:
        x2: int = int(temp_str)
        if x2 < 0:
            print(f"Error: {x2}°C is too cold for plants (min 0°C)")
        elif x2 > 40:
            print(f"Error: {x2}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {x2}°C is perfect for plants!")
            return x2
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    """Test check_temperature with valid, invalid, and extreme inputs."""
    print("=== Garden Temperature Checker ===\n")
    print("Testing temperature: 25")
    check_temperature("25")
    print()
    print("Testing temperature: abc")
    check_temperature("abc")
    print()
    print("Testing temperature: 100")
    check_temperature("100")
    print()
    print("Testing temperature: -50")
    check_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
