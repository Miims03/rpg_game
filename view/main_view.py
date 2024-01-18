from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel , QMainWindow , QPushButton , QVBoxLayout , QLineEdit , QHBoxLayout , QWidget
from game_view import GameWindow
# idem que background-color: green mais en plus clair
COLOR_STYLE_GREEN = "background-color: rgb(0, 200, 0)" 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemple de Fenêtre")
        #self.setGeometry(100, 100, 300, 200)  # Position et taille initiale de la fenêtre
        self.show_main_layout()

    def handle_submit(self):
        self.show_game_layout()
        
    def handle_submit_check(self):
        if len(self.entry.text()) >=5:
            self.start_button.setStyleSheet(COLOR_STYLE_GREEN)
            self.start_button.setDisabled(False)
        else:
            self.start_button.setDisabled(True)

    def show_main_layout(self):
        # Affiche le layout principal
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        label = QLabel("Bienvenue dans RPG Game !")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_username = QLabel("Username:")
        self.entry = QLineEdit()
        self.start_button = QPushButton("start")
  
        self.start_button.setDisabled(True)
        exit_button = QPushButton("exit")
        #Connect signal
        self.start_button.clicked.connect(self.handle_submit)
        exit_button.clicked.connect(self.close)
        self.entry.cursorPositionChanged.connect(self.handle_submit_check)

        #Horizontal
        user_layout = QHBoxLayout()
        user_layout.addWidget(label_username)
        user_layout.addWidget(self.entry)
        user_layout.addWidget(self.start_button)
        
        #Vertical
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addLayout(user_layout)
        layout.addWidget(exit_button)

        self.central_widget.setLayout(layout)

    def show_game_layout(self):
        self.setCentralWidget(GameWindow())
        
        

if __name__ == '__main__':
    app = QApplication()
    # Créer une instance de CellView avec le type de votre choix
    main_view = MainWindow()
    main_view.show()
    # Lancer l'application
    exit(app.exec())