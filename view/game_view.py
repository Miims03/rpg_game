from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel , QPushButton , QVBoxLayout , QWidget , QLineEdit , QGridLayout
from board_view import BoardView
from PySide6.QtGui import QPixmap
#from model.game import Game

class GameWindow(QWidget):
    def __init__(self, game = None):
        super().__init__()
        self.game = game
        self.create_widgets()
        
    def create_player_info(self):
        pass
        

    def create_widgets(self):
        # Méthode par défaut pour créer des widgets
        
        label = QLabel("Bienvenue dans le jeu.")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_root = QVBoxLayout()
        layout_root.addWidget(label)
        label1 = QLabel("Section 1")
        label2 = QLabel("Section 2")
        label3 = QLabel("Section 3")

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addLayout(BoardView())
        layout_root.addLayout(layout)

        self.setLayout(layout_root)


