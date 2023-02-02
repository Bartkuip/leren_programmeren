from functionsNew import *
from configNew import *
listOfMonsters = ["Goblin", "Orc", "Troll", "Gerlard", "Unknown"]
story = True
playerHealth, playerLevel = startGame(playerHealth, playerLevel)
while story:
    monsterHealth, monsterDamage = enemyEncounter(listOfMonsters[0]) #list maken en optellen? zo min mogelijk code
    while monsterHealth >= 0:           
        userMove = str(input("What attack do you want to use? Attack/Heal")).lower()
        playerHealth, monsterHealth = turnSequence(userMove, playerHealth, playerLevel, monsterHealth, monsterDamage)