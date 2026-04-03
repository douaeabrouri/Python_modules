from battle import Creature
from capabilities import TransformCapability


class Shiftling(Creature, TransformCapability): 
    def __init__(self) -> None:
        self.name = "Shiftling"
        self.type = "Normal"
    def attack(self) -> str:
        if self.is_transformed:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."
    
    def transform(self) -> str:
        self.is_transformed = True
        return "Shiftling shifts into a sharper form!"
    
    def revert(self) -> str:
        self.is_transformed = False
        return "Shiftling returns to normal."

class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
       self.name = "Morphagon"
       self.type = "Normal/Dragon"
    
    def attack(self) -> str:
        if self.is_transformed:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."
    
    def transform(self) -> str:
        self.is_transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_transformed = False
        return "Morphagon stabilizes its form."