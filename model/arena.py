

from enum import Enum

class CaseType(Enum):
    WALL=0,
    GRASS=1,
    WATER=2,
    ROCK=3
    


class Arena():
    """Arena
    - il va etre le fameux tableau de combat , comme un echiquier , il reçoi un tableau en paramètre pour spécier une arène, sinon génère en un automatiquement 
    Donc !!
    Il faut : 
    - placer le decors : mur, l'herbe des rochers et des flaque d'eau 
    - placer les joueurs
    - placer les ennemis
    - placer les items si y en a
    - Une fois qu'on a le start du joueur (ou des bref), on peut commencer la bataille, 
    - chaque joueur a son tour peux se déplacer d'un certain nombre de case 
    
    
    """
    #5*5
    def test_plateau(self):
        plateau = [(CaseType.WALL,CaseType.WALL,CaseType.WALL,CaseType.WALL,CaseType.WALL),
                   (CaseType.WALL,CaseType.GRASS,CaseType.GRASS,CaseType.GRASS,CaseType.WALL),
                   (CaseType.WALL,CaseType.GRASS,CaseType.GRASS,CaseType.GRASS,CaseType.WALL),
                   (CaseType.WALL,CaseType.GRASS,CaseType.GRASS,CaseType.GRASS,CaseType.WALL),
                   (CaseType.WALL,CaseType.WALL,CaseType.WALL,CaseType.WALL,CaseType.WALL)]
        return plateau
    
    def __init__(self,plateau=None):
        self.plateau = self.test_plateau()
    
    