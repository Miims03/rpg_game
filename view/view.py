#view.py
from model.game import Game
from prettytable import PrettyTable

class View():
    
    def __init__(self,game : 'Game'):
        self.game = game
        self.table = PrettyTable()

    def update(self):
        self.table.clear()
        
        self.table.add_column("PLAYER NAME",
            [
                self.game.player.name
            ])       
        self.table.add_column("PLAYER PV",
            [
                self.game.player.pv
            ])
        self.table.add_column("           ",
            [
                " "
            ])
        self.table.add_column("ENEMY NAME",
            [
                self.game.monster.role
            ])
        # self.table.add_rows(
        #     [
        #     [self.game.player.name, self.game.player.pv],
        #     [self.game.monster.role, self.game.monster.pv]
        #     ]  
        # )
        #print(self.game.player)
        #print(self.game.monster)
        print(self.table)

    def display_start(self):
        print("----------")
        print("START GAME")
        print("----------")



    #def display_player_up(self):

    #def display_menu_player(self):

    #def display_combat(self):

    
# x.add_column("City name",
# ["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
# x.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
# x.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092,
# 1554769])
# x.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9,
# 869.4])