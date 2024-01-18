#un item c'est quoi ? alors c'est d'office un truc qu'on peut soit equiper/consommer/vendre/abancer), breff c'est tout des truc que le player peut faire avec un item

ARMOR = 'armor'
CONSUMABLE = 'consumable'
WEAPON = 'weapon'

class Item():
    def __init__(self, name="item", description="item", item_type="item", weight=0, availability=True, required_level=0, value=0): #""",statistics"""
        self.name = name #son nom
        self.description = description # trouver dans la rue
        self.item_type = item_type #ARMOR ou CONSUMABLE ou WEAPON , mais ici on est a la base des bases, du coup juste 'item'
        self.weight = weight #poid du bazar
        self.availability = availability #si on peut l'utiliser 
        self.required_level = required_level # le niveau requis
        self.value = value # son prix , trop envie de faire hotel des ventes :3
        #self.statistics = statistics pas encore !
        
    #juste spécifie comment l'afficher 
    def __str__(self) -> str:
        return f"Name: {self.name} | Type: {self.item_type} | Description: {self.description} | Weight: {self.weight} | Availability: {self.availability} | Required Level: {self.required_level} | Value: {self.value}"
    

    
