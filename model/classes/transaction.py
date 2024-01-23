from model.classes.player.player import Player
from model.classes.item.item import Item

class Transaction():
    
    def __init__(self, vendeur : Player , achteur : Player, item : Item,value = 0):
        
        self.vendeur = vendeur
        self.achteur = achteur
        self.item_a_vendre = item
        self.valeur = value
        
        
    def check_is_full(self):
        #regarde si l'achteur a la place pour l'item dans son inventaire, sinon transaction abandonnée
        pass
    
    def check_item_owner(self):
        #regarde si c'est bien dans l'inventaire du vendeur et que ça appartient bien a lui 
        pass
    
    
    def check_balance(self):
        #regarde si la valeur DE LA TRANSACTION est supérieur à l'argent du joueur, sinon transaction abandonnée
        pass
        
    def start(self):
        if self.check_item_owner():
            if not self.check_is_full():
                if self.check_balance():
                    self.succes()
    
    def succes(self):
        #si tout est en ordre, alors on peut faire la transaction
        pass 
                    