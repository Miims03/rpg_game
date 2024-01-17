#view.py
from model.game import Game
from view.message import *

class View():
    
    def __init__(self,game : 'Game'):
        self.game = game
        self.historique = [Message]
        
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

    def register_message(self,action):
        self.historique.append(action)
      
    def display_error(self,error):
        self.display_message(error,ERROR)
    
    def display_message(self,message, STATUS=MSG):
        msg = Message(message,STATUS)
        print(msg)
        self.register_message(msg)
    
    def check_input(self,input_action,list_actions):
        for default_action in list_actions:
            if default_action == input_action:
                return input_action
        #si on retourne rien c'est qui a error input
        self.display_error(f"{WRONG_INPUT} : <<{input_action}>> is not inside {list_actions}")
        #print("Faut agiiir, gros , j'ai pas le temps !")
        return None
    
    def ask_action(self,list_actions):
        choices_str = '['
        for default_action in list_actions:
            choices_str +=default_action+'/'
        choices_str+=']'
        action = input(f"What do you want to do ? {choices_str}:\n").lower() #same as match action.lower():
        return self.check_input(action,list_actions)
    
    
    def bordered_message(self, message ,width=40):
        border = "-" * width
        #padded_message = f"{border}\nPriority: {self.priority}, Message: {self.message}\n"
        padded_message = f"{border}\n{message.center(width)}\n{border}"
        return padded_message
    
    def display_start(self):
        print(self.bordered_message("START GAME"))

#Ne fait plus partie de la class View , fonction globale
def choice_name():
        name = input("Choice your player name : ")
        return name

    #def display_player_up(self):

    #def display_menu_player(self):

    #def display_combat(self):

