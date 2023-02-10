from functionsNew import *
from configNew import *
monsterOrder = 0
listOfMonsters = ["Goblin", "Orc", "Troll", "Gerlard", "Unknown"]
story = 1
fireball = 0
playerHealth, playerLevel = startGame(playerHealth, playerLevel)
while story == 1:
    #if index is out of range do something else?
    #if enemyEncounter(listOfMonsters[monsterOrder]) != len(listOfMonsters) - 1:
    monsterHealth, monsterDamage = enemyEncounter(listOfMonsters[monsterOrder]) #list maken en optellen? zo min mogelijk code
    #else:
    #    story = 2
    while monsterHealth >= 1:    
        print(playerLevel)       
        userMove = str(input("What attack do you want to use? Attack/Heal")).lower()
        playerHealth, monsterHealth = turnSequence(userMove, playerHealth, playerLevel, monsterHealth, monsterDamage)
    else:
        monsterOrder += 1

#maze part after index is out of range:

while story == 2:
    print("Puzzle room!")
    color = input('''There are 4 colored buttons on the wall, which one do you choose? 
    A) RED 
    B) BLUE 
    C) GREEN 
    D) YELLOW
    ''')
    if color in ["red", "RED", "r", "a"]:
        print("You pressed the red button but you find absolutely nothing, select another button")
    elif color in ["blue", "BLUE", "b"]:
        print("You clicked the blue button, 20 monsters jump out and kill you")
        quit()
    elif color in ["green", "GREEN", "g", "c"]:
        if green is False:
            print("You pressed the green button and find a new magic spell named 'Fireball'")
            print("---- FIREBALL ----")
            print("- Damage: 15-30 --")
            print("------------------")
            green = True
            fireball = 1
        else:
            print("The room is empty now.")
    elif color in ["yellow", "YELLOW", "Y", "d"]:
        #final boss
        print('')
    else:
        print("Select a button!")