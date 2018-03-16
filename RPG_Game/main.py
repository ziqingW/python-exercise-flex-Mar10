import monsters
import hero
import store
import battle
import basic_items
import camp
import random
import time

if __name__ == "__main__":
    hero = hero.Hero("hero", 100, 5)
    goblin = monsters.Goblin("goblin", 16, 2)
    gargoyle = monsters.Medic("gargoyle", 25, 3)
    shadow = monsters.Shadow("shadow", 1, 3)
    ooze = monsters.Slime("acid ooze", 30, 5)
    spider = monsters.Spider("Giant spider", 40, 6)
    zombie = monsters.Undead("zombie", 45, 6)
    ogre = monsters.Ogre("ogre", 120, 10)
    peddler = store.Store()
    encounters_1 = [goblin, gargoyle, shadow]
    encounters_2 = [ooze, spider, zombie]
    boss = [ogre]
    battleEngine = battle.Battlefield()
    campfire = camp.Camp()

def results(player, enemy):
    if player.alive(enemy) and not enemy.alive(player):
        if enemy != boss[0]:
            print("")
            print("You won! The {} is dead.".format(enemy.name))
        else:
            print("")
            print("You won! The {} is dead.".format(enemy.name))
            print("Congratulations! You completed the quest!")
            print("")
            print("Thank you for playing the game!")
            print("")
            exit()
        player.loot(enemy)
        player.reset()
        battleEngine.turn = 1
    elif player.alive(enemy) and enemy.alive(player):
        print("Goodbye. You will be remembered as a coward.")
        exit()
    else:
        if enemy != boss[0]:
            print("You are dead.")
        else:
            print("You died, in honor.")
        print("Game Over")
        print("")
        exit()

def process(encounters):
    for encounter in encounters:
        campfire.explore(hero)
        time.sleep(0.8)
        print("")
        print(encounter)
        print("")
        print("Fight begins!!")
        battleEngine.battle_engine(hero, encounter)
        results(hero, encounter)
        print("")

def main():
    print("*" * 40)
    print("*{0}Welcome to the adventure{0}*".format(" " * 7))
    print("*" * 40)
    print("{0}ver 2.2".format(" " * 30))
    print("")
    print("You are or was once a knight, although what left on you now is only an aged blunt sword.")
    print("An entrance of dungeon emerged in the front darkness of you. From the dark deep, you heard unhuman wailings.")
    print("This is the final chance to reseize your long lost honor. You unsheathed your sword and stepped into the darkness.")
    print("")
    print("-" * 20)
    process(encounters_1)
    campfire.explore(hero)
    print(peddler.description_1())
    peddler.store_engine(hero)
    process(encounters_2)
    campfire.explore(hero)
    print(peddler.description_2())
    peddler.store_engine(hero)
    process(boss)

if __name__ == "__main__":
    main()