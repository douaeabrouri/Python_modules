#!/usr/bin/env python3

def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int) -> None:

    try:
        if not plant_name:
          raise ValueError("Plant name cannot be empty!")
    except ValueError as e:
       print(f"Error: {e}")
       return
    
    try:
        if water_level > 10:
           raise ValueError(f"Water level {water_level} is too high (max 10)")
        elif water_level < 1:
           raise ValueError(f"Water level {water_level} is too low (min 0)")
    except ValueError as e:
       print(f"Error: {e}")
       return
    try:
        if sunlight_hours < 2:
          raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
        elif sunlight_hours > 12:
           raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max 12)")
    except ValueError as e:
       print(f"Error: {e}")
       return
       
    if plant_name != None and (water_level >= 0 and water_level <= 10) and (sunlight_hours >= 2 and sunlight_hours <= 12):
       print(f"Plant '{plant_name}' is healthy!")

def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    check_plant_health("tomato", 5, 3)
    print()
    print("Testing empty plant name...")
    check_plant_health(None, 3, 7)
    print()
    print("Testing bad water level...")
    check_plant_health("tomato", -5, 3)
    print()
    print("Testing bad sunlight hours...")
    check_plant_health("tomato", 4, 1)
    print()
    print("All error raising tests completed!")
    
test_plant_checks()