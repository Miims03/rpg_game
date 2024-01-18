from model.game import Game
#from view.view import View , choice_name , WRONG_INPUT
from view.view import *
from view.main_view import *

ACTIONS_LIST_CONTROLLER = ['start','exit']

ACTIONS_LIST_GAME = ['combat','inventory','exit']

#controller.py
class Controller():      

    def start(self):
        self.game = Game(choice_name())
        
        self.view = View(self.game)
        self.view.display_start()
        #TANT QUE LE JEU NEST PAS FINI
        while self.game.notFinish():
            # essaye tant que possible de faire ce qui se trouve en dessous :        
            try :
                action = self.view.ask_action(ACTIONS_LIST_CONTROLLER)
                #if fail attribution action = someting like action=None, then go except
                if action :
                    self.do_controller_action(action)
            #j'expect que action = None si ask_action trouve pas ce qui se trouve dans actions_list_controller
            except Exception :
                #je passe car self.view.ask_action(ACTIONS_LIST) va déjà se charger de check si c'est bon ou pas, et si pas bon ben il print l'error             
                pass
                        
    def do_controller_action(self,action):
        match action:
            case 'start':
                self.game.play()
                pass
            case 'exit':
                exit()
            case _:
                self.view.display_error(WRONG_INPUT)
                
    def start2(self):
        app = QApplication(sys.argv)
        self.ui_view = MainWindow()
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
                   