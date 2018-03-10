class Character:
    
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False    
    
    def print_status(self):
        if self.name == "hero":
            print("You have {} health and {} power.".format(self.health, self.power))
        else:
            if self.health == None:
                print("The {} is undead, has no health point and {} power.".format(self.name, self.power))
            else:
                print("The {} has {} health and {} power.".format(self.name, self.health, self.power))
    
    def attack(self, enemy):
        if enemy.health != None:
            enemy.health -= self.power
        if self.name == "hero":
            print("You did {} damage to the {}.".format(self.power, enemy.name))
            if not enemy.alive():
                print("The {} is dead.".format(enemy.name))
        else:
            print("The {} did {} damage to you.".format(self.name, self.power))
            if not enemy.alive():
                print("You are dead.")
            
            
class Hero(Character):
    pass

class Goblin(Character):
    pass

class Zombie(Character):
    def alive(self):
        return True
        
player = Hero("hero", 10, 5)
enemy = Zombie("zombie", None, 2)

while enemy.alive() and player.alive():
    player.print_status()
    enemy.print_status()
    print()
    print("What do you want to do?")
    print("1. fight {}".format(enemy.name))
    print("2. do nothing")
    print("3. flee")
    print("> ", end =' ')
    raw_input = input()        
    if raw_input == "1":
        player.attack(enemy)
    elif raw_input == "2":
        pass
    elif raw_input == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid input {}".format(raw_input))
    
    if enemy.alive():
        enemy.attack(player)