from model.classes.player.player import Player
from model.classes.player.healer import Healer
from model.classes.player.warrior import Warrior
from model.classes.enemy.monster import Monster


class Game(): 

    def __init__(self,name):
        self.player = Player(name)
        self.monster = Monster()
    

    def lvl_up(self):
        self.player.lvl += 19
        if(self.player.lvl ==20):
            print("Congrate ! You can now change Sup Class !")
            self.player = self.new_class()
        
    def new_class(self):
        is_done = False
        while not is_done:
            role = input("What do you want to be ? [healer/warrior] :\n")
            match role.lower():
                case 'healer':
                    is_done=True
                    return self.changeClassHealer()                   
                case 'warrior':
                    is_done=True
                    return self.changeClassWarrior()
                case _:
                    print("WRONG INPUT. ENTER AGAIN")
                    pass


    def notFinish(self):
        return self.player.pv > 0
        
    def play(self):
        self.do_action()
    
    def changeClassHealer(self,newclass :'Player'):
        if self.lvl >= 20:
            newHealer = Healer(self.name)
            newHealer.lvl = self.lvl
            return newHealer
        else:
            print("Vous n'avez pas le niveau requis")
            return self
    
    def changeClassWarrior(self):
        if self.player.lvl >= 20:
            newWarrior = Warrior(self.player.name)
            newWarrior.lvl = self.player.lvl
            return newWarrior
        else:
            print("Vous n'avez pas le niveau requis")
            return self

    def do_action(self):
        action = input("What do you want to do ? [combat/inventory] :\n")
        match action.lower():
            case 'combat':
                self.combat()
                pass
            case 'inventory':
                print("Dans l'inventaire")
                pass
            case _:
                print("PAS A VOIR !!!")
                
    def is_someone_dead(self):
        if self.monster.pv <=0 or self.player.pv<=0:
            return True
        return False               
                
    def combat(self):
        #print(f"\nPv {self.player.name} : {self.player.pv}\nStamina {self.player.name} : {self.player.stamina}\nMana {self.player.name} : {self.player.mana}\nNombre d'armure : {self.player.numArmors}\nArmure : {self.player.armors}\n")
        #print(f'Pv {self.monster.role} : {self.monster.pv}\nStamina {self.monster.role} : {self.monster.stamina}\n')
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
                

        # if self.player.role == 'Warrior':
        #     while self.monster.pv >=0:           
        #         action = input("What do you want to do ? [attack/get armor/give armor] :\n")
        #         match action:
        #             case 'attack':
        #                 self.player.Attack(self.monster)
        #                 pass
        #             case 'get armor':
        #                 self.player.(self.monster)
        #                 pass
        #             case 'give armor':
        #                 self.player.Attack(self.monster)
        #                 pass
        #             case _:
        #                 print("MAUVAISE INPUT")
        #                 pass

        # if self.player.role == 'Healer':
        #     while self.monster.pv >=0:           
        #         action = input("What do you want to do ? [attack/get armor/give armor] :\n")
        #         match action:
        #             case 'attack':
        #                 self.player.Attack(self.monster)
        #                 pass
        #             case 'get armor':
        #                 self.player.Attack(self.monster)
        #                 pass
        #             case 'give armor':
        #                 self.player.Attack(self.monster)
        #                 pass
        #             case _:
        #                 print("MAUVAISE INPUT")
        #                 pass
            
            