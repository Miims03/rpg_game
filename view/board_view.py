from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel , QPushButton , QVBoxLayout , QWidget , QLineEdit , QGridLayout
from PySide6.QtGui import QPixmap
from cell_view import CellView

PATH_GRASS_BACKGROUND = 'view\\logo\\grass_background.png'

class BoardView(QVBoxLayout):
    def __init__(self, game=None):
        super().__init__()
        self.game = game
        self.image = QLabel()
        self.grid = QGridLayout()
        self.create_widgets()
        self.grid.setSpacing(0)
        
    
    def create_widgets(self):
        
        for x in range(0,5):
            for y in range(0,5):
                self.grid.addWidget(CellView(),x,y)
                
        pixmap = QPixmap(PATH_GRASS_BACKGROUND)
        #self.image.setPixmap(pixmap)
        self.image.setScaledContents(True)
        
        #self.addWidget(self.image)
        self.addLayout(self.grid)
        
        
                