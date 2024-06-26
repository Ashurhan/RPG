from abc import ABC , abstractmethod

class Monster(ABC):

    def __init__(self,name,health,damage):
        self.name=name
        self.health=health
        self.damage=damage

    @abstractmethod
    def atack(self,other):
        pass

    @abstractmethod
    def level_up(self):
        pass

    def die(self):
        del self

    
class Orc(Monster):

    def __init__(self,name):
        super().__init__(name,100,50)

    
    def atack(self,other):
        other.health-=self.damage
        if other.health <=0:
            other.die()
            print(f"{self.name} убил {other.name}")
        else:
            print(f"{self.name} ударил {other.name}")
    
    def level_up(self):
        self.damage+=10
        print("Монстер стал сильнее")
    
    def __str__(self):
        return f"""
        Name:{self.name}
        Health:{self.health}
        Damage:{self.damage}
        """


class OrcDoctor(Monster):
    def __init__(self,name):
        super().__init__(name, 100,0)
        self.magic=20
    
    def atack(self, other):
        print("Доктор не может атаковать")

    def level_up(self):
        self.magic+=10
        print("Орк доктор повысил урон магии")

    def heal(self,other):
        other.health+=self.magic
        print(f"{self.name} вылечил {other.name}")

    
    def __str__(self):
        return f"""
        Name:{self.name}
        Health:{self.health}
        Damage:{self.damage}
        Magic:{self.magic}
        """

class BigOrc(Orc):
    def __init__(self,name):
        super().__init__(name)