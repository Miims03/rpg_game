from model.classes.player.player import Player
import random

class Healer(Player):

    def __init__(self,name):
        super().__init__(name)
        self.role = 'Healer'
        self.pv_max = 8
        self.mana_max = 15
        self.attack = 2
        self.magic_attack = 4
        self.heal = random.randint(2, 4)

        self.pv = self.pv_max
        self.mana = self.mana_max

    def MagicAttack(self,monster):
        monster.pv -= self.magic_attack
        self.mana -= 3
        if monster.pv < 0:
            monster.pv = 0
    
    def Heal(self,player):
        if player.role_base == 'Joueur':
            self.mana -= 3
            player.pv += self.heal
                
            if player.pv > player.pv_max:
                pvEnTrop = player.pv - player.pv_max
                player.pv = player.pv_max
                bonHeal  = self.heal - pvEnTrop
                print(f'{self.name} Soigne {player.name} de {bonHeal}')
                print(f'{player.name} est full hp')
            else:
                print(f'{self.name} Soigne {player.name} de {self.heal}') 