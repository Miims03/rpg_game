class Monster:

    def __init__(self):

        self.role_base = 'Ennemi'
        self.role = "Monstre"
        self.lvl = 2
        self.pv_max = 20
        self.pv = self.pv_max
        self.mana_max = 10
        self.mana = self.mana_max
        self.stamina_max = 10
        self.stamina = self.stamina_max
        self.attack = 5

    def Attack(self,player):
        if player.role_base == "Joueur":
            if player.numArmors >= 1:
                player.armors[0] -= self.attack
                self.stamina -= 3
                if player.armors[0] <= 0:
                    player.pv += player.armors[0]
                    player.armors.pop(0)
                    player.numArmors -= 1
            else :
                player.pv -= self.attack
                self.stamina -= 3
            if player.pv < 0:
                player.pv = 0
    
    def __str__(self) :
        return f"{self.role} (Lvl {self.lvl}) - PV: {self.pv}/{self.pv_max} - Mana: {self.mana}/{self.mana_max} - Stamina: {self.stamina}/{self.stamina_max} - Attack: {self.attack}"


