#!/usr/bin/env python3

# class student:
# 	def __init__(self, name:str, age:int, level:str) -> None:
# 		self.name = name
# 		self.age = age
# 		self.level = level
# 	def introduce(self) -> None:
# 		print(f"Hi, my name is {self.name}, I am {self.age} years old, level {self.level}.")

# if __name__ == "__main__":
# 	students = student("douae", 20, "python01")
# 	students.introduce()

# exercice2
# class Plant:
# 	kingdom = "plante"

# 	def __init__(self, name:str, height: int) -> None:
# 		self.name = name
# 		self.height = height
# 	def grow(self, grew:int) -> None:
# 			self.height += grew
	
# if __name__ == "__main__":
# 	p1 = Plant("Rose", 10)
# 	p2 = Plant("Tree", 100)
# 	p1.kingdom = "change"

# 	p1.grow(5)

# 	print(p1.kingdom)   # 15
# 	print(p2.kingdom)   # 100
# 	print(Plant.kingdom)

# exercice 3

# class Animal:
#     def __init__(self, name: str) -> None:
#         self.name = name

#     def speak(self):
#         print("Animal makes a sound")


# class Dog(Animal):
#     def __init__(self, name: str, breed: str) -> None:
#         super().__init__(name)
#         self.breed = breed

#     def speak(self):
#         print("WOOF")


# if __name__ == "__main__":
#     d = Dog("Rex", "husky")

#     print(d.name)
#     print(d.breed)

# exercice 5
    
class BankAccount:
	bank_name = "1337 Bank"
	def __init__(self, owner: str, balance: str) -> None:
		self.owner = owner

	@staticmethod
	def deposit(amount:int) -> None:
		