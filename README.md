# RPG Game

## Parce que j'adore les README.md c'est bien connu

## Setup

### step 0 : Obligatoire

url : <https://wiki.qt.io/Qt_for_Python>

```shell
#python -m venv /path/to/new/virtual/environment
python -m venv env
# Active env on windows
.\env\Scripts\Activate.ps1   
pip install pyside6
```

### step 1 : clone git repo

```shell
git clone https://github.com/Miims03/rpg_game
```

## Play Game

### step 2 : python

```shell
python.exe main.py
```

## ACTUAL STATE

- les classes model :
  - class Item
  - class Inventory
  - class Consumable
  - class Weapon
  - class Armor
  - class Character
  - class Player
  - class Monster
  - class Transaction
  - class Game
  - class combat

- les classes view :
  - class View
  - class Message
  - class ItemView
  - class GameView
  - class InventoryView
  - class PlayerView
  - class MainView

## TODO

- authentication : authentication.py

- hotel des ventes : h_d_v.py

- mini map  : mini_map.py

- plateau jeu : board.py

- class combat : combat.py

- GameView : !!

- MainView : !!!

## IDEA

- Idée indexation : fixée au début par l'algorithme, puis fixée par un joueur élu maître de l'HV par exemple.

- reduction promotion | dans le temps
