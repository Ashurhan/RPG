from abc import ABC, abstractmethod


class Potion(ABC):
    def __init__(self,name,description):
        self.name=name
        self.description=description

    @abstractmethod
    def use(self):
        pass

    def __str__(self):
        return f"{self.name}-{self.description}"
    
class HealPotion(Potion):
    def __init__(self,name,description):
        super().__init__(name,description)

    def use(self,other):
        other.health+=50
        print(f"{other.name}  выпил зелье здоровья")

class DamagePotion(Potion):
    def __init__(self,name,description):
        super().__init__(name,description)

    def atack(slef,other):
        other.damage+=15
        print(f"{other.name} выпил зелье урона")
