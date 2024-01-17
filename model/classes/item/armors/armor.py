from item import Item, ARMOR

class Armor(Item):
    
    def __init__(self, name="consomable", description="consomable with attack/heal stat", item_type=ARMOR, weight=1, required_level=1, value=0):
        super().__init__(name, description, item_type, weight, required_level, value)
        self.armor = 0
        