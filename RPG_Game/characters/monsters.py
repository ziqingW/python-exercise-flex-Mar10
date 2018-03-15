from base_character import Character
import auras
import random

class Goblin(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.bounty = random.randint(8, 10)
    
    def __str__(self):
        return "In front of you stood a ugly humanoid, his small yellow eyes glittered with greedy.\n\"meat...\", you could even smell the ill reek from the goblin's drooling."
        
class Medic(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.regen = 0.2
        self.regdodge = 0.2
        self.dodge = self.regdodge
        self.bounty = random.randint(14, 18)
        self.armor = 1
    
    def regeneration(self):
        if random.random() <= self.regen:
            self.health += 2
            print("The {} healed itself for 2 health!".format(self.name))
    
    def __str__(self):
        return "Once you stepped into the room, a flying mass rushed to you from the left.\nYou barely evaded it and found it was a gargoyle, without eyes.\n** Gargoyle can heal itself each turn by chance."

class Shadow(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.regdodge = 0.9
        self.dodge = self.regdodge
        self.bounty = random.randint(25, 35)
    
    def __str__(self):
        return "You thought there was nothing in the room before you realized it completely wrong as a cloud of shadow solidiying in front of you. \n ** Shadow is fragile, but extremely hard to be hit."

class Slime(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.bounty = random.randint(35, 45)
        self.acid = 0.2
        self.armor = 1

    def corrode(self, enemy):
        if random.random() <= self.acid:
            enemy.get_aura(auras.auraCorrupted)
            print("The green ooze's soft body was strongly acidic, your weapon was corroded! (power decreases)")
            
    def __str__(self):
        return "You saw a huge fluorescent body before you. Countless bubbles popped on and off inside it.\nYou poked it with the sword tip, which disturblingly sizzled."
            
class Spider(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.bounty = random.randint(40, 50)
        self.slow = 0.3
        self.regdodge = 0.2
        self.dodge = self.regdodge
    
    def web(self, enemy):
        if random.random() <= self.slow:
            enemy.get_aura(auras.auraSlowed)
            print("The giant spider spurt a sticky web on you, your movement is slowed! (hit rate decreases)")
    
    def __str__(self):
        return "One monstrous spider suddenly dropped from nowhere before you.\n\"I can handle it with ease.\" \nYou thought so before noticing something sticky restrained your move."
        
class Undead(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.bounty = random.randint(46, 52)
        self.armor = 1
        self.reghit = 0.7
        self.hit = self.reghit
    
    def alive(self, player):
        if player.status.name != "blessed":
            return True
        else:
            return self.health > -1
    
    def __str__(self):
        return "A staggering animated corpse tried to get close to you from not far away. From the shattered armor on it you knew it was one of you once. \n** Undead can only be killed by blessed weapon."
        
class Ogre(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.bounty = 300
        self.reghit = 0.7
        self.critical = 0.2
        self.hit = self.reghit
        self.armor = 3
    
    def roar(self):
        if random.random() <= 0.25:
            self.get_aura(auras.auraEnraged)
            print("Ogre made a deafening roar, its attacks become more deadly! (power + 3)")
    
    def stomp(self, enemy):
        if self.health <= self.maxhealth * 0.5 and random.random() <= 1/3:
            print("Ogre made a heavy stomp in rage!")
            if self.hitin(enemy):
                print("You are paralyzed by the shockwave!")
                enemy.get_aura(auras.auraParalyzed)
            else:
                print("You evaded the shockwave!")
                
    def __str__(self):
        return "You saw a strong light shining ahead. An exit to the outer?! \nYou couldn't hold yourself but rushing towards the light. The earth suddenly began vigorously shaking in the middle of your sprint. \nYou stopped and squat, nearly deafened by a following growl. \nAfter you stood again, you saw that angry thing before you. It's a Ogre!"