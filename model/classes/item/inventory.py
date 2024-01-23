from model.classes.item.item import *

DEFAULT_MAX_SIZE = 20


class Inventory():
    
    def __init__(self):
        self.items : dict[:Item] = {}
        self.size_max =20

    def add_item(self, item: Item):
        # Ajoute un item à l'inventaire avec un ID unique
        if len(self.items)<self.size_max:
            self.items[item.uid] = item
        else:
            raise Exception("Inventory is Full.")

    def get_item(self, item_id):
        # Recupère un item de l'inventaire en utilisant son ID
        if self.items[item_id]:
            return self.items[item_id]
        else:
            raise Exception(f"L'item avec l'UID {item_id} n'est pas dans l'inventaire.")
        
    def get_all_item(self):
        return self.items

    def remove_item(self, item_id):
        # Retire un item de l'inventaire en utilisant son ID
        if self.items[item_id]:
            del self.items[item_id]
        else:
            raise Exception(f"L'item avec l'UID {item_id} n'est pas dans l'inventaire.")

    def display_inventory(self):
        # Affiche le contenu de l'inventaire avec les ID
        print("Inventaire:")
        for item_id, item in self.items.items():
            print(f"uID {item_id}: {item}")
        
# def test():
#     i = Inventory()
#     itema = Item(name="Plaque Fer",description="Une plaque en Fer classique",item_type=ARMOR)
#     itemab = Item(name="Epee Fer",description="Une Epee en Fer assez classique",item_type=WEAPON)
#     itemabc = Item(name="Potion rich en Fer",description="Une potion pour les os fragiles",item_type=CONSUMABLE)
#     i.add_item(itema)
#     i.add_item(itemab)
#     i.add_item(itemabc)
#     i.display_inventory()
#     return i

#test()