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