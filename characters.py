
from abc import ABC, abstractmethod

class Characters(ABC):
    def __init__(self,name,health,damage):
        self.name=name
        self.health=health
        self.max_health=health
        self.damage=damage
        self.level=0
        self.lives=5
        self.inventory=[]

    @abstractmethod
    def atack(self):
        pass

    @abstractmethod
    def level_up(self):
        pass
    
    def use_potion(self, potion):
        if potion in self.inventory:
            potion.use(self)
            self.inventory.remove(potion)
        else:
            print("Нет в наличии")
    
    def add_potion(self , potion):
        self.inventory.append(potion)

    def die(self):
        self.lives-=1


    def __str__(self):
        return f"""
        Name:{self.name}
        Level:{self.level}
        Damage:{self.damage}
        Health:{self.health}
        """
    
class Knigt(Characters):
    def __init__(self,name):
        super().__init__(name, 100 , 30)
   
        
    def atack(self,other):
        other.health-=self.damage
        if other.health <=0:
            other.die()
            print(f"{self.name} убил {other.name}")
        else:
            print(f"{self.name} ударил {other.name}")
    
    def level_up(self):
        self.level+=1
        self.damage+=15
        self.max_health+=50
        self.health=self.max_health
        print("Боец повысил уровень")
    
class Withard(Characters):
    def __init__(self,name):
        super().__init__(name,80,80)

    def atack(self,other):
        other.health-=self.damage
        if other.health <=0:
            other.die()
            print(f"{self.name} убил {other.name}")
        else:
            print(f"{self.name} ударил {other.name}")
    

    def level_up(self):
        self.level+=1
        self.damage+=5
        self.max_health+=20
        self.health=self.max_health
        print("Лучник повысил уровень")


class Tank(Characters):
    def __init__(self,name):
        super().__init__(name,200,100)

    def atack(self,other):
        other.health-=self.damage
        if other.health <=0:
            other.die()
            print(f"{self.name} убил {other.name}")
        else:
            print(f"{self.name} ударил {other.name}")

    def level_up(self):
        self.level+=1
        self.damage+=10
        self.max_health+=75
        self.health=self.max_health
        print("Танк повысил уровень")

        