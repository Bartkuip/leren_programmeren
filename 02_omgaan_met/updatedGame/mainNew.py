from functionsNew import *
from configNew import *
listOfMonsters = ["Goblin", "Orc", "Troll", "Unknown", "Gerlard"]
story = True
monsterActive = False
monsterCounter = 0
turnCounter = 0
playerHealth, playerLevel = startGame(playerHealth, playerLevel)
while story:
    while monsterActive == False:
        monsterHealth, monsterDamage = enemyEncounter(listOfMonsters[monsterCounter]) #list maken en optellen? zo min mogelijk code
        while monsterHealth >= 0:     
            if playerHealth <= 0:
                print("The player has died!")
                quit()
            else:     
                turnCounter += 1
                print(f"You are currently on turn: {turnCounter}!")
                userMove = str(input("What attack do you want to use? Attack/Heal\n")).lower()
                playerHealth, monsterHealth = turnSequence(userMove, playerHealth, playerLevel, monsterHealth, monsterDamage)
        else:
            playerLevel += 1 
            monsterCounter += 1
            turnCounter = 0