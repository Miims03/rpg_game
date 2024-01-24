from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel , QDialog , QPushButton , QVBoxLayout , QLineEdit , QHBoxLayout , QWidget

# idem que background-color: green mais en plus clair
COLOR_STYLE_GREEN = "background-color: rgb(0, 200, 0)" 

class AuthenticationView(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AuthenticationView")
        
        self.show_layout()
        
    def handle_submit_check(self):
        if len(self.entry.text()) >=5:
            self.start_button.setStyleSheet(COLOR_STYLE_GREEN)
            self.start_button.setDisabled(False)
        else:
            self.start_button.setDisabled(True)

    def show_layout(self):
        # Affiche le layout principal
    
        label = QLabel("Bienvenue dans RPG Game !")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_username = QLabel("Username:")
        self.entry = QLineEdit()
        self.start_button = QPushButton("start")
        self.start_button.setDisabled(True)
        exit_button = QPushButton("exit")
        
        #Connect signal
        #self.start_button.clicked.connect(self.handle_submit)
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

        self.setLayout(layout)
        
        