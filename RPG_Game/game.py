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
            print("The {} has {} health and {} power.".format(self.name, self.health, self.power))
    
    def attack(self, enemy):
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

hero = Hero("hero", 10, 5)
goblin = Goblin("goblin", 6, 2)

while goblin.alive() and hero.alive():
    hero.print_status()
    goblin.print_status()
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ", end =' ')
    raw_input = input()        
    if raw_input == "1":
        hero.attack(goblin)
    elif raw_input == "2":
        pass
    elif raw_input == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid input {}".format(raw_input))
    
    if goblin.alive():
        goblin.attack(hero)