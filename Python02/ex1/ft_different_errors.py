#!/usr/bin/env python3


def garden_operations() -> None:

    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("\nTesting ZeroDivisionError...")
    try:
        divisor: int = 0
        print(f"{10/divisor}")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("\nTesting FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("\nTesting KeyError...")
    try:
        dict = {"x": "abc", "x2": 1, "x3": 5}
        s: str = "missing_plant"
        data = dict[s]
        print(f"{data}")
    except KeyError:
        print(f"Caught KeyError: '{s}'\n")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")

    garden_operations()

    print("Testing multiple errors together...")
    try:
        int("abc")
        10 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")
