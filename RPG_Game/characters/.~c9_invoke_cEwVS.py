from base_character import Character
import random

class Goblin(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.bounty = 10
        self.regdodge = 0.1
    
    def __str__(self):
        return "In front of you stood a ugly humanoid, his small yellow eyes glitter with greedy.\n\"meat...\", you can smell the ill reek from the goblin's drooling."
        
class Medic(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.regen = 0.2
        self.bounty = 15
        self.regdodge = 0.1
    
    def regeneration(self):
        if random.random() <= self.regen:
            self.health += 2
            print("The {} healed itself for 2 health!".format(self.name))
    
    def __str__(self):
        return "Once you stepped into the room, a grey mass rushed to you from the left.\nYou barely evaded it and found it was a gargoyle, without eyes."

class Shadow(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.regdodge = 0.9
        self.bounty = 30
    
    def __str__(self):
        return "At first you thought there was nothing in the room, when you realized it completely wrong as a cloud of shadow solidiying before you."

class Slime(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.bounty = 35
        self.acid = 0.2

    def corrode(self, enemy):
        if random.random() <= self.acid:
            enemy.power *= 0.75
            enemy.status = "corrupted"
            print("The green slime's gelly body is strongly acidic, your weapon is corroded! (power decreases)")
            
    def __str__(self):
        return "\"It's not a mucus!\" You gripped your weapon in horror as the sword tip sizzling."
            
class Spider(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.bounty = 50
        self.slow = 0.3
        self.regdodge = 0.3
    
    def web(self, enemy):
        if random.random() <= self.slow:
            enemy.hit *= 0.1
            enemy.status = "slowed"
            print("The giant spider spurt a sticky web on you, your movement is slowed! (hit rate decreases)")
    
    def __str__(self):
        return "One giant fat spider dropped in front you.\n\"I can handle it with ease.\" \nYou thought so before noticing something sticky restrained your move."
        
class Undead(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.bounty = 48
    
    def alive(self, player):
        if player.status != "blessed":
            return True
        else:
            return self.health > -1
    
    def __str__(self):
        return "\"Aha, just another zombie!\" You released when you found out the approaching thing as an animated corpse.\nYou were humming while trying to reach your backpack. \nSuddenly your hand froze. \"The holyoil, didn't I use the last one five minutes ago?\""
        
class Minotaur(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.bounty = 300
        self.reghit = 0.8
        self.armor = 3
    
    def roar(self):
        if random.random() <= 0.3:
            self.power += 3
            print("Minotaur made a deafening roar, its attacks become more deadly! (power + 3)")
    
    def stomp(self, enemy):
        if self.health <= self.maxhealth * 0.5 and random.random() <= 1/3:
            print("Minotaur made a heavy stomp in rage!")
            if self.hitin(enemy):
                print("You are paralyzed by the shockwave!")
                enemy.status = "paralyzed"
            else:
                print("You evaded the shockwave!")
                
    def __str__(self):
        return "You saw a strong light shining ahead. An exit to the outer?! \nYou couldn't hold yourself but rushing towards the light. The earth suddenly began vigorously shaking in the middle of your sprint. \nYou stopped and squat, nearly deafened by a following growl. \nAfter you stood again, you saw that angry thing before you. It's a Minotaur!"