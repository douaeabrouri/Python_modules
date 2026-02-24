#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color
        self.is_blooming = True

    def get_info(self) -> str:
        status = "blooming" if self.is_blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({status})"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        super().__init__(name, height, color)
        self.prize = prize

    def get_info(self) -> str:
        base = super().get_info()
        return f"{base}, Prize points: {self.prize}"


class GardenManager:
    total_gardens = 0

    class GardenStats:
        def __init__(self, plants: list) -> None:
            self.plants = plants

        def total_plants(self) -> int:
            return len(self.plants)

        def total_growth(self) -> int:
            return len(self.plants)

        def count_types(self) -> tuple:
            regular = 0
            flowering = 0
            prize = 0

            for plant in self.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1

            return regular, flowering, prize

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant) -> None:
        self.plants.append(plant)
        if self.owner == "Alice":
            print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        if self.owner == "Alice":
            print(f"{self.owner} is helping all plants grow...")
            for plant in self.plants:
                plant.grow()
        else:
            # Grow silently for Bob
            for plant in self.plants:
                plant.height += 1

    def get_report(self) -> None:
        stats = GardenManager.GardenStats(self.plants)
        regular, flowering, prize = stats.count_types()

        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")

        for plant in self.plants:
            print(f"- {plant.get_info()}")

        print(
            f"\nPlants added: {stats.total_plants()}, "
            "Total growth: {stats.total_growth()}cm"
            )
        print(
            f"Plant types: {regular} regular, "
            "{flowering} flowering, {prize} prize flowers"
            )

    def get_score(self) -> int:
        score = 0
        for plant in self.plants:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.prize * 4
        return score

    @classmethod
    def create_garden_network(cls) -> None:
        print(f"Total gardens managed: {cls.total_gardens}")

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print("")
    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    bob.add_plant(Plant("Cactus", 50))
    bob.add_plant(Plant("Fern", 40))

    print()
    alice.grow_all()
    bob.grow_all()

    alice.get_report()

    print(f"\nHeight validation test: {GardenManager.validate_height(10)}")

    alice_score = alice.get_score()
    bob_score = bob.get_score()

    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")

    GardenManager.create_garden_network()
