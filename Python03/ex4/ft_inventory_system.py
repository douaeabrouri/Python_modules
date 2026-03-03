#!/usr/bin/env python3

import sys


def get_value(item: tuple) -> int:
    return item[1]


if __name__ == "__main__":
    try:
        if len(sys.argv) >= 1:
            inventory: dict = {}
            for arg in sys.argv[1:]:
                parts: list = arg.split(":")
                key: str = parts[0]
                value: int = int(parts[1])
                inventory[key] = value
            total_items: int = sum(inventory.values())
            unique_item: int = len(inventory.values())
            sorted_inventory: dict = sorted(
                inventory.items(), key=get_value, reverse=True
            )
            max: tuple = max(inventory.items(), key=get_value)
            min: tuple = min(inventory.items(), key=get_value)
            print("=== Inventory System Analysis ===")
            print(f"Total items in inventory: {total_items}")
            print(f"Unique item types: {unique_item}")
            print()
            print("=== Current Inventory ===")
            for key, value in sorted_inventory:
                va_units: str = "unit" if value == 1 else "units"
                persentage: float = (value / total_items) * 100
                print(f"{key}: {value} {va_units} ({persentage:.1f}%)")
            most_unit = "unit" if max[1] == 1 else "units"
            least_unit = "unit" if min[1] == 1 else "units"
            print()
            print("=== Inventory Statistics ===")
            print(f"Most abundant: {max[0]} ({max[1]} {most_unit})")
            print(f"Least abundant: {min[0]} ({min[1]} {least_unit})")
            print()
            moderate: dict = {}
            scarce: dict = {}
            restock: list = []
            print("=== Item Categories ===")
            for key, value in inventory.items():
                if value >= 4:
                    moderate[key] = value
                else:
                    scarce[key] = value
            print(f"moderate: {moderate}")
            print(f"scarce: {scarce}")
            print()
            print("=== Management Suggestions ===")
            for key, value in inventory.items():
                if value == 1:
                    restock.append(key)
            key_str: str = ""
            for key in restock:
                if key_str == "":
                    key_str += key
                else:
                    key_str += ", " + key
            print(f"restock needed: {key_str}")
            print()
            print("=== Dictionary Properties Demo ===")
            keys_str2: str = ""
            for key in inventory.keys():
                if keys_str2 == "":
                    keys_str2 += key
                else:
                    keys_str2 += ", " + key
            key_str3: str = ""
            for value in inventory.values():
                if key_str3 == "":
                    key_str3 += str(value)
                else:
                    key_str3 += ", " + str(value)
            print(f"Dictionary keys: {keys_str2}")
            print(f"Dictionary values: {key_str3}")
            result: bool = "sword" in inventory
            print(f"Sample lookup - 'sword' in inventory: {result}")
    except Exception as e:
        print(f"ERROR : {e}")
