from PySide6.QtCore import Qt, QMimeData , QSize , QRect 
from PySide6.QtWidgets import QVBoxLayout,QMainWindow, QGridLayout,QGraphicsSimpleTextItem, QGraphicsWidget,QGraphicsLayoutItem,QLabel, QWidget, QGraphicsGridLayout , QApplication , QHBoxLayout , QGraphicsItem , QBoxLayout , QGraphicsItem , QGraphicsProxyWidget , QGraphicsScene , QGraphicsView , QGraphicsEllipseItem
from PySide6.QtGui import QPixmap, QDragEnterEvent, QDropEvent, QMouseEvent, QDrag , QFont , QColor


class DragItem(QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setContentsMargins(25, 5, 25, 5)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("border: 1px solid black;")
        # Store data separately from display label, but use label for default.
        self.data = self.text()

    def set_data(self, data):
        self.data = data

    def mouseMoveEvent(self, e):

        if e.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)

            pixmap = QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)

            drag.exec(Qt.MoveAction)


class DragWidget(QWidget):
    """
    Generic list sorting handler.
    """

    #orderChanged = pyqtSignal(list)

    def __init__(self, *args, orientation=Qt.Orientation.Vertical, **kwargs):
        super().__init__()
        self.setAcceptDrops(True)

        # Store the orientation for drag checks later.
        self.orientation = orientation

        if self.orientation == Qt.Orientation.Vertical:
            self.blayout = QVBoxLayout()
        else:
            self.blayout = QHBoxLayout()

        self.setLayout(self.blayout)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        pos = e.position()
        widget = e.source()

        for n in range(self.blayout.count()):
            # Get the widget at each index in turn.
            w = self.blayout.itemAt(n).widget()
            if self.orientation == Qt.Orientation.Vertical:
                # Drag drop vertically.
                drop_here = pos.y() < w.y() + w.size().height() // 2
            else:
                # Drag drop horizontally.
                drop_here = pos.x() < w.x() + w.size().width() // 2

            if drop_here:
                # We didn't drag past this widget.
                # insert to the left of it.
                self.blayout.insertWidget(n-1, widget)
                #self.orderChanged.emit(self.get_item_data())
                break

        e.accept()

    def add_item(self, item):
        self.blayout.addWidget(item)

    def get_item_data(self):
        data = []
        for n in range(self.blayout.count()):
            # Get the widget at each index in turn.
            w = self.blayout.itemAt(n).widget()
            data.append(w.data)
        return data


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.drag = DragWidget(orientation=Qt.Orientation.Vertical)
        for n, l in enumerate(['A', 'B', 'C', 'D']):
            item = DragItem(l)
            item.set_data(n)  # Store the data.
            self.drag.add_item(item)

        # Print out the changed order.
        #self.drag.orderChanged.connect(print)

        container = QWidget()
        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addWidget(self.drag)
        layout.addStretch(1)
        container.setLayout(layout)

        self.setCentralWidget(container)


app = QApplication([])
w = MainWindow()
w.show()

app.exec()






# class DraggableLabel(QLabel):
#     def __init__(self, text, parent=None):
#         super(DraggableLabel, self).__init__(text, parent)
#         self.setAcceptDrops(True)

#     def mousePressEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             drag = QDrag(self)
#             mime_data = QMimeData()
#             mime_data.setText(self.text())
#             drag.setMimeData(mime_data)
#             drag.exec()

# class DropGrid(QGraphicsWidget):
#     def __init__(self, rows, columns, parent=None):
#         super(DropGrid, self).__init__(parent)
#         self.grid_layout = QGraphicsGridLayout(self)
#         self.rows = rows
#         self.columns = columns
#         self.setAcceptDrops(True)
#         self.init_grid()

#     def init_grid(self):
#         for row in range(self.rows):
#             for col in range(self.columns):
#                 label = DraggableLabel(f"Cell {row}-{col}")
#                 label.setAlignment(Qt.AlignCenter)
#                 proxy = QGraphicsProxyWidget()
#                 proxy.setWidget(label)
#                 proxy.setAcceptDrops(True)
#                 self.grid_layout.addItem(proxy, row, col)

#     def dragEnterEvent(self, event):
#         if event.mimeData().hasText():
#             event.acceptProposedAction()

#     def dropEvent(self, event):
#         if event.mimeData().hasText():
#             destination_pos = event.pos()

