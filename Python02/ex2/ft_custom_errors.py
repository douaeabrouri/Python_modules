#!/usr/bin/env python3

""" this class just inherits everything fron exception without adding anything new!"""
class GardenError(Exception):
	def __init__(self, message: str = "A garden Error"):
		super().__init__(message)

class PlantError(GardenError):
	def __init__(self, message: str = "A Plant error"):
		super().__init__(message)

class WaterError(GardenError):
	def __init__(self, message: str = "A Water error"):
		super().__init__(message)


def test_plant_error() -> None:
    print("Testing PlantError...")
    try:
       raise PlantError("the tomato plant is wilting")
    except PlantError as e:
       print(f"caught PlantError: {e}\n")

def test_water_error() -> None:
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

def test_all_garden_errors() -> None:
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_plant_error()
    print()
    test_water_error()
    print()
    test_all_garden_errors()
    print()
    print("All custom error types work correctly!")
