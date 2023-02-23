from configNew import *
def startGame(health, level):
    print("CONTROLS: ATTACK: a, attack, hit, damage.")
    print("Welcome, in this game you will attempt to escape the dungeon whilst fighting monsters on your way. \n")
    health = int(input("Met hoeveel HP wil je starten? Recommended hp is 100\n"))
    level = int(input("Met welk level wil je starten? Recommended level is 1\n"))
    return health, level

def enemyEncounter(monster) -> str:
    if monster == "Goblin":
        monsterHealth = 100
        monsterDamage = 5
        print(f"You've encountered a {monster}! Health: {monsterHealth} / {monsterHealth}")
    elif monster == "Orc":
        monsterHealth = 150
        monsterDamage = 7
        print(f"You've encountered an {monster}! Health: {monsterHealth} / {monsterHealth}")
    elif monster == "Troll":
        monsterHealth = 200
        monsterDamage = 8
        print(f"You've encountered a {monster}! Health: {monsterHealth} / {monsterHealth}")
    elif monster == "Gerlard":
        monsterHealth = 200
        monsterDamage = 13
        print(f"You've encountered a {monster}! Health: {monsterHealth} / {monsterHealth}")
    elif monster == "Unknown":
        monsterHealth = 200
        monsterDamage = 10
        print(f"You've encountered an {monster} monster! Health: {monsterHealth} / {monsterHealth}")
    return monsterHealth, monsterDamage

def turnSequence(move, hp, lvl, monsterhp, monsterdmg):
    damage = lvl * 3
    if move in ["attack", "hit", "damage", "d", "a"]:
        monsterhp -= damage
        hp -= monsterdmg
        print(f"Current health of the player is: {hp}")
        print(f"Current health of the monster is: {monsterhp}")
    return hp, monsterhp
