from PySide6.QtCore import Qt, QMimeData , QSize , QRect 
from PySide6.QtWidgets import QComboBox, QHBoxLayout, QWidget, QProgressBar , QVBoxLayout , QLabel , QApplication , QBoxLayout 
from PySide6.QtGui import QPixmap, QDragEnterEvent, QDropEvent, QMouseEvent, QDrag , QFont , QColor



PATH_MEAT_LOGO = 'view\\logo\\meat.png'

class PlayerView(QWidget):
    def __init__(self, ):
        super().__init__()
        

        self.setFixedSize(QSize(300,180))
        self.setWindowTitle("PlayerView")

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)

        horizontal_layout = QHBoxLayout()
        main_layout.addLayout(horizontal_layout)

        # Player Info
        player_layout = QVBoxLayout()
        horizontal_layout.addLayout(player_layout)
        #name
        label_playername = QLabel("Miims", self)
        label_playername.setFont(QFont("Segoe UI", 12))
        label_playername.setAlignment(Qt.AlignmentFlag.AlignCenter)
        player_layout.addWidget(label_playername)
        #image
        label_logo_player = QLabel("ICON", self)
        label_logo_player.setFixedSize(QSize(100,100))
        #label_logo_player.setStyleSheet("background-color: rgb(0, 0, 0);")
        label_logo_player.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
        image = QPixmap(PATH_MEAT_LOGO)
        label_logo_player.setPixmap(image)
        
        player_layout.addWidget(label_logo_player)

        label_lvl = QLabel("LvL", self)
        label_lvl.setFont(QFont("Segoe UI", 12))
        label_lvl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        player_layout.addWidget(label_lvl)

        # Progress Bars
        progress_layout = QVBoxLayout()
        horizontal_layout.addLayout(progress_layout)
        #pv
        progressBar_pv = QProgressBar(self)
        progressBar_pv.setStyleSheet("QProgressBar::chunk {background-color: rgb(0, 170, 0);}")
        progressBar_pv.setMaximum(2000)
        progressBar_pv.setValue(250)
        progressBar_pv.setFont(QFont("Segoe UI", 12))
        progressBar_pv.setFormat("%v/%m")
        progressBar_pv.setAlignment(Qt.AlignmentFlag.AlignCenter)
        progress_layout.addWidget(progressBar_pv)
        #mana
        progressBar_mana = QProgressBar(self)
        progressBar_mana.setStyleSheet("QProgressBar::chunk {background-color: rgb(0, 170, 255);}")
        progressBar_mana.setValue(40)
        progressBar_mana.setFont(QFont("Segoe UI", 12))
        progressBar_mana.setFormat("%v/%m")
        progressBar_mana.setAlignment(Qt.AlignmentFlag.AlignCenter)
        progress_layout.addWidget(progressBar_mana)
        #stamina
        progressBar_stamina = QProgressBar(self)
        progressBar_stamina.setStyleSheet("QProgressBar::chunk {background-color: rgb(255, 170, 0);}")
        progressBar_stamina.setValue(60)
        progressBar_stamina.setFont(QFont("Segoe UI", 12))
        progressBar_stamina.setFormat("%v/%m")
        progressBar_stamina.setAlignment(Qt.AlignmentFlag.AlignCenter)
        progress_layout.addWidget(progressBar_stamina)
        
        self.setStyleSheet("border: 1px solid black;")
        


if __name__ == '__main__':
    app = QApplication()
    form = PlayerView()
    form.show()
    exit(app.exec())
