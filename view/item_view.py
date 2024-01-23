
from PySide6.QtCore import Qt, QMimeData , QSize , QRect 
from PySide6.QtWidgets import QLabel, QGraphicsPixmapItem, QWidget, QPushButton , QGraphicsItem , QHBoxLayout , QToolTip , QBoxLayout
from PySide6.QtGui import QPixmap, QDragEnterEvent, QDropEvent, QMouseEvent, QDrag , QFont , QColor
from model.classes.item.item import Item 


SIZE_ITEM = 70

PATH_MEAT_LOGO = 'view\\logo\\meat.png'
PATH_GRASS_LOGO = 'view\\logo\\grass_logo.png'

class CustomToolTip(QToolTip):
    def __init__(self,widget):
        super(CustomToolTip,self).__init__()
        self.widget = widget
        # Définir la police par défaut pour le tooltip
        font = QFont("Arial", 25)
        self.setFont(font)
        self.item_text = ""
        # Créer un QGraphicsRectItem
        self.rect_item = QRect(100, 200, 50, 50)
        # Définir la bordure noire
        
    
    # def set_text(self,item_text):
    #     if item_text:
    #         self.item_text = item_text.replace('|', '\n')
    #     else:
    #         self.item_text = 'pas encore choisi : None'

        
    def show_text(self):
        self.showText(self.widget.mapToGlobal(self.widget.rect().bottomLeft()), self.item_text, self.widget,self.rect_item,50000)
    

class ItemView(QLabel):
    def __init__(self, item : 'Item'=None):
        super().__init__()
        self.item = item
        self.setContentsMargins(0, 0, 0, 0)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("border: 1px solid black;")
        self.setFixedSize(QSize(SIZE_ITEM,SIZE_ITEM))
        self.setAcceptDrops(True)
        self.create_widgets()
        self.toolTip = CustomToolTip(self)
        #c'est possible ça ?
        #self.connect(#le label self avec l'evenement UnderMouse, pour la fonction hello)
              
        
    def set_text(self,item_text = None):
        if item_text:
            return item_text.replace('|', '\n')
        else:
            return 'pas encore choisi : None'

    def create_widgets(self):     
        
        #1.charge l'image de l'item 
        # Utilisez le chemin approprié pour l'image de l'item !!!!
        #self.pixmap =  QPixmap(PATH_MEAT_LOGO)
        
        if self.item:
            self.setPixmap(QPixmap(PATH_MEAT_LOGO))
            self.setToolTip(self.set_text(str(self.item)))
        else:
            self.setPixmap(QPixmap(PATH_GRASS_LOGO))
            self.setToolTip(self.set_text())
        
        #self.tool = CustomToolTip(self)
        #self.tool.set_text(str(self.item))
        
        #tool.set_custom_tooltip(self.rect)
        #self.rect.setToolTip("j'ai ici une longue\n description qui peut durée longtemps\n donc vaut mieux check")
        #self.setToolTip("tessts")
        #self.button_item.clicked.connect(self.display_text)
        
        #self.display_text()   
       
    def mouseMoveEvent(self, e):

        if e.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)

            pixmap = QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)

            drag.exec(Qt.MoveAction)
    

   
    # def mouseMoveEvent(self, event):

    #     if event.buttons() == Qt.MouseButton.LeftButton:
    #         print("iciii")
    #         drag = QDrag(self)
    #         mime = QMimeData()
    #         drag.setMimeData(mime)
    #         #drag.setPixmap(self.pixmap)
    #         drag.exec(Qt.MoveAction)

# if __name__ == '__main__':
#     app = QApplication()

#     # Créer une instance de CellView avec le type de votre choix
#     # Créer un widget principal pour contenir le layout
#     main_widget = QWidget()
#     main_widget.setLayout(ItemView())
#     main_widget.setWindowTitle('Test de ItemView')

#     # Afficher la fenêtre
#     main_widget.show()

#     # Lancer l'application
#     exit(app.exec())