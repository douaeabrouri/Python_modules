#!/usr/bin/env python3

from ex0.flame_factory import FlameFactory
from ex0.aqua_factory import AquaFactory

def test_factory(factory):
    print("Testing factory")

    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())	

def battle(factory1, factory2):
    print("Testing battle")

    c1 = factory1.create_base()
    c2 = factory2.create_base()

    print(c1.describe())
    print("vs.\n")
    print(c2.describe())
    print("fight!\n")

    print(c1.attack())
    print(c2.attack())

if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    
    test_factory(flame_factory)
    print()
    test_factory(aqua_factory)
    print()
    battle(flame_factory, aqua_factory)
    