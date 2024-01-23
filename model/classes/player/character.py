from enum import Enum

class CharacterRole(Enum):
    
    PLAYER = 0,
    PNJ = 1,
    MONSTER = 2
    
class Character():
    
    def __init__(self,name="character_PNJ", role = CharacterRole.PNJ):
        self.name = name    
        self.role = role
        self.lvl = 1