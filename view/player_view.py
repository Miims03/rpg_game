from PySide6.QtCore import Qt, QMimeData , QSize , QRect 
from PySide6.QtWidgets import QComboBox, QHBoxLayout, QWidget, QProgressBar , QVBoxLayout , QLabel , QApplication , QBoxLayout 
from PySide6.QtGui import QPixmap, QDragEnterEvent, QDropEvent, QMouseEvent, QDrag , QFont , QColor
from model.classes.player.player import Player


PATH_MEAT_LOGO = 'view\\logo\\meat.png'

class PlayerView(QWidget):
    def __init__(self, actor : Player):
        super().__init__()
        self.actor = actor

        self.setFixedSize(QSize(300,180))
        self.setWindowTitle("Actor View")

        self.init_ui()
        
        self.update_progressBar()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        qFont = QFont("Segoe UI", 12)
        qFont.setBold(True)
        horizontal_layout = QHBoxLayout()
        main_layout.addLayout(horizontal_layout)

        # Player Info
        player_layout = QVBoxLayout()
        horizontal_layout.addLayout(player_layout)
        #name
        self.label_playername = QLabel(self.actor.name, self)
        self.label_playername.setFont(qFont)
        self.label_playername.setAlignment(Qt.AlignmentFlag.AlignCenter)
        player_layout.addWidget(self.label_playername)
        #image
        self.label_logo_player = QLabel("ICON", self)
        self.label_logo_player.setFixedSize(QSize(100,100))
        #label_logo_player.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_logo_player.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
        self.image = QPixmap(PATH_MEAT_LOGO)
        self.label_logo_player.setPixmap(self.image)
        
        player_layout.addWidget(self.label_logo_player)
        #lvl
        self.label_lvl = QLabel('lvl '+str(self.actor.lvl), self)
        self.label_lvl.setFont(qFont)
        self.label_lvl.font().setBold(True)
        self.label_lvl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        player_layout.addWidget(self.label_lvl)

        # Progress Bars
        progress_layout = QVBoxLayout()
        horizontal_layout.addLayout(progress_layout)
        #pv
        self.progressBar_pv = QProgressBar(self)
        self.progressBar_pv.setStyleSheet("QProgressBar::chunk {background-color: rgb(0, 170, 0);}")
        self.progressBar_pv.setMaximum(100)
        self.progressBar_pv.setValue(50)
        self.progressBar_pv.setFont(qFont)
        
        self.progressBar_pv.setFormat("%v/%m")
        self.progressBar_pv.setAlignment(Qt.AlignmentFlag.AlignCenter)
        progress_layout.addWidget(self.progressBar_pv)
        #mana
        self.progressBar_mana = QProgressBar(self)
        self.progressBar_mana.setStyleSheet("QProgressBar::chunk {background-color: rgb(0, 170, 255);}")
        self.progressBar_mana.setMaximum(100)
        self.progressBar_mana.setValue(50)
        self.progressBar_mana.setFont(qFont)
        self.progressBar_mana.setFormat("%v/%m")
        self.progressBar_mana.setAlignment(Qt.AlignmentFlag.AlignCenter)
        progress_layout.addWidget(self.progressBar_mana)
        #stamina
        self.progressBar_stamina = QProgressBar(self)
        self.progressBar_stamina.setStyleSheet("QProgressBar::chunk {background-color: rgb(255, 170, 0);}")
        self.progressBar_stamina.setMaximum(100)
        self.progressBar_stamina.setValue(50)
        self.progressBar_stamina.setFont(qFont)
        self.progressBar_stamina.setFormat("%v/%m")
        self.progressBar_stamina.setAlignment(Qt.AlignmentFlag.AlignCenter)
        progress_layout.addWidget(self.progressBar_stamina)
        
        
        self.setStyleSheet("border: 1px solid black;")
        
    def update_progressBar(self):
        #pv
        self.progressBar_pv.setMaximum(self.actor.pv_max)
        self.progressBar_pv.setValue(self.actor.pv)
        #mana
        self.progressBar_mana.setMaximum(self.actor.mana_max)
        self.progressBar_mana.setValue(self.actor.mana)
        #stamina
        self.progressBar_stamina.setMaximum(self.actor.stamina_max)
        self.progressBar_stamina.setValue(self.actor.stamina)