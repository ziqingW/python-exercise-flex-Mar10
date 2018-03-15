import monsters

class Battlefield:
    def __init__(self):
        self.turn = 1
        self.buff_begin = 0
        self.buff_end = 0
        self.debuff_begin = 0
        self.debuff_end = 0
        self.battleOption = ""
        self.bufflist = ["blessed", "protected"]
        self.debufflist = ["paralyzed", "slowed", "corrupted"]
        
    def reset(self, player):
        player.status = "normal"
        self.buff_begin = 0
        self.buff_end = 0
        self.debuff_begin = 0
        self.debuff_end = 0
        self.battleOption = ""
        player.hit = player.reghit
        player.dodge = player.regdodge
        player.power = player.regpower
        
    def buff_checker(self, player):
        if player.status in self.bufflist and self.buff_begin == 0:
            self.buff_begin = self.turn
            self.buff_end = self.buff_begin + 3
        elif self.buff_begin != 0 and self.buff_begin < self.buff_end:
            self.buff_begin += 1
        elif self.buff_begin !=0 and self.buff_end !=0 and self.buff_begin == self.buff_end:
            self.reset(player)
        else:
            pass

    def debuff_checker(self, player):
        if player.status in self.debufflist and self.debuff_begin == 0:
            self.debuff_begin = self.turn
            self.debuff_end = self.debuff_begin + 1
        elif self.debuff_begin != 0 and self.debuff_begin < self.debuff_end:
            self.debuff_begin += 1
        elif self.debuff_begin !=0 and self.debuff_end !=0 and self.debuff_begin == self.debuff_end:
            self.reset(player)
        else:
            pass    
    
    def battle_playerAct(self, player, enemy):
        while True:
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
                        print("{}. {}".format(i+1, player.inventory[i].name))
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
                                    player.use(player.inventory[answer - 1])
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
        if enemy.alive(player):
            if isinstance(enemy, monsters.Spider):
                enemy.web(player)
            elif isinstance(enemy, monsters.Medic):
                enemy.regeneration()
            elif isinstance(enemy, monsters.Slime):
                enemy.corrode(player)
            elif isinstance(enemy, monsters.Minotaur):
                enemy.roar()
                enemy.stomp(player)
            enemy.attack(player)
            
    def battle_engine(self, player, enemy):
        while player.alive(enemy) and enemy.alive(player):
            self.buff_checker(player)
            self.debuff_checker(player)
            print("=" * 20)
            print("Turn {}".format(self.turn))
            player.print_status()
            enemy.print_status()
            if player.status != "paralyzed":
                self.battle_playerAct(player, enemy)
                if self.battleOption == "1":
                    player.attack(enemy)
                elif self.battleOption == "3":
                    pass
                elif self.battleOption == "4":
                    break
            else:
                print("You are paralyzed, skip one turn.")
            self.battle_monsterAct(player, enemy)
            self.buff_checker(player)
            self.debuff_checker(player)
            self.turn += 1