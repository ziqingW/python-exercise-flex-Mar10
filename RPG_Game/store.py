import basic_items

potion = basic_items.Potion("healing potion", 15, 15)
holyoil = basic_items.Holyoil("holy oil", 12)
amulet = basic_items.Amulet("amulet", 50)
leather = basic_items.Armor("leather armor", 30, 2)
longSword = basic_items.Weapon("long sword", 32, 2)
evadeRing = basic_items.Ring("evade ring", 50, "20% dodge")
criticalRing = basic_items.Ring("critical ring", 50, "10% critical")
swapWand = basic_items.Wand("swap wand", 50)
stuffs = [potion, holyoil, amulet, leather, longSword, evadeRing, criticalRing, swapWand]

class Store:
    def __init__(self):
        self.storage = stuffs
    
    def description_1(self):
        print("")
        return "About five yards in front of you, the bleak flare from a lantern throbbed as it would die out at anytime. \nA humped crone behind the light grinned to you. \"Any spare coin? I have so many shining things for you.\""
    
    def description_2(self):
        print("")
        return "You saw the same crone emerged ahead with the same appearance. She grinned to you again:\"Wanna see something good?\"\nAre they just twins?"
        
    def store_engine(self, player):
        while True:
            print("")
            print("What do you want to do? ")
            print("*" * 20)
            print("1. Buy")
            print("2. Sell")
            print("3. Leave")
            print("*" * 20)
            print("Your coins: {}".format(player.coin))
            print("-" * 20)
            answer = input("> ")
            if answer == "1":
                print("-" * 20)
                print("What do you want to buy?")
                for i in range(len(self.storage)):
                    print("{}. {} -- {} coins -- {}".format(i+1, stuffs[i].name.capitalize(), stuffs[i].price, stuffs[i].descript()))
                print("")
                print("0. Back")
                print("Your coins: {}".format(player.coin))
                print("-" * 20)
                while True:
                    try:
                        answer = int(input("You want to buy > "))
                    except:
                        print("Invalid input.")
                    else:
                        if answer not in range(1, len(stuffs) + 1) and not answer == 0:
                                continue
                        else:
                            if answer != 0:
                                self.buy(player, stuffs[answer-1])
                            break
            elif answer == "2":
                print("")
                allitems = player.inventory + player.equipitems
                if allitems != []:
                    print("What do you want to sell?")
                    print("=" * 20)
                    for i in range(len(allitems)):
                        print("{}. {} -- {}coins  {}".format(i+1, allitems[i].name.capitalize(), allitems[i].price, allitems[i].descript()))
                    print("")
                    print("0. Back")
                    print("=" * 20)
                    print("Your coins: {}".format(player.coin))
                    while True:
                        try:
                            answer = int(input("You want to sell > "))
                        except:
                            print("Invalid input.")
                        else:
                            if answer not in range(1, len(allitems) + 1) and not answer == 0:
                                    continue
                            else:
                                if answer != 0:
                                    self.sell(player, allitems[answer-1])
                                break
                else:
                    print("You have nothing to sell.")
            elif answer == "3":
                print("")
                print("You ignored the peddler and started to leave. When you passed the hag, she bursted a hysterical laugh.")
                print("")
                print("")
                break
            else:
                print("Invalid input")
                    
    def sell(self, player, item):
        if item.usable:
            player.inventory_del(item)
        else:
            player.equipitems_del(item)
        player.coin += item.price
        print("")
        print("You sold {}, get {} coins back.".format(item.name, item.price))
        
    def buy(self, player, item):
        if player.coin >= item.price:
            if item.usable:
                player.inventory_add(item)
            else:
                player.equipitems_add(item)
            player.coin -= item.price
            print("")
            print("You bought {}, spent {} coins out.".format(item.name, item.price))
        else:
            print("")
            print("You don't have enough money.")
    