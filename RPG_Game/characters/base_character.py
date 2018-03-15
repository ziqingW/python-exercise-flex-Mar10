import random

class Character:
    
    def __init__(self, name, maxhealth, regpower):
        self.name = name
        self.maxhealth = maxhealth
        self.health = self.maxhealth
        self.regpower = regpower
        self.power = self.regpower
        self.critical = 0
        self.critical_fold = 2
        self.reghit = 0.85
        self.hit = self.reghit
        self.regdodge = 0.15
        self.dodge = self.regdodge
        self.armor = 0
        self.status = "normal"
        
    def alive(self, player = None):
        return self.health > 0
            
    def print_status(self):
        if self.health > self.maxhealth:
            self.health = self.maxhealth
        if self.health < 0:
            self.health = 0
        print("{0} -- Health: {1}/{2}\t\tPower: {3}\t\tstatus: {4}".format(self.name.capitalize(), self.health, self.maxhealth, int(self.power), self.status))
    
    def hitin(self, enemy):
        return random.random() <= self.hit * (1 - enemy.dodge)
    
    def critical_attack(self):
        return random.random() <= self.critical
             
    def attack(self, enemy):
        if self.hitin(enemy):
            damage = int(self.power - enemy.armor)
            crAttack = ""
            if self.critical_attack():
                damage = int(self.power * self.critical_fold - enemy.armor)
                crAttack = "It's a critical attack!"
            enemy.health -= damage
            if self.name == "hero":
                print("You did {} damage to the {}. {}".format(damage, enemy.name, crAttack))
            else:
                print("The {} did {} damage to you. {}".format(self.name, damage, crAttack))
        else:
            if self.name == "hero":
                print("You swung the sword to {}, but missed!".format(enemy.name))
            else:
                print("The {} tried to hit you, you agilely evaded it!".format(self.name))