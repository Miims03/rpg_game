#view.py
from model.game import Game

class View():
    
    def __init__(self,game : 'Game'):
        self.game = game
        
    def display_players_and_enemies(self,players, enemies):
        max_length = max(len(players), len(enemies))

        print(f"{'Joueurs':<20}{'':<20}{'Ennemis':<20}")
        print('-' * 60)

        for i in range(max_length):
            player_str = ""
            enemy_str = ""

            if i < len(players):
                player_str = str(players[i])

            if i < len(enemies):
                enemy_str = str(enemies[i])

            print(f"{player_str:<20}{'':<20}{enemy_str:<20}")        

    def update(self):
        self.display_players_and_enemies([self.game.player],[self.game.monster])

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