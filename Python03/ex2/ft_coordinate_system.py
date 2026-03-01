#!/usr/bin/env python3

import math


def calculate_distance(p1: tuple, p2: tuple) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def create_position(x: int, y: int, z: int) -> tuple:
    p: tuple = (x, y, z)
    return p


def parse_coordinates(coord_string: str) -> tuple:
    try:
        parts: tuple = coord_string.split(",")
        x: int = int(parts[0])
        y: int = int(parts[1])
        z: int = int(parts[2])
        return (x, y, z)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")


if __name__ == "__main__":
    print("=== Game Coordinate System ==\n")

    tp1: tuple = create_position(10, 20, 5)
    tp2: tuple = create_position(0, 0, 0)
    print(f"Position created: {tp1}")
    print(f"Distance between {tp2} and {tp1}:"
          f" {round(calculate_distance(tp1, tp2), 2)}")
    print()
    s: str = "3,4,0"
    tp3: tuple = parse_coordinates(s)
    print(f'Parsing coordinates: "{s}"')
    print(f"Parsed position: {tp3}")
    print(f"Distance between {tp2} and {tp3}: {calculate_distance(tp2, tp3)}")
    print()
    s1: str = "abc,def,ghi"
    tp4: tuple = parse_coordinates(s1)
    print()
    print("Unpacking demonstration:")
    print(f"Player at x={tp3[0]}, y={tp3[1]}, z={tp3[2]}")
    print(f"Coordinates: x={tp3[0]}, y={tp3[1]}, z={tp3[2]}")
