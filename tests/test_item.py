import unittest
import sys
import os

# # Ajouter le répertoire racine du projet au chemin de recherche des modules
# current_dir = os.path.dirname(os.path.abspath(__file__))
# project_root = os.path.abspath(os.path.join(current_dir, ".."))
# sys.path.insert(0, project_root)

# Importer le module nécessaire
from model.classes.item.item import *

class TestItem(unittest.TestCase):

    def setUp(self):
        # Initialisation des objets pour les tests
        self.item1 = Item(name="Sword", description="Sharp and shiny", item_type=ItemType.WEAPON, weight=5, availability=True, required_level=3, value=50)
        self.item2 = Item(name="Potion", description="Heals wounds", item_type=ItemType.CONSUMABLE, weight=1, availability=True, required_level=1, value=10)
        self.item3 = Item(name="Shield", description="Protects against attacks", item_type=ItemType.ARMOR, weight=8, availability=True, required_level=5, value=80)


    def test_default_values(self):
        default_item = Item()
        self.assertEqual(default_item.name, "item")
        self.assertEqual(default_item.description, "item")
        self.assertEqual(default_item.item_type,ItemType.ITEM)
        self.assertEqual(default_item.weight, 0)
        self.assertEqual(default_item.availability, True)
        self.assertEqual(default_item.required_level, 0)
        self.assertEqual(default_item.value, 0)

    def test_uid_generation(self):
        self.assertIsNotNone(self.item1.uid)
        self.assertIsNotNone(self.item2.uid)
        self.assertIsNotNone(self.item3.uid)
        self.assertNotEqual(self.item1.uid, self.item2.uid)
        self.assertNotEqual(self.item1.uid, self.item3.uid)
        self.assertNotEqual(self.item2.uid, self.item3.uid)

if __name__ == '__main__':
    unittest.main()
