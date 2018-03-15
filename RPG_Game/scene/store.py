import basic_items

potion = basic_items.Potion("healing potion", 10, 10)
holyoil = basic_items.Holyoil("holyoil", 15)
amulet = basic_items.Amulet("amulet", 50)
leather = basic_items.Armor("leather armor", 20, 1)
plate = basic_items.Armor("plate armor", 45, 2)
steelSword = basic_items.Weapon("steel sword", 20, 2)
bastardSword = basic_items.Weapon("bastard sword", 50, 4)
evadeRing = basic_items.Ring("evade ring", 50, "evade")
criticalRing = basic_items.Ring("cri ring", 50, "critical")
stuffs = [potion, holyoil, amulet, leather, plate, steelSword, bastardSword, evadeRing, criticalRing]

class Store:
    def __init__(self):
        self.storage = stuffs
    
    def __str__(self):
        return "About five yards in front of you, the dim flame in a lantern throbbed as will die out anytime. \nA hag behind the light and grinned to you. \"Any spare coin? I have many good stuff for you.\""
    
    def store_engine(self, player):
        print(self.__str__())
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
                    print("{}. {} -- {} coins".format(i+1, stuffs[i].name, stuffs[i].price))
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
                        print("{}. {}".format(i+1, allitems[i].name))
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
        if player.coin > item.price:
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
    