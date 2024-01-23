from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel , QPushButton , QVBoxLayout , QWidget , QHBoxLayout , QGridLayout , QDialog
from view.board_view import BoardView
from view.inventory_view import InventoryView , test
from PySide6.QtGui import QPixmap
from model.game import Game


class GameWindow(QWidget):
    
    
    def __init__(self,parent : QWidget | None, game = None):
        super().__init__(parent)
        self.game = game
        self.create_widgets()
        
    def show_inventory_layout(self):
        inventory_view = InventoryView(test())
        layout = QHBoxLayout()
        layout.addWidget(inventory_view)
        self.label1.setLayout(layout)
        print('test invo')
        # inventory_view.show()
        
        

    def create_widgets(self):
        # Méthode par défaut pour créer des widgets
        
        label = QLabel("Bienvenue dans le jeu.")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_root = QVBoxLayout()
        self.layout_root.addWidget(label)
        
        inventaire = QPushButton("Inventaire")
        
        
        self.label1 = QLabel("Section 1")
        label2 = QLabel("Section 2")
        label3 = QLabel("Section 3")

        layout = QVBoxLayout()
        layout.addWidget(inventaire)
        layout.addWidget(self.label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addLayout(BoardView())
        self.layout_root.addLayout(layout)

        self.setLayout(self.layout_root)
        
        #signal 
        inventaire.clicked.connect(self.show_inventory_layout)


