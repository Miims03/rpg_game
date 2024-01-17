from item import Item, WEAPON

class Weapon(Item):
    def __init__(self, name="weapon", description="Weapon with attack stat", item_type=WEAPON, weight=1, required_level=1, value=0):
        super().__init__(name, description, item_type, weight, required_level, value)
        self.attack = 0
        
    def __str__(self) -> str:
        str = super().__str__()
        str+=f" | attack:{self.attack}"
        return str