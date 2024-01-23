from PySide6.QtCore import Qt, QMimeData , QSize , QRect
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QPushButton , QApplication , QHBoxLayout , QToolTip , QGridLayout
from PySide6.QtGui import QPixmap, QDragEnterEvent, QDropEvent, QMouseEvent, QDrag , QFont 
from model.classes.item.inventory import *
from view.item_view import ItemView , SIZE_ITEM , Item


def test():
    i = Inventory()
    itema = Item(name="Plaque Fer",description="Une plaque en Fer classique",item_type=ItemType.ARMOR)
    itemab = Item(name="Epee Fer",description="Une Epee en Fer assez classique",item_type=ItemType.WEAPON)
    itemabc = Item(name="Potion rich en Fer",description="Une potion pour les os fragiles",item_type=ItemType.CONSUMABLE)
    i.add_item(itema)
    i.add_item(itemab)
    i.add_item(itemabc)
    return i


class InventoryView(QWidget):
    
    def __init__(self,inventory : 'Inventory' = None):
        super().__init__()
        self.inventory = inventory
        #self.setFixedSize(QSize(300,300))
        self.setAcceptDrops(True)
        self.create_widgets()
        
        
    def get_item_or_none(self, item_list):
        if item_list:
            item_key = item_list.pop()
            return self.inventory.get_item(item_key)
        else:
            return None

        
    def create_widgets(self):
        self.grid = QGridLayout()
        x = 0
        y = 0
        item_list = list(self.inventory.items.keys())
        index = len(item_list)
        
        for y in range(0,4):
            for x in range(0,5):
                #tes = QWidget()
                if(index > 0):
                    item_view = ItemView(self.get_item_or_none(item_list))
                    index=index-1
                else:
                    item_view = ItemView()
                #item_view.setSpacing(0)
                #tes.setLayout(item_view)        
                self.grid.addWidget(item_view,y,x,Qt.AlignmentFlag.AlignCenter)
                
        self.grid.setSpacing(0)
            
        # for item in self.inventory.items.values():
        #     item_view = ItemView(item)
        #     tes = QWidget()
        #     tes.setLayout(item_view)
        #     self.grid.addWidget(tes,y,x,Qt.AlignmentFlag.AlignCenter)
        #     x+=1
        #     if x>=4:
        #         y+=1
        #         x=0
        
        self.setLayout(self.grid)
        #self.addLayout(self.grid)
        
        
    def dragEnterEvent(self, e):
        e.accept()
    
    def dropEvent(self, e):
        
        pos = e.position()
        widget_to_replace = self.target(pos)
        widget = e.source()
        print("drop :",widget_to_replace)
        print("widget :",widget)


    """
    target convert x.y "pixel position" into position on grid.
    row, col position. This is strongly dependant of background picture
    size and item side.
    """
    def target(self,position):
        row = (position.x() / SIZE_ITEM)
        col = (position.y() / SIZE_ITEM)
        return int(col),int(row)

