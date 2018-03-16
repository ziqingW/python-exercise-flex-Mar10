from base_character import Character
import auras
import basic_items
import time
import store

class Hero(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        self.critical = 0.2
        self.regdodge = 0.2
        self.dodge = self.regdodge
        self.armor = 1
        self.coin = 50
        self.inventory = []
        for i in range(3):
            self.inventory_add(store.potion)
        self.inventory_add(store.holyoil)
        self.equipitems = []
        self.currentEquip = []

    def loot(self, enemy):
        self.coin += enemy.bounty
        print("You found {} coins from the body of {}.".format(enemy.bounty, enemy.name))
        print("=" * 40)
    
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
        
    def use(self, item, enemy = None):
        if item.number > 0:
            if isinstance(item, basic_items.Potion):
                if self.health == self.maxhealth:
                    print("Your health is full, no need to heal.")
                else:
                    self.health += item.heal
                    self.inventory_del(item)
                    if self.health > self.maxhealth:
                        self.health = self.maxhealth
                        time.sleep(0.3)
                    print("You drank one bottle of {}, feeling saved. \n(health + {}, health: {}/{})".format(item.name, item.heal, self.health, self.maxhealth))
            elif isinstance(item, basic_items.Wand):
                self.get_aura(auras.auraSwapped, enemy)
                self.power, enemy.power = enemy.power, self.power
                self.inventory_del(item)
                print("You took out the swap wand and pointed to the {}, the wand vibrated in your hand. \nYou felt a stream of strange power flowing into you.".format(enemy.name))
                time.sleep(0.3)
                print("You switched power with the {} for 1 turn.".format(enemy.name))
            elif isinstance(item, basic_items.Holyoil):
                self.get_aura(auras.auraBlessed)
                self.inventory_del(item)
                time.sleep(0.3)
                print("You oilded your weapon with {}, it can hurt the undeads now!".format(item.name))
            elif isinstance(item, basic_items.Amulet):
                self.get_aura(auras.auraProtected)
                self.inventory_del(item)
                time.sleep(0.3)
                print("You crushed the amulet in your hand, from which a pure white aura flowing out and clad you. \nYou are immune to any damage and negative effect for 3 turns!")
        else:
            print("You don't have any {} left.".format(item.name))
            
    def equip(self, item):
        if item.equipnum < item.equiplimit:
            item.equipnum += 1
            self.equipitems_del(item)
            info = "(+{})".format(item.descript())
            if isinstance(item, basic_items.Weapon):
                self.regpower += item.dmg
                self.power = self.regpower
            elif isinstance(item, basic_items.Armor):
                self.armor += item.armor_class
            elif isinstance(item, basic_items.Ring):
                if item.effect == "20% dodge":
                    self.regdodge += 0.2
                    self.dodge = self.regdodge
                elif item.effect == "10% critical":
                    self.critical += 0.1
            self.currentEquip.append(item)
            time.sleep(0.3)
            print("You equipped the {}{}.".format(item.name, info))
        else:
            print("You can't equip more.")
    
    def unequip(self, item):
        if item.equipnum > 0:
            item.equipnum -= 1
            self.equipitems_add(item)
            info = "(-{})".format(item.descript())
            if isinstance(item, basic_items.Weapon):
                self.regpower -= item.dmg
                self.power = self.regpower
            elif isinstance(item, basic_items.Armor):
                self.armor -= item.armor_class
            elif isinstance(item, basic_items.Ring):
                if item.effect == "20% dodge":
                    self.regdodge -= 0.2
                    self.dodge = self.regdodge
                elif item.effect == "10% critical":
                    self.critical -= 0.1
            self.currentEquip.remove(item)
            time.sleep(0.3)
            print("You unequipped the {}{}.".format(item.name, info))
        else:
            print("You haven't equipped it yet.")        