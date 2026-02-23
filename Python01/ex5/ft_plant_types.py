#!/usr/bin/env python3

import math

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int,
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade = int(math.pi * (self.trunk_diameter / 2)) 
        print(
            f"{self.name} provides {shade} "
            f"square meters of shade"
            )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_nutrition(self):
        print(f"{self.name} is rich in Vitamin {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("")
    flower = Flower("Rose", 25, 30, "Red")
    tree = Tree("Oak", 500, 1825, 50)
    vegetable = Vegetable("Tomato", 80, 90, "summer", "C")
    print(
        f"{flower.name} (Flower): {flower.height}cm, "
        f"{flower.age} days, {flower.color} color"
        )
    flower.bloom()
    print("")
    print(
        f"{tree.name} (Tree): {tree.height}cm, {tree.age} days,  "
        f"{tree.trunk_diameter}cm diameter"
        )
    tree.produce_shade()
    print("")
    print(
        f"{vegetable.name} (Vegetable): {vegetable.height}cm, "
        f"{vegetable.age} days, {vegetable.harvest_season} harvest"
        )
    vegetable.show_nutrition()
