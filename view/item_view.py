
from PySide6.QtCore import Qt, QMimeData
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QGridLayout , QApplication
from PySide6.QtGui import QPixmap, QDragEnterEvent, QDropEvent, QMouseEvent, QDrag

PATH_MEAT_LOGO = 'view\\logo\\meat.png'

class ItemView(QWidget):
    def __init__(self, item=None):
        super().__init__()
        self.item = item
        self.create_widgets()

    def create_widgets(self):
        pixmap = QPixmap(PATH_MEAT_LOGO)  # Utilisez le chemin approprié pour l'image de l'item
        self.image_label = QLabel()
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)

        layout = QVBoxLayout(self)
        layout.addWidget(self.image_label)

        # Connecter les événements de souris
        self.setMouseTracking(True)
        self.image_label.mousePressEvent = self.mousePressEvent
        self.image_label.mouseMoveEvent = self.mouseMoveEvent



    # def mousePressEvent(self, event: QMouseEvent):
    #     if event.button() == Qt.LeftButton:
    #         # Commencer le drag-and-drop
    #         drag = QDrag(self)
    #         mime_data = QMimeData()
    #         # Ajouter des données spécifiques à l'item ici
    #         mime_data.setText(self.item.name)
    #         drag.setMimeData(mime_data)

    #         # Définir l'icône de l'objet glissé
    #         drag.setPixmap(QPixmap(self.item.image_path))
    #         drag.exec_()

    # def mouseMoveEvent(self, event: QMouseEvent):
    #     # Gérer le déplacement de la souris ici (si nécessaire)
    #     pass


if __name__ == '__main__':
    app = QApplication()

    # Créer une instance de CellView avec le type de votre choix
    item_view = ItemView()

    # Organiser le widget dans une mise en page (layout)
    layout = QVBoxLayout()
    layout.addWidget(item_view)

    # Créer un widget principal pour contenir le layout
    main_widget = QWidget()
    main_widget.setLayout(layout)
    main_widget.setWindowTitle('Test de ItemView')

    # Afficher la fenêtre
    main_widget.show()

    # Lancer l'application
    exit(app.exec())