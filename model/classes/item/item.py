#un item c'est quoi ? alors c'est d'office un truc qu'on peut soit equiper/consommer/vendre/abancer), breff c'est tout des truc que le player peut faire avec un item

ARMOR = 'armor'
CONSUMABLE = 'consumable'
WEAPON = 'weapon'

class Item():
    def __init__(self, name="item", description="item", item_type="item", weight=0, availability=True, required_level=0, value=0): #""",statistics"""
        self.name = name
        self.description = description
        self.item_type = item_type
        self.weight = weight
        self.availability = availability
        self.required_level = required_level
        self.value = value
        #self.statistics = statistics
    def __str__(self) -> str:
        return f"Name: {self.name} | Type: {self.item_type} | Description: {self.description} | Weight: {self.weight} | Availability: {self.availability} | Required Level: {self.required_level} | Value: {self.value}"
    

    
