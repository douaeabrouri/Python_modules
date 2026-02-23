#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    Plants = [
        Plant("Rose", 25, 30),
        Plant("OaK", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]
print("=== Plant Factory Output ===")
for i in Plants:
    print(f"Created: {i.name} ({i.height}cm, {i.age} days)")
print("\n")
print(f"Total plants created: {len(Plants)}")
