from functionsNew import *
def gameStart():
    from configNew import playerHealth, playerLevel
    story = 1
    listOfMonsters = ["Goblin", "Orc", "Troll", "Gerlard", "Unknown"]
    monsterOrder = 0
    artifact = 0
    green = False
    playerHealth, playerLevel = startGame(playerHealth, playerLevel)
    while story == 1:
        if monsterOrder < len(listOfMonsters):
            monsterHealth, monsterDamage = enemyEncounter(listOfMonsters[monsterOrder]) #list maken en optellen? zo min mogelijk code
        else:
            story = 2
        while monsterHealth >= 1:      
            userMove = str(input("What attack do you want to use? Attack/Heal")).lower()
            playerHealth, monsterHealth = turnSequence(userMove, playerHealth, playerLevel, monsterHealth, monsterDamage)
        else:
            monsterOrder += 1

    #maze part after index is out of range:

    while story == 2:
        if artifact == 0:
            artifact += 1
            print(f"You found an artifact after beating all the monsters ({artifact})")
        else:
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
                artifact += 1
                print(f"You found an artifact! ({artifact})")
                green = True
            else:
                print("The room is empty now.")
        elif color in ["yellow", "YELLOW", "Y", "d"]:
            print("You click the yellow door, infront of you 2 more doors appear...")
            door = input("Do you want to take left or right?")
            if door in ["left", "l"]:
                print("You found the exit of the dungeon, congratulations!")
                print(f"You collected {artifact} artifacts.")
                story = 3
                
            elif door in ["right", "r"]:
                print("Decypher the code")
                correctWord = input("trab rood neverhcseg si edoc ezed").lower()
                if correctWord == "deze code is geschreven door bart":
                    artifact += 1
                    print("You found the exit of the dungeon, congratulations!")
                    print(f"You collected {artifact} artifacts.")
                    story = 3
                    
                else:
                    print("You entered the wrong code... the floor collapses")
                    quit()

            else:
                door = input("Do you want to take left or right?")
        else:
            print("Select a button!")

    while story == 3:
        repeat = input("Wil je nog een keer spelen? (alleen ja of nee) \n")
        if repeat == "ja":
            print("Thank you for playing the game, have fun in another run!")
            gameStart()
        else:
            quit()
gameStart()