#!/usr/bin/env python3


def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise TypeError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except TypeError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    plant_list: list = ["tomato", "lettuce", "carrots"]
    water_plants(plant_list)
    print("Watering completed successfully!\n")
    print("Testing with error...")
    plant_list: list = ["tomato", None]
    water_plants(plant_list)
    print()
    print("Cleanup always happens, even with errors!")
