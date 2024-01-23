import unittest
from model.classes.item.inventory import *

class TestInventory(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory()
        self.item1 = Item(name="Sword", description="Sharp and shiny", item_type="weapon", weight=5, availability=True, required_level=3, value=50)
        self.item2 = Item(name="Potion", description="Heals wounds", item_type="consumable", weight=1, availability=True, required_level=1, value=10)

    def test_add_item(self):
        self.inventory.add_item(self.item1)
        self.assertIn(self.item1.uid, self.inventory.get_all_item())

    def test_add_item_inventory_full(self):
        # Remplir l'inventaire avec des éléments jusqu'à la limite
        for i in range(DEFAULT_MAX_SIZE):
            item = Item(name=f"Item{i}", description=f"Description{i}")
            self.inventory.add_item(item)

        # Essayer d'ajouter un autre élément doit lever une exception
        with self.assertRaises(Exception):
            self.inventory.add_item(self.item1)

    def test_get_item(self):
        self.inventory.add_item(self.item1)
        retrieved_item = self.inventory.get_item(self.item1.uid)
        self.assertEqual(retrieved_item, self.item1)

    def test_get_item_not_found(self):
        # Essayer de récupérer un élément non présent doit lever une exception
        with self.assertRaises(Exception):
            self.inventory.get_item("non_existent_uid")

    def test_remove_item(self):
        self.inventory.add_item(self.item1)
        self.inventory.remove_item(self.item1.uid)
        self.assertNotIn(self.item1.uid, self.inventory.get_all_item())

   
    def test_remove_item_not_found(self):
        """Test the get_pull_request_ready_branch from the internal API
        on the main repository
        """
        # Essayer de supprimer un élément non présent doit lever une exception
        with self.assertRaises(Exception):
            self.inventory.remove_item("non_existent_uid")


if __name__ == '__main__':
    unittest.main()