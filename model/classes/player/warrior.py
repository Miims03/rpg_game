from model.classes.player.player import Player

class Warrior(Player):

    def __init__(self,name):

        super().__init__(name)
        self.role = 'Warrior'
        self.pv_max = 10
        self.mana_max = 8
        self.attack = 4
        self.magic_attack = 0
        self.pv = self.pv_max
        self.mana = self.mana_max
        self.armors = [3,3]
        self.numArmors = len(self.armors)
        self.armors_add = 3

    def get_armor(self):
        if self.mana >= 4:
            self.mana -= 4
            self.armors.append(self.armors_add)
            self.armors.append(self.armors_add)
            self.numArmors = len(self.armors)
        else:
            if self.mana < 4:
                print("\nVous n'avez plus de mana")

    def give_armor(self,player):
        if player.role_base == 'Joueur':
            if self.numArmors >= 1 and self.mana >= 2:
                self.mana -= 2
                self.armors.pop(0)
                player.armors.append(self.armors_add)
                self.numArmors = len(self.armors)
                player.numArmors = len(player.armors)
            else:
                if self.numArmors == 0:
                    print("\nVous n'avez plus d'armures")
                elif self.mana < 2:
                    print("\nVous n'avez plus de mana")