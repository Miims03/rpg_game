from abc import ABC , abstractmethod



class Skill(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def use(self, *targets):
        # Logique de l'utilisation de la compétence
        print('shoud be ovverride')


class Fireball(Skill):
    def __init__(self):
        super().__init__("Fireball", "Launches a fiery projectile.")

    def use(self, *targets):
        # Logique spécifique de Fireball
        print(f"{self.name} used on {targets}!")

class Heal(Skill):
    def __init__(self):
        super().__init__("Heal", "Restores health.")

    def use(self, *targets):
        # Logique spécifique de Heal
        print(f"{self.name} used on {targets}!")