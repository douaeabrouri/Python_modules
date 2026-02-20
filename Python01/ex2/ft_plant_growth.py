#!/usr/bin/env Python3

class Plant:
	def __init__(self, name: str, Height: int, Age: int) ->None:
		self.name = name
		self.Height = Height
		self.Age = Age
	def grow(self) -> None:
		self.Height += 1
	def age(self) -> None:
		self.Age += 1
	def get_info(self) -> None:
		print(f"{self.name}: {self.Height}cm, {self.Age} days old")

if __name__ == "__main__":
	rose = Plant("Rose", 25, 30)
print("=== Day 1 ===")
rose.get_info()
for day in range(7):
	rose.grow()
	rose.age()
print("=== day 7 ===")
rose.get_info()