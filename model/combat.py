from model.classes.player.player import Player
from model.classes.player.healer import Healer
from model.classes.player.warrior import Warrior
from model.classes.enemy.monster import Monster

class Combat():
    
    def __init__(self,player : 'Player',ennemi : 'Monster'):
        self.player = player
        self.monster = ennemi
        self.actions = []
    
    def is_someone_dead(self):
        if self.monster.pv <=0 or self.player.pv<=0:
            return True
        return False   
    
    def play(self):
        if self.player.role == 'Novice':
            while not self.is_someone_dead():
                print(self.player)
                print(self.monster)           
                action = input("What do you want to do ? [attack] :\n")
                match action.lower():
                    case 'attack':
                        self.player.Attack(self.monster)
                        print(f'\n{self.player.name} attaque de {self.player.attack} pv')
                        self.monster.Attack(self.player)
                        print(f'{self.monster.role} attaque de {self.monster.attack} pv\n')
                        pass
                    case _:
                        print("MAUVAISE INPUT")
                        pass
            print("someone just die oO")