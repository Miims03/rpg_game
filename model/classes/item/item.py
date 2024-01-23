#lib pour généré des id uniques
import uuid
#Abstract lib 
from abc import ABC , abstractmethod
#lib pour enumeration : a faire si constant
from enum import Enum

class ItemType(Enum):
    ITEM = 0,
    ARMOR = 1,
    CONSUMABLE =2,
    WEAPON =3

class Item(ABC):
    def __init__(self, name="item", description="item", item_type=ItemType.ITEM, weight=0, availability=True, required_level=0, value=0):
        # Utilisation de uuid4 pour générer un identifiant unique
        self.uid = str(uuid.uuid4())
        self.name = name #son nom
        self.description = description # trouver dans la rue
        self.item_type = item_type #ARMOR ou CONSUMABLE ou WEAPON , mais ici on est a la base des bases, du coup juste 'item'
        self.weight = weight #poid du bazar
        self.availability = availability #si on peut l'utiliser 
        self.required_level = required_level # le niveau requis
        self.value = value # son prix , trop envie de faire hotel des ventes :3
        #self.statistics = statistics pas encore !
        
    #spécifie comment l'afficher 
    def __str__(self):
        return f"Name: {self.name} | Type: {self.item_type} | Description: {self.description} | Weight: {self.weight} | Availability: {self.availability} | Required Level: {self.required_level} | Value: {self.value}"
    
    #@abstractmethod
    def use(self):
        ...
    
