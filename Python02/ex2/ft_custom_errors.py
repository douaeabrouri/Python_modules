#!/usr/bin/env python3


class GardenError(Exception):
    """Base exception for all garden-related problems."""
    def __init__(self, message: str = "A garden Error"):
        super().__init__(message)


class PlantError(GardenError):
    """Exception raised for problems with individual plants."""
    def __init__(self, message: str = "A Plant error"):
        super().__init__(message)


class WaterError(GardenError):
    """Exception raised for problems with the watering system."""
    def __init__(self, message: str = "A Water error"):
        super().__init__(message)


def test_plant_error() -> None:
    """Raise and catch a PlantError."""
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"caught PlantError: {e}")


def test_water_error() -> None:
    """Raise and catch a WaterError."""
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_all_garden_errors() -> None:
    """Show that GardenError catches all garden-specific errors."""
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")


def test() -> None:
    """Run all custom exception demonstrations."""
    print("=== Custom Garden Errors Demo ===\n")
    test_plant_error()
    print()
    test_water_error()
    print()
    test_all_garden_errors()
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test()
