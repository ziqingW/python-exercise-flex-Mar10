from base_character import Character
import basic_items

class Hero(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.critical = 0.2
        self.regdodge = 0.2
        self.armor = 1
        self.coin = 200
        self.inventory = []
        self.equipitems = []
        self.currentEquip = []

    def loot(self, enemy):
        self.coin += enemy.bounty
        print("You found {} coins from the body of {}.".format(enemy.bounty, enemy.name))
    
    def inventory_add(self, item):
        self.inventory.append(item)
        item.number += 1
    
    def inventory_del(self, item):
        self.inventory.remove(item)
        item.number -= 1
        
    def equipitems_add(self, item):
        self.equipitems.append(item)
        item.number += 1
    
    def equipitems_del(self, item):
        self.equipitems.remove(item)
        item.number -= 1
        
    def use(self, item):
        if item.number > 0:
            if isinstance(item, basic_items.Potion):
                if self.health == self.maxhealth:
                    print("Your health is full, no need to heal.")
                else:
                    self.health += item.heal
                    self.inventory_del(item)
                    if self.health > self.maxhealth:
                        self.health = self.maxhealth
                    print("You drank one bottle of {}, feeling saved. \n(health + {}, health: {}/{})".format(item.name, item.heal, self.health, self.maxhealth))
            elif isinstance(item, basic_items.Holyoil):
                self.status = "blessed"
                self.inventory_del(item)
                print("You oilded your weapon with {}, it can hurt the undeads now!".format(item.name))
            elif isinstance(item, basic_items.Amulet):
                self.status = "protected"
                self.dodge = 1
                self.inventory_del(item)
                print("You crushed the amulet in your hand, from which a pure white aura flowing out and clad you. \nYou are immune to any damage and negative effect for 3 turns!")
        else:
            print("You don't have any {} left.".format(item.name))
            
    def equip(self, item):
        if item.equipnum < item.equiplimit:
            item.equipnum += 1
            self.equipitems_del(item)
            info = ""
            if isinstance(item, basic_items.Weapon):
                info = "(+{} power)".format(item.dmg)
                self.regpower += item.dmg
                self.power = self.regpower
            elif isinstance(item, basic_items.Armor):
                info = "(+{} armor)".format(item.armor_class)
                self.armor += item.armor_class
            elif isinstance(item, basic_items.Ring):
                if item.effect == "evade":
                    self.regdodge += 0.2
                    self.dodge = self.regdodge
                    info = " (+20% dodge)"
                elif item.effect == "critical":
                    self.critical += 0.1
                    info = " (+10% critical rate)"
            self.currentEquip.append(item)
            print("You equipped the {}{}.".format(item.name, info))
        else:
            print("You can't equip more.")
    
    def unequip(self, item):
        if item.equipnum > 0:
            item.equipnum -= 1
            self.equipitems_add(item)
            info = ""
            if isinstance(item, basic_items.Weapon):
                info = "(- {} power)".format(item.dmg)
                self.power -= item.dmg
            elif isinstance(item, basic_items.Armor):
                info = "(- {} armor)".format(item.armor_class)
                self.armor -= item.armor_class
            elif isinstance(item, basic_items.Ring):
                if item.effect == "evade":
                    self.dodge -= 0.2
                    info = " (-20% dodge)"
                elif item.effect == "critical":
                    self.critical -= 0.1
                    info = " (-10% critical rate)"
            self.currentEquip.remove(item)
            print("You unequipped the {}{}.".format(item.name, info))
        else:
            print("You haven't equipped it yet.")        