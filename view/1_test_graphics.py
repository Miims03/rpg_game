
from PySide6.QtCore import Qt, QMimeData , QSize , QRect 
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QPushButton , QApplication , QHBoxLayout , QGraphicsItem , QBoxLayout , QGraphicsItem , QGraphicsProxyWidget , QGraphicsScene , QGraphicsView , QGraphicsEllipseItem
from PySide6.QtGui import QPixmap, QDragEnterEvent, QDropEvent, QMouseEvent, QDrag , QFont , QColor


class MyGraphicsItem(QGraphicsEllipseItem):
    def __init__(self):
        super(MyGraphicsItem, self).__init__(0, 0, 50, 50)
        self.setBrush(Qt.red)
        self.setAcceptDrops(True)

    def mousePressEvent(self, event):
        print("Item clicked!")


class MyGraphicsView(QGraphicsView):
    def __init__(self, scene):
        super(MyGraphicsView, self).__init__(scene)
        self.setAcceptDrops(True)


class MyGraphicsScene(QGraphicsScene):
    def __init__(self):
        super(MyGraphicsScene, self).__init__()

        # Create a custom QGraphicsItem
        my_item = MyGraphicsItem()
        my_item.setPos(100, 100)

        # Add the item to the scene
        self.addItem(my_item)
        


def main():
    app = QApplication()
    
    scene = MyGraphicsScene()
    view = MyGraphicsView(scene)
    view.show()

    exit(app.exec())


if __name__ == '__main__':
    main()