#             # Trouver l'item existant à la position de dépôt
#             items = self.items(destination_pos)
#             existing_item = None
#             for item in items:
#                 if isinstance(item, DraggableLabel):
#                     existing_item = item
#                     break

#             if existing_item:
#                 # Échanger les textes
#                 source_text = event.mimeData().text()
#                 existing_text = existing_item.text()

#                 existing_item.setText(source_text)
#                 event.source().setText(existing_text)

#             event.setDropAction(Qt.MoveAction)
#             event.accept()


# if __name__ == "__main__":
#     app = QApplication([])
#     view = QGraphicsView()
#     scene = QGraphicsScene(view)

#     drop_grid = DropGrid(5, 5)
#     drop_grid.setAcceptDrops(True)
    
#     scene.addItem(drop_grid)

#     view.setScene(scene)
#     view.show()
#     exit(app.exec())


# class DraggableLabel(QLabel):
#     def __init__(self, text, parent=None):
#         super(DraggableLabel, self).__init__(text, parent)
#         self.setAcceptDrops(True)
        

#     def mousePressEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             drag = QDrag(self)
#             mime_data = QMimeData()
#             mime_data.setText(self.text())
#             drag.setMimeData(mime_data)
#             drag.exec()

# class DropGrid(QGraphicsWidget):
#     def __init__(self, rows, columns, parent=None):
#         super(DropGrid, self).__init__(parent)
#         self.grid_layout = QGraphicsGridLayout(self)
#         self.rows = rows
#         self.columns = columns
#         self.setAcceptDrops(True)
#         self.init_grid()

#     def init_grid(self):
#         for row in range(self.rows):
#             for col in range(self.columns):
#                 label = QLabel(f"Cell {row}-{col}")
#                 label.setAlignment(Qt.AlignCenter)
#                 proxy = QGraphicsProxyWidget()
#                 proxy.setWidget(label)
                
#                 self.grid_layout.addItem(proxy, row, col)

#     def dragEnterEvent(self, event):
#         if event.mimeData().hasText():
#             event.acceptProposedAction()

#     def dropEvent(self, event):
#         if event.mimeData().hasText():
#             source_item = event.source()
#             destination_pos = event.pos()

#             # Trouver l'item existant à la position de dépôt
#             items = self.items(destination_pos)
#             existing_item = None
#             for item in items:
#                 if isinstance(item, QGraphicsProxyWidget):
#                     existing_item = item
#                     break

#             if existing_item:
#                 # Échanger les positions
#                 source_item_pos = source_item.pos()
#                 existing_item_pos = existing_item.pos()

#                 source_item.setPos(existing_item_pos)
#                 existing_item.setPos(source_item_pos)

#             event.setDropAction(Qt.MoveAction)
#             event.accept()


# if __name__ == "__main__":
#     app = QApplication([])
#     view = QGraphicsView()
#     scene = QGraphicsScene(view)

#     drop_grid = DropGrid(5, 5)
#     scene.addItem(drop_grid)

#     label = DraggableLabel("Drag me!")
#     label.setAlignment(Qt.AlignCenter)
#     proxy = QGraphicsProxyWidget()
#     proxy.setWidget(label)
#     scene.addItem(proxy)

#     view.setScene(scene)
#     view.show()
#     exit(app.exec())


# class MyLabel(QGraphicsSimpleTextItem):
#     def __init__(self, text="", parent=None):
#         super(MyLabel, self).__init__(text, parent)
#         self.setFont(QFont("Arial", 16))
#         self.setAcceptDrops(True)

# if __name__ == "__main__":
#     app = QApplication()
#     view = QGraphicsView()
#     scene = QGraphicsScene(view)

#     label = QLabel("Hello World")
#     #label.setPos(10, 10)
#     truc = QGraphicsWidget()
#     grid = QGraphicsGridLayout(truc)
#     for x in range(10):
#         for y in range(10):
#             label = QLabel("[o]")
#             proxy = QGraphicsProxyWidget()
#             proxy.setWidget(label)
#             proxy.setAcceptDrops(True)
#             grid.addItem(proxy,x,y)
#     view.setAcceptDrops(True)
#     # grid.removeAt(0)
#     # proxy = QGraphicsProxyWidget()
#     # proxy.setWidget(label)        
#     # grid.addItem(proxy,0,0)
    
#     scene.addItem(truc)

#     view.setScene(scene)
#     view.show()
#     exit(app.exec())