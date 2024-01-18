
from PySide6.QtCore import Qt 
from PySide6.QtWidgets import QLabel , QApplication , QVBoxLayout , QWidget , QHBoxLayout
from PySide6.QtGui import QPixmap

TYPE_FALL = -1
TYPE_GRASS = 0
TYPE_STAR = 1

PATH_GRASS_LOGO = 'view\\logo\\grass_logo.png'


class CellView(QLabel):
    
    def __init__(self,type=TYPE_GRASS):
        super().__init__()
        self.type = type
        self.create_widgets()
        
    
    def create_widgets(self):
        #Une casse a une image
        pixmap = QPixmap(PATH_GRASS_LOGO)
        if not pixmap:
            print("error")
        self.setPixmap(pixmap)
        self.setScaledContents(True)
        #for debug
        #self.setStyleSheet("QLabel {""background-color: none;""color : black;""border: 1px solid black;}")


        

if __name__ == '__main__':
    app = QApplication()

    # Créer une instance de CellView avec le type de votre choix
    cell_view = CellView(TYPE_GRASS)

    # Organiser le widget dans une mise en page (layout)
    layout = QVBoxLayout()
    layout.addWidget(cell_view)

    # Créer un widget principal pour contenir le layout
    main_widget = QWidget()
    main_widget.setLayout(layout)
    main_widget.setWindowTitle('Test de CellView')

    # Afficher la fenêtre
    main_widget.show()

    # Lancer l'application
    exit(app.exec())