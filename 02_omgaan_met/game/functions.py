import random
import config

def damage():
    lowRoll = 0 + config.playerLevel * 2
    highRoll = 5 + config.playerLevel * 2
    damage = random.randint(lowRoll,highRoll)
    return damage

def heal():
    lowRoll = 2 + config.playerLevel * 2
    highRoll = 10 + config.playerLevel * 2
    heal = random.randint(lowRoll,highRoll)
    return heal

def damageGoblin():
    lowRoll = 1
    highRoll = 5 
    damageGoblin = random.randint(lowRoll,highRoll)
    return damageGoblin

def damageFire():
    lowRoll = 15 + config.playerLevel * 2
    highRoll = 30 + config.playerLevel * 2
    damage = random.randint(lowRoll,highRoll)
    return damage
def damageOrc():
    lowRoll = 3
    highRoll = 6 
    damageOrc = random.randint(lowRoll,highRoll)
    return damageOrc

def damageTroll():
    lowRoll = 5 
    highRoll = 7
    damageTroll = random.randint(lowRoll,highRoll)
    return damageTroll

def damageGerlard():
    lowRoll = 7
    highRoll = 15
    damageGerlard = random.randint(lowRoll,highRoll)
    return damageGerlard

def damageUnknown():
    lowRoll = 7
    highRoll = 10
    damageUnknown = random.randint(lowRoll,highRoll)
    return damageUnknown

def levelUp():
    config.playerLevel += 1
    print('------------------------------------')
    print('Congratulations, you are now level:',config.playerLevel,'!')
    print('------------------------------------')
    return 

def attackDialogue():
    print("---------------------------------------------------------")
    print("--------------Please use a valid move--------------------")
    print("-----------------USE ATTACK / HEAL-----------------------")
    print("If you don't use anything the enemy can still attack you!")
    print('---------------------------------------------------------')
    return

def healthDialogue():
    print("Your health is", config.playerHealth)
    print("The enemy health is", config.orcHealth)
    return

def endGame():
    print('------------------------------------------')
    print('GAME OVER! Thank you for playing the demo.')
    print('------------------------------------------')    
    quit()