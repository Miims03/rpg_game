from model.classes.item.inventory import *
from model.classes.player.character import Character , CharacterRole


class Player(Character):
    
    def __init__(self,name="player"):
        super().__init__(name,CharacterRole.PLAYER)
        self.pv_max = 10
        self.pv = self.pv_max
        self.mana_max = 10
        self.mana = self.mana_max
        self.stamina_max = 10
        self.stamina = self.stamina_max
        self.attack = 3
        self.magic_attack = 3
        self.armors = [2]
        self.numArmors = len(self.armors)
        # self.attack_crit = 6
        # self.crit_chance = 10
        self.inventory = Inventory()
        
    def Attack(self, monster):
        monster.pv -= self.attack
        self.stamina -= 3
        if monster.pv < 0:
            monster.pv = 0


    def __str__(self) -> str:
        return f"{self.name} (Lvl {self.lvl}) - PV: {self.pv}/{self.pv_max} - Mana: {self.mana}/{self.mana_max} - Stamina: {self.stamina}/{self.stamina_max} - Role: {self.role} - Armure: {self.numArmors}/{self.armors}"
         
    
