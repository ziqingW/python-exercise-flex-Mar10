import monsters
from auras import Aura
import time

class Battlefield:
    def __init__(self):
        self.turn = 1
        self.battleOption = ""
    
    def battle_playerAct(self, player, enemy):
        while True:
            print("=" * 20)
            print("Turn {}".format(self.turn))
            player.print_status()
            enemy.print_status()
            print("")
            print("What do you want to do?")
            print("1. Fight {}".format(enemy.name))
            print("2. Use item")
            print("3. Do nothing")
            print("4. Flee")
            print("-" * 20)
            self.battleOption = input("> ")
            print("-" * 20)
            if self.battleOption == "1":
                break
            elif self.battleOption == "2":
                if len(player.inventory) > 0:
                    print("Which item do you want to use?")
                    for i in range(len(player.inventory)):
                        print("{}. {} -- {}".format(i+1, player.inventory[i].name.capitalize(), player.inventory[i].descript()))
                    print("")
                    print("0. Back")
                    print("-" * 20)
                    while True:
                        try:
                            answer = int(input("> "))
                        except:
                            print("Invalid input.")
                        else:
                            if answer not in range(1, len(player.inventory) + 1) and not answer == 0:
                                continue
                            else:
                                if answer != 0:
                                    print("-" * 20)
                                    player.use(player.inventory[answer - 1], enemy)
                                break
                else:
                    print("You have no usable item.")
                    continue
            elif self.battleOption == "3":
                break
            elif self.battleOption == "4":
                break
            else:
                print("Invalid input {}".format(self.battleOption))
                continue
            
    def battle_monsterAct(self, player, enemy): 
        time.sleep(0.3)
        if enemy.alive(player):
            if isinstance(enemy, monsters.Spider):
                enemy.web(player)
            elif isinstance(enemy, monsters.Medic):
                enemy.regeneration()
            elif isinstance(enemy, monsters.Slime):
                enemy.corrode(player)
            elif isinstance(enemy, monsters.Ogre):
                enemy.roar()
                enemy.stomp(player)
            enemy.attack(player)
            
    def battle_engine(self, player, enemy):
        while player.alive(enemy) and enemy.alive(player):
            time.sleep(0.3)
            if player.status.name != "paralyzed":
                self.battle_playerAct(player, enemy)
                if self.battleOption == "1":
                    player.attack(enemy)
                elif self.battleOption == "3":
                    pass
                elif self.battleOption == "4":
                    break
            else:
                print("=" * 20)
                print("Turn {}".format(self.turn))
                player.print_status()
                enemy.print_status()
                print("You are paralyzed, skip one turn.")
            self.battle_monsterAct(player, enemy)
            player.aura_checker()
            enemy.aura_checker()
            if player.status.name == "swapped":
                player.reset()
                enemy.reset()
            self.turn += 1