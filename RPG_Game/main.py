import setPath
import monsters
import hero
import store
import battle
import basic_items
import camp
import random

if __name__ == "__main__":
    hero = hero.Hero("hero", 1000, 10)
    goblin = monsters.Goblin("goblin", 12, 3)
    gargoyle = monsters.Medic("gargoyle", 25, 5)
    shadow = monsters.Shadow("shadow", 1, 8)
    ooze = monsters.Slime("acid ooze", 30, 9)
    spider = monsters.Spider("Giant spider", 40, 11)
    zombie = monsters.Undead("zombie", 40, 10)
    minotaur = monsters.Minotaur("minotaur", 200, 18)
    peddler = store.Store()
    encounters_1 = [ooze] #gargoyle, shadow]
    encounters_2 = [zombie] 
    boss = [minotaur]
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
        battleEngine.reset(player)
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
        exit()

def process(encounters):
    for encounter in encounters:
        campfire.explore(hero)
        print("")
        print(encounter)
        print("")
        print("Fight begins!!")
        battleEngine.battle_engine(hero, encounter)
        results(hero, encounter)
        print("")

def main():
    print("")
    print("")
    print("You are a knight, or used to be, although what left of you now is only a blunt sword.")
    print("In front of you, rose an entrance of cave. From the darkness, you hear unhuman wailings.")
    print("This is the final chance to reseize your long lost honor. You unsheath your sword and walk into the dark.")
    process(encounters_1)
    campfire.explore(hero)
    peddler.store_engine(hero)
    # process(encounters_2)
    # campfire.explore(hero)
    # peddler.store_engine(hero)
    process(boss)

if __name__ == "__main__":
    main()