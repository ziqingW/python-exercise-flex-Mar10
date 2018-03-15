class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.equippable = False
        self.number = 0
        self.usable = True

# consumables
class Potion(Item):
    def __init__(self, name, price, heal):
        super().__init__(name, price)
        self.heal = heal
            
class Holyoil(Item):
    pass

class Amulet(Item):
    pass

class Weapon(Item):
    def __init__(self, name, price, dmg):
        super().__init__(name, price)
        self.equippable = True
        self.usable = False
        self.equiplimit = 1
        self.dmg = dmg
        self.equipnum = 0

class Armor(Item):
    def __init__(self, name, price, armor_class):
        super().__init__(name, price)
        self.equippable = True
        self.usable = False
        self.equiplimit = 1
        self.armor_class = armor_class
        self.equipnum = 0
        
class Ring(Item):
    def __init__(self, name, price, effect):
        super().__init__(name, price)
        self.equippable = True
        self.usable = False
        self.equiplimit = 2
        self.equipnum = 0
        self.effect = effect