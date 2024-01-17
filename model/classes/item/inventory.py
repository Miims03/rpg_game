from item import *
from consumables.consumable import Consumable
from weapons.weapon import Weapon
from armors.armor import Armor
class Inventory():
    
    def __init__(self):
        self.armors = [Armor]
        self.consumables = [Consumable]
        self.weapons = [Weapon]

    def add_mult_item(self,list):
        for item in list : 
            self.add_item(item)
        pass

    def add_item(self, item : 'Item'):
        if item.item_type == ARMOR:
            self.armors.append(item)
        elif item.item_type == CONSUMABLE:
            self.consumables.append(item)
        elif item.item_type == WEAPON:
            self.weapons.append(item)
        else:
            print(f"Unsupported item type: {item.item_type}. Item not added to the inventory.")

    def remove_item(self, item : 'Item'):
        if item.item_type == ARMOR and item in self.armors:
            self.armors.remove(item)
            print(f"{item.name} removed from the armor inventory.")
        elif item.item_type == CONSUMABLE and item in self.consumables:
            self.consumables.remove(item)
            print(f"{item.name} removed from the consumable inventory.")
        elif item.item_type == WEAPON and item in self.weapons:
            self.weapons.remove(item)
            print(f"{item.name} removed from the weapon inventory.")
        else:
            print(f"{item.name} not found in the inventory.")

    def display_inventory(self):
        print("Armor Inventory:")
        for item in self.armors:
            print(item)

        print("Consumable Inventory:")
        for item in self.consumables:
            print(item)

        print("Weapon Inventory:")
        for item in self.weapons:
            print(item)
        
def test():
    i = Inventory()
    itema = Item(name="Plaque Fer",description="Une plaque en Fer classique",item_type=ARMOR)
    itemab = Item(name="Epee Fer",description="Une Epee en Fer assez classique",item_type=WEAPON)
    itemabc = Item(name="Potion rich en Fer",description="Une potion pour les os fragiles",item_type=CONSUMABLE)
    i.add_mult_item({itema,itemab,itemabc})
    i.display_inventory()

test()