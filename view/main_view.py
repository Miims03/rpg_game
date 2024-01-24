from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel , QMainWindow , QPushButton , QVBoxLayout , QLineEdit , QHBoxLayout , QWidget
from view.game_view import GameWindow



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MainWindow")
        self.setGeometry(100, 100, 700, 500)  # Position et taille initiale de la fenêtre
        self.show_main_layout()
        

    def show_main_layout(self):
        
        # Affiche le layout principal
        self.central_widget = GameWindow(self)
        
        self.setCentralWidget(self.central_widget)
        
        
        