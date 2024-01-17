from item import Item, CONSUMABLE

class Consumable(Item):
    
    def __init__(self, name="consomable", description="consomable with attack/heal stat", item_type=CONSUMABLE, weight=1, required_level=1, value=0):
        super().__init__(name, description, item_type, weight, required_level, value)
        self.attack = 0
        self.heal = 0