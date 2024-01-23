
from PySide6.QtCore import Qt, QMimeData , QSize , QRect 
from PySide6.QtWidgets import QLabel,QGridLayout, QVBoxLayout, QWidget, QPushButton , QApplication , QHBoxLayout , QToolTip , QBoxLayout
from PySide6.QtGui import QPixmap, QDragEnterEvent, QDropEvent, QMouseEvent, QDrag , QFont , QColor




class DraggableLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setAcceptDrops(True)
        self.mousePressPos = None
        self.mouseMovePos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mousePressPos = event.globalPosition().toPoint()
            self.mouseMovePos = event.globalPosition().toPoint()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.mousePressPos:
                delta = event.globalPosition().toPoint() - self.mouseMovePos
                self.move(self.x() + delta.x(), self.y() + delta.y())
                self.mouseMovePos = event.globalPosition().toPoint()
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mousePressPos = None
        super().mouseReleaseEvent(event)

def main():
    app = QApplication()
    grid = QGridLayout()
    for i in range(5):
        for y in range(5):
            label = DraggableLabel(f"Cell {i}-{y}")
            grid.addWidget(label,i,y)
    scene = QWidget()
    
    #scene.setAcceptDrops(True)
    scene.setLayout(grid)
    scene.show()
    app.exec()

if __name__ == "__main__":
    main()


# class DragButton(QPushButton):

#     def mouseMoveEvent(self, e):

#         if e.buttons() == Qt.LeftButton:
#             drag = QDrag(self)
#             mime = QMimeData()
#             drag.setMimeData(mime)
#             drag.exec(Qt.MoveAction)


# class Window(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.setAcceptDrops(True)

#         self.blayout = QHBoxLayout()
#         for l in ['A', 'B', 'C', 'D']:
#             btn = DragButton(l)
#             self.blayout.addWidget(btn)

#         self.setLayout(self.blayout)

#     def dragEnterEvent(self, e):
#         e.accept()

#     def dropEvent(self, e):
#         pos = e.pos()
#         widget = e.source()

#         for n in range(self.blayout.count()):
#             # Get the widget at each index in turn.
#             w = self.blayout.itemAt(n).widget()
#             if pos.x() < w.x() + w.size().width() // 2:
#                 # We didn't drag past this widget.
#                 # insert to the left of it.
#                 self.blayout.insertWidget(n-1, widget)
#                 break

#         e.accept()


# app = QApplication()
# w = Window()
# w.show()

# app.exec()