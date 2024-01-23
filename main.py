from controller.controller import Controller
from PySide6.QtWidgets import QWidget, QApplication
from view.inventory_view import InventoryView
from model.classes.item.inventory import Inventory
from model.classes.item.item import *
#main.py

def main():
   controller = Controller()
   #controller.start()
   controller.start2()
   
if __name__ == "__main__":
   main()


# def test():
#     i = Inventory()
#     itema = Item(name="Plaque Fer",description="Une plaque en Fer classique",item_type=ARMOR)
#     itemab = Item(name="Epee Fer",description="Une Epee en Fer assez classique",item_type=WEAPON)
#     itemabc = Item(name="Potion rich en Fer",description="Une potion pour les os fragiles",item_type=CONSUMABLE)
#     i.add_item(itema)
#     i.add_item(itemab)
#     i.add_item(itemabc)
#     return i

# if __name__ == '__main__':
#     app = QApplication()

#     # Créer une instance de CellView avec le type de votre choix
#     # Créer un widget principal pour contenir le layout
#     #main_widget = QWidget()
#     #main_widget.setAcceptDrops(True)
#     i=test()
#     inventory_widget = InventoryView(i)
#     #main_widget.setLayout(inventory_widget)
#     #main_widget.setWindowTitle('Test de InventoryView')

#     # Afficher la fenêtre
#     #main_widget.show()
#     inventory_widget.show()

#     # Lancer l'application
#     exit(app.exec())

# Miims = Player('Miims')
# Miims.get_lvl()
# Miims = Miims.changeClassWarrior()
# # Miims.get_armor()
# # Miims2 = Player('Miims 33')
# # Miims.give_armor(Miims2)
# # Miims.get_armor()
# Mob = Monster()
# Mob.Attack(Miims)
# Mob.Attack(Miims)
# Mob.Attack(Miims)
# print(f"\nBienvenue {Miims.role}\n{Miims.name} Lvl {Miims.lvl}\nPv : {Miims.pv}\nMana : {Miims.mana}\nEndurance : {Miims.stamina}\nAttaque : {Miims.attack}\nNombre de d'armures : {Miims.numArmors}\nArmures : {Miims.armors}\n")

# print(f"\nBienvenue {Miims2.role}\n{Miims2.name} Lvl {Miims2.lvl}\nPv : {Miims2.pv}\nMana : {Miims2.mana}\nEndurance : {Miims2.stamina}\nAttaque : {Miims2.attack}\nNombre de d'armures : {Miims2.numArmors}\nArmures : {Miims2.armors}\n")

# Miims.get_lvl()
# Miims = Miims.changeClassHealer()

# print(Miims.heal in globals())

# if Miims.heal in locals() or Miims.heal in globals():
#     print(f"\nBienvenue {Miims.role}\n{Miims.name} Lvl {Miims.lvl}\nPv : {Miims.pv}\nMana : {Miims.mana}\nEndurance : {Miims.stamina}\nAttaque : {Miims.attack}\nNombre de d'armures : {Miims.numArmors}\nArmures : {Miims.armors}Heal = {Miims.heal}")
# else:
#     print(f"\nBienvenue {Miims.role}\n{Miims.name} Lvl {Miims.lvl}\nPv : {Miims.pv}\nMana : {Miims.mana}\nEndurance : {Miims.stamina}\nAttaque : {Miims.attack}\nNombre de d'armures : {Miims.numArmors}\nArmures : {Miims.armors}\n")

# Mob = Monster()
# Mob.Attack(Miims)



# print(f"\nBienvenue {Miims.role}\n{Miims.name} Lvl {Miims.lvl}\nPv : {Miims.pv}\nEndurance : {Miims.stamina}\nAttaque Magique : {Miims.magic_attack}\nNombre de d'armures : {Miims.numArmors}\nArmures : {Miims.armors}")
# print(Miims.numArmors)
# for shield in Miims.armors:
#     print(shield)
# print(f'\nBienvenue {Miims.role}\n{Miims.name} Lvl {Miims.lvl}\nPv : {Miims.pv}\nEndurance : {Miims.stamina}\nAttaque : {Miims.attack}\n')


# Miims.get_lvl()
# Miims = Miims.changeClassHealer()

# print(f'\nBienvenue {Miims.role}\n{Miims.name} Lvl {Miims.lvl}\nPv : {Miims.pv}\nMana : {Miims.mana}\nAttaque Magique : {Miims.magic_attack}\n')

# Mob1 = Monster()
# Miims.Attack(Mob1)
# Miims.MagicAttack(Mob1)
    
# print(f'\nBienvenue {Miims.role}\n{Miims.name} Lvl {Miims.lvl}\nPv : {Miims.pv}\nEndurance : {Miims.stamina}\nAttaque : {Miims.attack}\n')

# print(f'\nBienvenue {Miims.name}\nLvl : {Miims.lvl}\nPv : {Miims.pv}\nMana : {Miims.mana}\nEndurance : {Miims.stamina}\nAttaque : {Miims.attack}\nAttaque Magique : {Miims.magic_attack}\nHeal : {Miims.heal}\n')

# print(f'\nMob 1 :\nPv : {Mob1.pv}\nMana : {Mob1.mana}\nEndurance : {Mob1.stamina}\n')
    
