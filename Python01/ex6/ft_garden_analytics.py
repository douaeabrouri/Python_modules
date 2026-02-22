#!usr/bin/evn python3 

class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height
    def grew(self) -> None:
        self.height += 1
        print(f"{self.name} grew {self.height}")
    def get_info(self):
        return f"{self.name}: {self.height}cm"

class FloweringPlant(Plant):
    def __init__(self,  name: str, height: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = True
        def get_info(self) -> None:
            status = "blooming" if is.blooming else "not blooming"
            print(f"{self.nam}: {self.height}cm, {self.color} flowers ({status})")
class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        super().__init__(name, height, age)
        self.prize = prize
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Prize points: {self.prize}"
        
class GardenManager():
    Total_gardens_managed = 0
    class GardenStats():
        def __init__(self, Plants: list) -> None:
            self.Plants = Plants
        def Total_plants(self) -> int:
            return len(Plants)
        def Total_growth(self) -> None:
            total = 0
            for plant in self.Plants:
                total += self.Plants
                return total
        def count_types(self) -> None:
            self.count_types = 0
            return count_types += 1
        def get_repot(self) -> None:
            repot = GrandenManager().GardenStats(self.plants)
            repot.Total_growth()
            repot.Total_plants()

@classmethod
class create_garden_network(cls) -> None:
        cls.total_garden = total_garden
        print(f"Total garden managed: {cls.total_garden}")

@staticmethod
class validate_height(height) -> bool:
    validate = "True" if height >= 0 else "False"
   return f"Height validation test: {validate}"

if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    Plant("Oak Tree", 101)
    print(f"Added {Plant.name} to Alice's garden")
    Plant("Rose", 26, "red")
    print(f"Added {Plant.name} to Alice's garden")
    Plant("Sunflower", 51, "yellow")
    print(f"Added {Plant.name} to Alice's garden")
    print("")
    print("Alice is helping all plants grow...")
    for plant in Plants:
        print(f"{Plant.name} grew 1cm")
    print("=== Alice's Garden Report ===")
    print("Plants in garden:")
    print(f"- {plant}")
