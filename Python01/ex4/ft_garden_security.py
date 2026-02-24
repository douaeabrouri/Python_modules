#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str) -> None:
        self.name = name
        self.height = 0
        self.age = 0

    def set_height(self, value: int) -> None:
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"Invalid operation attempted: age {value} [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.age = value
            print(f"Age updated: {value} days [OK]")

    def get_height(self) -> int:
        return self.height

    def get_age(self) -> int:
        return self.age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    Plant = SecurePlant("Rose")
    print(f"Plant created: {Plant.name}")
    Plant.set_height(25)
    Plant.set_age(30)
    print("")
    Plant.set_height(-5)
    print("")
    print(f"Current plant: {Plant.name} ({Plant.height}cm, {Plant.age} days)")
