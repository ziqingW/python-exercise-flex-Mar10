import random
import auras
import time

class Character:
    def __init__(self, name, maxhealth, regpower):
        self.name = name
        self.maxhealth = maxhealth
        self.health = self.maxhealth
        self.regpower = regpower
        self.power = self.regpower
        self.critical = 0.1
        self.critical_fold = 2
        self.reghit = 0.9
        self.hit = self.reghit
        self.regdodge = 0.15
        self.dodge = self.regdodge
        self.armor = 0
        self.status = auras.auraNormal
        
    def reset(self):
        self.status.begin = 0
        self.status = auras.auraNormal
        self.hit = self.reghit
        self.dodge = self.regdodge
        self.power = self.regpower

    def aura_checker(self):
        if self.status.name != "normal":
            if self.status.begin == 0:
                self.status.begin = 1
            elif self.status.begin != 0 and self.status.begin < self.status.end:
                self.status.begin += 1
                if self.status.begin == self.status.end:
                    self.reset()
        else:
            pass
     
    def alive(self, player = None):
        return self.health > 0
        
    def get_aura(self, aura, enemy = None):
        self.status = aura
        self.status.begin = 0
        if aura.name == "normal":
            pass
        elif aura.name == "blessed":
            pass
        elif aura.name == "protected":
            self.dodge = 1
        elif aura.name == "enraged":
            self.power += 3
            self.hit -= 0.1
        elif aura.name == "slowed":
            self.hit *= 0.5
        elif aura.name == "corrupted":
            self.power *= 0.75
        elif aura.name == "paralyzed":
            self.dodge = 0
        elif aura.name == "swapped":
            enemy.status = aura
            
    def print_status(self):
        if self.health > self.maxhealth:
            self.health = self.maxhealth
        if self.health < 0:
            self.health = 0
        print("{0} -- Health: {1}/{2}\tPower: {3}\tArmor: {4}\tstatus: {5}".format(self.name.capitalize(), self.health, self.maxhealth, int(self.power), self.armor, self.status.name))
    
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