from model.game import Game
from view.view import View

#controller.py
class Controller():      

    def start(self):
        self.game = Game(self.choice_name())
        self.view = View(self.game)
        self.view.display_start()
        #TANT QUE LE JEU NEST PAS FINI
        while self.game.notFinish():
            action = self.ask_action()
            if action == 'start':
                self.game.play()
                #self.view.update()
            if action == 'exit':
                exit()   

    def choice_name(self):
        name = input("Choice your player name : ")
        return name

    def ask_action(self):
        action = input("What do you want to do ? [start/exit] :\n")
        match action.lower():          
            case 'start':
                print('start')
                return 'start'
            case 'exit':
                print('exit')
                return 'exit'
            case _:
                print("Faut agiiir, gros , j'ai pas le temps !")
                return None
        