class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.equippable = False
        self.number = 0
        self.usable = True
    
    def descript(self):
        return ""

# consumables
class Potion(Item):
    def __init__(self, name, price, heal):
        super().__init__(name, price)
        self.heal = heal
    
    def descript(self):
        return "heal {} health".format(self.heal)
        
class Holyoil(Item):
    def descript(self):
        return "bless weapon"

class Amulet(Item):
    def descript(self):
        return "immune for 3 turns"

class Wand(Item):
    def descript(self):
        return "swap power with enemy"
    
class Weapon(Item):
    def __init__(self, name, price, dmg):
        super().__init__(name, price)
        self.equippable = True
        self.usable = False
        self.equiplimit = 1
        self.dmg = dmg
        self.equipnum = 0
        
    def descript(self):
        return "{} power".format(self.dmg)

class Armor(Item):
    def __init__(self, name, price, armor_class):
        super().__init__(name, price)
        self.equippable = True
        self.usable = False
        self.equiplimit = 1
        self.armor_class = armor_class
        self.equipnum = 0
    
    def descript(self):
        return "{} armor".format(self.armor_class)        

class Ring(Item):
    def __init__(self, name, price, effect):
        super().__init__(name, price)
        self.equippable = True
        self.usable = False
        self.equiplimit = 2
        self.equipnum = 0
        self.effect = effect

    def descript(self):
        return self.effect