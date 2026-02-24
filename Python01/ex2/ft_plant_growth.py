#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1

    def age_(self) -> None:
        self.age += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
print("=== Day 1 ===")
rose.get_info()
count = 0
for day in range(6):
    count += 1
    rose.grow()
    rose.age_()
print("=== day 7 ===")
rose.get_info()
print(f"Growth this week: +{count}cm")
