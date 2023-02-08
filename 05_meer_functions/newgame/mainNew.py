from functionsNew import *
from configNew import *
monsterOrder = 0
listOfMonsters = ["Goblin", "Orc", "Troll", "Gerlard", "Unknown"]
story = True
playerHealth, playerLevel = startGame(playerHealth, playerLevel)
while story:
    monsterHealth, monsterDamage = enemyEncounter(listOfMonsters[monsterOrder]) #list maken en optellen? zo min mogelijk code
    while monsterHealth >= 1:    
        print(playerLevel)       
        userMove = str(input("What attack do you want to use? Attack/Heal")).lower()
        playerHealth, monsterHealth = turnSequence(userMove, playerHealth, playerLevel, monsterHealth, monsterDamage)
    else:
        monsterOrder += 1