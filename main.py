from characters import Knigt , Withard , Tank
from monsters import Orc , OrcDoctor, BigOrc
from items import HealPotion , DamagePotion


class Game:
    def __init__(self,player , monsters):
        self.player=player
        self.monsters=monsters
    
    def game_over(self):
        if self.player.lives < 0:
            return True
        return False

    def win_game(self):
        if len(self.monsters) ==0:
            return True
        return False
    
    def add_monsters(self, monster):
        if isinstance(monster , (Orc, OrcDoctor,BigOrc)):
            self.monsters.append(monster)
        else:
            print("Ошибка можно лишь добавить монстра")

    def remove_monster(self, monster):
        if monster.health < 0:
            self.monsters.remove(monster)
    

def main():
    characters= int(input("""
    Выберите героя:
    1-Рыцарь
    2-Волшебник
    3-Танк
"""))        
    
    name=input("Назовите героя")

    if characters==1:
        player=Knigt(name)
    elif characters==2:
        player=Withard(name)
    elif characters ==3:
        player=Tank(name)

    game=Game(player, [Orc("Usual Orc") , OrcDoctor("Orc doctor") , BigOrc("Big orc")])


    def start():
        print(f"{player.name} отправился в опасное путешествие ")
        while True:
            monster=game.monsters[-1]
            print(f"{player.name}  встретил {monster} ! Началось опасное битва")
            while player.health > 0 or monster.health > 0:
                player.atack(monster)
                if monster.health <= 0:
                    monster.die()
                    game.remove_monster(monster)
                    break
                else:
                    monster.atack(player)
                    if player.health <=0:
                        player.die()
                        print(f"{player.name}  возродился остаток жизни {player.lives}")
                        if game.game_over():
                            print(f"{player.name} проиграл")
            print(player.__dict__)
            if game.win_game():
                print(f"{player.name} выиграл")
                break
            else:
                print(f"После битвы с монстром у {player.name} осталось {player.health}")
        

    start()
main()


    
        
