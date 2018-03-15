class Camp:
    def explore(self, player, enemy = None):
        while True:
            print("You sat next to the campfire, gazing at the flame. \nYou believed you saw something, but it vanished instantly.")
            print("")
            print("What's your next step?")
            print("1. Go further")
            print("2. Drink potion")
            print("3. Change equipments")
            print("4. Check status")
            print("5. Retire")
            print("-" * 20)
            answer = input("> ")
            if answer == "1":
                print("-" * 20)
                print("Enough rest, you put yourself together and walked into the darkness.")
                break
            elif answer == "2":
                while True:
                    print("-" * 20)
                    potionNumber = 0
                    for item in player.inventory:
                        if item.name == "healing potion":
                            potionNumber = item.number
                            potion = item
                    print("Your Health: {}/{}".format(player.health, player.maxhealth))
                    if potionNumber > 0:
                        if potionNumber == 1:
                            print("You have {} bottle of potion. Drink one?".format(potionNumber))
                        else:
                            print("You have {} bottles of potion. Drink one?".format(potionNumber))
                        print("")
                        drinkPotion= input(("Y/N ? > ")).upper()
                        if drinkPotion == "Y":
                            print("")
                            player.use(potion)
                            print("Your Health: {}/{}".format(player.health, player.maxhealth))
                        elif drinkPotion == "N":
                            break
                        else:
                            print("Invalid input.")
                    else:
                        print("You don't have any potion left.")
                        break
            elif answer == "3":
                while True:
                    print("-" * 20)
                    print("What do you want to do? ")
                    print("")
                    print("1. Equip")
                    print("2. Unequip")
                    print("3. Back")
                    print("")
                    print("-" * 20)
                    option = input("> ")
                    print("")
                    if option == "1":
                        if player.equipitems != []:
                            print("-" * 20)
                            print("Your equipments:")
                            print("")
                            for i in range(len(player.equipitems)):
                                print("{}. {}  {}".format(i+1, player.equipitems[i].name.capitalize(), player.equipitems[i].descript()))
                            print("")
                            print("0. Back")
                            print("-" * 20)
                            while True:
                                try:
                                    answer = int(input("Which one do you want to equip?  >"))
                                except:
                                    print("Invalid input.")
                                else:
                                    if answer not in range(1, len(player.equipitems) + 1) and not answer == 0:
                                        continue
                                    else:
                                        if answer != 0:
                                            player.equip(player.equipitems[answer - 1])
                                        break
                        else:
                            print("You don't have any equippable items.")
                    elif option == "2":
                        if player.currentEquip != []:
                            print("You have equipped:")
                            for j in range(len(player.currentEquip)):
                                print("{}. {}  {}".format(j+1, player.currentEquip[j].name.capitalize(), player.currentEquip[j].descript()))
                            print("")
                            print("0. Back")
                            print("Which one do you want to unequip?")
                            print("-" * 20)
                            while True:
                                try:
                                    answer = int(input("> "))
                                except:
                                    print("Invalid input.")
                                else:
                                    if answer not in range(1, len(player.currentEquip) + 1) and not answer == 0:
                                        continue
                                    else:
                                        if answer != 0:
                                            player.unequip(player.currentEquip[answer - 1])
                                        break                            
                        else:
                            print("You haven't equipped anything.")
                    elif option == "3":
                        break
                    else:
                        print("Invalid input.")
            elif answer == "4":
                print("Your status:")
                print("Health: {}/{} \tPower: {} \tArmor: {}".format(player.health, player.maxhealth, player.power, player.armor))
                for item in player.currentEquip:
                    print("Equipped: {}".format(item.name))
                print("-" * 10)    
                print("Inventory:")
                allitem = player.inventory + player.equipitems
                if allitem == []:
                    print("nothing")
                else:
                    for item in allitem:
                        print(" * {} -- {}".format(item.name.capitalize(), item.descript()))
                print("-" * 10)
                print("Coins: {}".format(player.coin))
                print("")
            elif answer == "5":
                print("Pathetic, you can't even grasp your own fate.")
                print("You died.")
                exit()
            else:
                print("Invalid input")