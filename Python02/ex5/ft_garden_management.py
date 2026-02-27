#!/usr/bin/env python3


class GardenError(Exception):
    def __init__(self, message: str = "A garden error occurred"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "A plant error occurred"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "A water error occurred"):
        super().__init__(message)


class GardenManager:
    def __init__(self) -> None:
        self.plants: list = []

    def add_plants(self, plant_name: str) -> None:
        try:
            if not plant_name:
                raise PlantError("Plant name cannot be empty!")
            self.plants.append(plant_name)
            print(f"Added {plant_name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(
        self, plant_name: str, water_level: int, sunlight_hours: int
    ) -> None:
        try:
            if water_level > 10:
                raise WaterError(f"Water level {water_level}"
                                 f" is too high (max 10)")
            elif water_level < 1:
                raise WaterError(f"Water level {water_level}"
                                 f" is too low (min 0)")
            else:
                print(
                    f"{plant_name}: healthy (water: {water_level},"
                    f" sun: {sunlight_hours})"
                )
        except WaterError as e:
            print(f"Error checking {plant_name}: {e}")


def test_garden_management() -> None:
    manager = GardenManager()
    print("=== Garden Management System ===")
    print()
    print("Adding plants to garden...")
    manager.add_plants("tomato")
    manager.add_plants("lettuce")
    manager.add_plants("")
    print()
    print("Watering plants...")
    manager.water_plants()
    print()
    print("Checking plant health...")
    manager.check_plant_health("tomato", 5, 8)
    manager.check_plant_health("lettuce", 15, 8)
    print()
    print("Testing error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"caught GardenError: {e}")
        print("System recovered and continuing...\n")

    print("Garden management system test complete!")
