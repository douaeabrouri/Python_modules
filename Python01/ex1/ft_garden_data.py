#!/usr/bin/env python3

class Plant:
	def __init__(self, name: str, Height: int, Age: int)->None:
		self.name = name
		self.Height = Height
		self.Age = Age

if __name__ == "__main__":
	Plants = [
		Plant("Rose", 25, 30),
		Plant("Sunflower", 80, 45),
		Plant("Cactus", 15, 120),
	]
	print("=== Garden Plant Registry ===")
	for Plant in Plants:
		print(f"{Plant.name}: {Plant.Height}cm, {Plant.Age} days old")