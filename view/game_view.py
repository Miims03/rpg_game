import tkinter as tk

class GameWindow(tk.Frame):
  
  def __init__(self, master, game='game'):
    super().__init__(master)
    #self.game = game
    self.create_widgets()
    
  def create_widgets(self):
  # Ajoutez ici les widgets spécifiques à GameWindow
    label = tk.Label(self, text="Bienvenue dans le jeu.")
    label.pack(pady=10)
