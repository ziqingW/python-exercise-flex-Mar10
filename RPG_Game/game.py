import setPath
from goblin import Goblin
from zombie import Zombie
from hero import Hero

player = Hero("hero", 10, 5)
enemy = Zombie("zombie", None, 2)

while enemy.alive() and player.alive():
    player.print_status()
    enemy.print_status()
    print()
    print("What do you want to do?")
    print("1. fight {}".format(enemy.name))
    print("2. do nothing")
    print("3. flee")
    print("> ", end =' ')
    raw_input = input()        
    if raw_input == "1":
        player.attack(enemy)
    elif raw_input == "2":
        pass
    elif raw_input == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid input {}".format(raw_input))
    
    if enemy.alive():
        enemy.attack(player)