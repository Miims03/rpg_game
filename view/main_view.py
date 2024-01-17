import tkinter as tk
from game_view import GameWindow

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python RPG Game")
        self.geometry("250x100")
        self.show_main_layout()

    def handle_submit(self):
        # Méthode appelée lorsqu'on clique sur le bouton "Submit" dans le layout fieldUsername
        # Ajoutez ici le code pour traiter le nom d'utilisateur saisi
        #heuu ben pour l'instant juste si username inférieur à 5 caractère alors j'accepte pas
        if len(self.entry.get())>=5:
            self.show_game_layout()
        else:
            
        

    def show_main_layout(self):
        # Affiche le layout principal
        self.clear_widgets()
        label = tk.Label(self, text="Bienvenue dans RPG Game !")
        # fieldUsername
        label2 = tk.Label(self, text="Username:")
        #self pour la récupéré dans handle_sumbit
        self.entry = tk.Entry(self)
        start_button = tk.Button(self, text="Start", command=self.handle_submit)
        exit_button = tk.Button(self, text="Exit", command=self.destroy)

        label.grid(row=0, column=1,pady=0,padx=10)
        start_button.grid(row=1, column=0,pady=0,padx=0)
        exit_button.grid(row=1, column=1,pady=0,padx=0)
        label2.grid(row=2, column=0, pady=0,padx=0)
        self.entry.grid(row=2, column=1, pady=0,padx=0)
        

    def show_game_layout(self):
        # Affiche le layout du jeu
        self.clear_widgets()
        self.geometry("300x200")
        game_window = GameWindow(self, game=None)
        game_window.pack(fill=tk.BOTH, expand=True)

    def clear_widgets(self):
        # Efface tous les widgets actuellement dans la fenêtre
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()