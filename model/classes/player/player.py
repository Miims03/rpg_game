
class Player():
    
    def __init__(self,name="player"):
        self.role_base = 'Joueur'
        self.name = name
        self.lvl = 1
        self.role = 'Novice'
        self.pv_max = 10
        self.pv = self.pv_max
        self.mana_max = 8
        self.mana = self.mana_max
        self.stamina_max = 10
        self.stamina = self.stamina_max
        self.attack = 3
        self.magic_attack = 3
        self.armors = [2]
        self.numArmors = len(self.armors)
        # self.attack_crit = 6
        # self.crit_chance = 10
        
    def Attack(self, monster):
        monster.pv -= self.attack
        self.stamina -= 3
        if monster.pv < 0:
            monster.pv = 0


    def __str__(self) -> str:
        # str=self.name
        # str+="(Lvl "
        # str+=self.lvl
        # str+=") - PV: "
        # str+=self.pv
        # str+="/"
        # str+=self.pv_max
        # str+=" - Mana: "
        # str+= self.mana
        # str+="/"
        # str+=self.mana_max
        # str+=" - Stamina: "
        # str+= self.stamina
        # str+="/"
        # str+=self.stamina_max
        # str+=" - Role: "
        # str+=self.role
        # return str
        
        return f"{self.name} (Lvl {self.lvl}) - PV: {self.pv}/{self.pv_max} - Mana: {self.mana}/{self.mana_max} - Stamina: {self.stamina}/{self.stamina_max} - Role: {self.role} - Armure: {self.numArmors}/{self.armors}"
         
    
