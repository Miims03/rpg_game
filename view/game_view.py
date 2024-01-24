from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel , QPushButton , QVBoxLayout , QWidget , QHBoxLayout , QGridLayout , QDialog , QStackedWidget , QGraphicsView , QGraphicsScene
from view.board_view import BoardView
from view.inventory_view import InventoryView , test
from PySide6.QtGui import QPixmap
from model.game import Game
from view.player_view import PlayerView


class MiniMap(QGraphicsView):
    def __init__(self, scene, parent=None):
        super().__init__(scene, parent)
        self.setSceneRect(scene.sceneRect())
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)


class GameWindow(QWidget):
    
    def __init__(self,parent : QWidget | None):
        super().__init__(parent)
        self.game = Game("PlayerTesT")
        self.game.player.inventory = test()
        self.setWindowTitle("GameWindow")
        self.create_widgets()
        
    def show_inventory_layout(self):
        current_index = self.stacked_widget.currentIndex()
        if current_index == 0:
            self.stacked_widget.setCurrentIndex(1)
        elif current_index == 1:
            self.stacked_widget.setCurrentIndex(0)
        

    def create_widgets(self):
        # Méthode par défaut pour créer des widgets
        
        label = QLabel("Bienvenue dans le jeu.")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_root = QVBoxLayout()
        self.layout_root.addWidget(label)
        
        
        self.player_view = PlayerView(self.game.player)
        inventaire = QPushButton("Inventaire")
        self.inventory_view = InventoryView(self.game.player.inventory)
        
        self.label1 = QLabel("Section 1  : Statistiques problablement")
        label2 = QLabel("Section 2   : les buffs probalbment")
        label3 = QLabel("Section 3 : des racourccis items j'imagine")

        layout = QVBoxLayout()
        #layout.addWidget(self.player_view)
        encore_layout = QVBoxLayout()
        
        encore_layout.addWidget(self.label1)
        encore_layout.addWidget(label2)
        encore_layout.addWidget(label3)
        encore_layout.addWidget(inventaire)
        
        #le gros horizontal premier
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.player_view)
        h_layout.addLayout(encore_layout)
        
        scene = QGraphicsScene(self)
        scene.setSceneRect(0, 0, 500, 500)
        mini_map = MiniMap(scene)
        h_layout.addWidget(mini_map)
        
        layout.addLayout(h_layout)
        
        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.addWidget
        self.container_board = QWidget()
        self.board = BoardView()
        self.container_board.setLayout(self.board)
        self.stacked_widget.addWidget(self.container_board)
        self.stacked_widget.addWidget(self.inventory_view)
        layout.addWidget(self.stacked_widget)
        
        self.layout_root.addLayout(layout)

        
        self.setLayout(self.layout_root)
        
        #signal 
        inventaire.clicked.connect(self.show_inventory_layout)


