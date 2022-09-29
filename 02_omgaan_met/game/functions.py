import random
import config
import time
import sys

def print_delay(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)

def damage():
    lowRoll = 0 + config.playerLevel * 2
    highRoll = 5 + config.playerLevel * 2
    damage = random.randint(lowRoll,highRoll)
    return damage

def heal():
    if config.playerHealth >= 100:
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

def orcEncounter():
    print_delay(f"----YOU HAVE ENCOUNTERED A NEW ENEMY: ORC ----[{config.orcHealth} / {config.orcHealth}]")
    print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣧⣄⣉⣉⣠⣼⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⡿⣿⣿⣿⣿⢿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⣤⣤⣈⠙⠳⢄⣉⣋⡡⠞⠋⣁⣤⣤⣧⠀⠀⠀⠀⠀⠀⠀
⠀⢲⣶⣤⣄⡀⢀⣿⣄⠙⠿⣿⣦⣤⡿⢿⣤⣴⣿⠿⠋⣠⣿⠀⢀⣠⣤⣶⡖⠀
⠀⠀⠙⣿⠛⠇⢸⣿⣿⡟⠀⡄⢉⠉⢀⡀⠉⡉⢠⠀⢻⣿⣿⡇⠸⠛⣿⠋⠀⠀
⠀⠀⠀⠘⣷⠀⢸⡏⠻⣿⣤⣤⠂⣠⣿⣿⣄⠑⣤⣤⣿⠟⢹⡇⠀⣾⠃⠀⠀⠀
⠀⠀⠀⠀⠘⠀⢸⣿⡀⢀⠙⠻⢦⣌⣉⣉⣡⡴⠟⠋⡀⢀⣿⡇⠀⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣧⠈⠛⠂⠀⠉⠛⠛⠉⠀⠐⠛⠁⣼⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣏⠀⣤⡶⠖⠛⠋⠉⠉⠙⠛⠲⢶⣤⠀⣹⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣶⣿⣿⣿⣿⣿⣿⣶⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠛⠛⠛⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')

def goblinEncounter():
    print_delay(f"You encounter a goblin! [{config.goblinHealth}] / [{config.goblinHealth}] \n")
    print('''⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣀⣀⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⠤⢶⣿⣿⣿⡿⠋⠛⢻⣷⣤⡀⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⣠⠶⣏⣀⣼⣿⣿⣿⣷⣄⣀⣈⣿⡿⢷⡀⠄⠄⠄⠄⠄⠄
⠄⠄⢠⠤⠤⠤⠠⠾⠷⠾⠿⣿⣿⠿⠛⠛⠛⠛⣛⣋⣉⣁⡀⢳⡀⠄⠄⠄⠄⠄
⠄⠄⢸⡀⢰⡆⢀⡤⠄⢰⡂⠉⠛⠁⢹⣿⠿⠛⢩⣥⣶⣿⠃⢸⣧⠄⠄⠄⠄⡄
⠄⠄⢶⣌⡁⠉⠘⠄⠈⢁⣔⠉⢹⣿⢆⢠⣬⣥⣤⣤⣤⣤⣤⣿⠟⣠⠶⢋⡽⠁
⠄⠄⢠⠛⠃⣤⢾⣿⠃⣎⣹⣿⣿⣷⠿⢆⣿⠿⠿⠟⣛⡛⠿⣿⣼⠃⣶⡞⠃⠄
⠄⠄⠄⢠⣼⢱⠖⡀⡀⢿⣿⠿⠛⣁⣋⣭⠖⣌⠻⢿⣿⠟⡆⣹⣥⡏⣀⡄⠄⠄
⠄⠄⢿⡈⢹⡎⣾⡇⠱⠈⡁⠄⣶⠉⣉⢁⢸⣿⡀⠈⠁⣆⣰⣿⠏⣰⣿⡇⠄⠄
⠄⠄⠄⢀⣀⣓⠘⠃⢛⣠⣥⣤⣶⡶⣶⣶⣦⣤⣤⣴⠾⢋⣌⠻⠂⣉⣉⠄⠄⠄
⠄⣴⡃⣿⡿⢡⣆⢉⣛⣩⣭⣤⣶⣶⣦⣬⣭⣥⣶⡶⠇⣿⡟⢰⣷⡌⣿⣷⡀⠄
⢀⠻⡇⠛⢃⡟⣿⢰⣌⢙⠻⠿⢿⣿⡿⢻⠟⣁⠉⢡⡆⠋⠞⣸⠟⡁⠉⣿⣧⠄
⠘⢧⡄⣤⣤⢠⡟⣸⣿⣿⣧⣀⣠⣜⣠⣤⣼⣿⡇⠸⢃⣼⡄⢃⣼⠃⣤⣿⣿⠄
⠄⠄⠁⠄⠄⠄⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠛⠁⠄⠄⠄⠄⠄''')

def trollEncounter():
    print_delay(f"You encounter a troll! [{config.trollHealth}] / [{config.trollHealth}] \n")
    print('''░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░
░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░
░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░
░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░
░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░
█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█
█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█
░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░
░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░
░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░
░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░
░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░
░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░
░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░
░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░''')

def gerlardEncounter():
    print_delay(f"You encounter GERLARD THE OVERLORD!!! [{config.gerlardHealth}] / [{config.gerlardHealth}] \n")
    print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠋⢹⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⡿⠁⠀⠈⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠁⠙⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣾⣦⡀⠀⠀⢰⣿⠃⠀⠀⠀⢹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠁⠀⠀⢹⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣿⠃⠻⣧⠀⠀⣿⡏⠀⠀⠀⢀⣠⣽⣿⣶⠶⠿⠿⠿⠿⠿⠿⠿⢶⣶⣤⣄⣀⢀⣴⡿⠋⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣼⡏⠀⠀⢹⣧⣸⣿⠁⢀⣤⣾⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢿⣯⣀⠀⠀⠀⠀⠀⠀⣿⣷⠀⠀⠀⠀⠀⠀⣀⣤⣾
⣿⡇⠀⠀⠀⢻⣿⣿⣴⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⣿⡟⠀⢀⣠⣴⣾⠿⠛⢹⣿
⣿⡇⠀⠀⠀⠀⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⢰⣿⣧⣶⡿⠛⠉⠀⠀⠀⣾⡏
⢹⣇⢰⠀⠀⢠⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⣾⣿⡟⠉⠀⠀⠀⠀⠀⣼⡿⠀
⠘⣿⡈⡆⠀⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⡟⠀⠀⠀⠀⠀⠀⣴⡿⠁⠀
⠀⢹⣧⠸⣤⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡇⣰⠊⠁⠀⢀⣼⡿⠁⠀⠀
⠀⠀⢿⣇⣹⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⡄⠀⠀⢹⣿⠃⠀⠀⣠⣿⠟⠀⠀⠀⠀
⠀⠀⠈⣿⣿⠃⢿⡇⠉⠛⠷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣴⡶⠶⠟⠛⠋⣻⡿⠀⠀⠀⢸⣿⢀⣠⣾⡿⠁⠀⠀⠀⠀⠀
⠀⠀⣴⡿⠁⠀⠘⣿⡄⠀⠀⠀⠉⠛⣷⣼⠀⢰⣤⣴⡶⠾⠟⠛⠋⠉⠁⠀⠀⠀⠀⠀⣰⣿⢃⠀⠀⠀⢸⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⢰⣿⠁⠀⠀⠀⠈⢿⣦⣄⣀⣀⣼⠇⠀⠀⠀⠀⠻⣧⣀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⠕⠃⠀⠀⠀⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⣿⡆⠀⠀⠀⠀⠀⠈⠙⠛⠋⠉⠀⠀⠀⠀⠀⠀⠈⠛⠿⣶⣶⣶⣶⣶⡾⠿⠛⠋⠁⠀⠀⠀⠀⣼⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⢿⣦⡀⠀⠀⠀⢀⣤⣦⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⢿⣦⣄⠀⠈⠀⢹⣤⠞⠉⠹⣄⣤⠞⠻⣄⣠⠿⡄⢀⡴⠋⠳⣄⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠛⠿⣶⣤⣀⠀⠀⠀⠀⠋⠀⠀⠀⠙⠋⠀⠙⠁⠀⠀⠀⠈⠂⣀⣤⣾⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠉⠛⠿⣶⣦⣤⣀⣀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣴⣶⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣴⡿⠛⠷⣶⣤⣄⣉⣽⣿⠛⠛⠿⠿⠟⠛⠛⣻⡿⠋⠉⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣥⡶⣶⣤⠤⠈⠉⠉⠉⠀⢀⣀⠲⡄⠀⢀⣼⠟⠁⠀⢀⣿⣷⡀⣀⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⠟⢠⡿⣡⣦⣤⣤⣤⣤⣼⣟⡛⠻⠿⠿⠟⠋⠀⠀⣠⣾⠋⠹⣿⠟⣉⣡⣄⡉⠻⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡟⠁⠀⠉⠉⠙⡿⢋⡿⠂⣀⣀⣤⣤⣤⣾⠟⠁⠀⢰⣿⠟⠋⠁⠉⢻⡆⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣷⡿⠛⠋⠉⠉⠁⢄⠀⠀⠀⠘⣿⠀⠀⠀⠀⠈⣿⢸⣿⡀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⡁⠠⣤⣤⣤⣀⣘⣧⡀⠀⠀⠛⢷⣦⡀⠀⣠⣿⡇⠻⠷⠶⢿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⠷⠀⠀⠈⣿⡏⠉⠉⢻⣆⣀⣤⠄⠻⣷⡀⠻⣿⣄⡀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣟⣁⠀⠀⠀⣠⡾⠛⠁⠀⠀⠀⠙⣿⡇⠀⠀⠹⣷⡄⠈⠙⠿⣦⣄⣸⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠿⠿⠟⠀⠀⠀⠀⠀⠀⠀⢸⣷⣶⣶⠾⠿⠟⠀⠀⠀⠈⠻⡿⠁⠀⠀⠀⠀⠀⠀⠀''')
def zombieEncounter():
    print_delay(f"----YOU HAVE ENCOUNTERED A NEW ENEMY: ZOMBIE ----[{config.zombieHealth}/{config.zombieHealth}] \n")
    print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠾⠛⠉⠉⠀⠀⠀⠀⠀⠀⢀⡤⠊⠉⠉⠛⠳⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢮⡀⠀⠀⠀⠀⠀⠀⠙⢷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⡡⢤⠀⠀⠀⢰⣛⣉⣉⣓⠢⣄⠀⠀⠀⠈⢉⡁⠐⠒⠒⠂⠉⠉⠉⠛⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠁⣘⡒⠁⢀⠀⠀⠀⣀⣀⣀⣈⣹⣾⣕⠀⢠⡎⠁⡹⠀⣠⠄⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢀⣎⡩⠃⢠⣏⡴⠞⠛⠉⠉⠀⠀⠀⠀⠹⡏⠀⠉⠉⣠⣾⠖⠋⠉⠻⣅⠀⣠⠖⢲⠌⢻⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⡠⠔⢿⠀⢀⡟⠉⠀⠀⠀⣀⣤⣤⡀⠀⠀⠀⣿⠀⠀⠀⡼⠉⠉⠒⢦⣀⠘⠷⡛⠒⡿⣄⠈⣷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⣠⠏⠀⢸⠀⠀⠀⠀⢰⣿⣿⣿⡇⠀⠀⢀⡿⠀⠀⣸⠃⠀⠀⣀⣄⡙⢷⣄⡇⠘⠀⢸⡆⢹⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣧⠞⠁⠀⠀⢸⡆⠀⠀⠀⠸⣿⣿⡿⠃⠀⢀⣼⠃⠀⠀⣿⣆⠀⠀⣿⣿⡟⠀⠙⣧⠳⡤⠞⠀⢸⡇⠀⠀⠀⠀
⠀⢀⣠⠤⠤⢄⡀⠈⣧⢈⣧⠀⠀⢸⣿⣄⣀⣀⣠⣬⣥⠴⠶⢚⣿⠋⠀⠀⠀⢻⣿⣦⣄⠈⠁⠀⠀⣰⠟⠆⠀⠀⠀⢸⣡⠴⠖⠶⣦
⢠⠏⠀⠀⠀⢀⠈⠓⢿⡄⢳⠀⠀⠀⢳⣌⠻⠯⣤⣀⣀⣀⣴⣿⠏⢀⣶⢰⣦⠈⢿⣿⣿⣷⣀⣠⡼⠋⠀⢀⡀⠀⢀⣿⠥⢄⠀⠀⣿
⣏⠀⠀⠀⡟⢉⡽⣦⡈⢻⣼⠄⠀⠀⠀⠉⠓⠦⠤⠬⣏⣡⠾⠃⢀⣾⣿⢸⣿⣇⠈⠻⡯⠽⢯⡽⠁⠠⣴⠝⠃⢀⣾⢋⣁⠈⢀⡾⠃
⠘⠶⠲⢦⣷⠸⣤⣸⡇⠀⢻⣦⡀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠘⠛⠋⠘⠋⠋⠀⠀⠑⠚⠉⠀⠀⠀⠈⣠⣠⡾⠳⠤⣿⡀⣾⠁⠀
⠀⠀⠀⠀⠸⢧⠉⠉⠀⢀⡾⠀⠉⠻⣦⠀⠀⠀⠈⢟⡽⠄⠀⠀⢀⣀⣤⣤⣤⣄⣀⠀⠀⠀⢀⡀⠀⠀⣴⡿⠛⠻⢶⣤⣿⡿⠋⠀⠀
⠀⠀⠀⠀⠀⠙⠒⠒⠚⠋⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠁⠀⣠⣾⡿⢿⠀⠀⢀⣮⣙⡻⣦⡈⠙⠿⠀⣸⠏⠀⠀⠀⠀⢀⣿⣇⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡆⠀⠀⠀⠀⣼⣿⣿⣇⣸⣷⣶⣾⡀⣯⣻⣿⣿⡄⠀⠀⡿⠀⠀⠀⠀⠀⢻⣾⡛⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⡇⠀⠀⠀⠀⠀⠀⠛⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⡀⠀⢸⣿⣿⡟⢻⡿⠿⣇⣿⢸⠿⣿⣿⣿⡏⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠐⡇⠀⠸⣯⠉⠙⠒⣃⣀⣈⣭⣭⣤⣀⣩⡟⠁⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠃⠀⣀⣽⠷⠞⠛⠉⠉⠁⠀⣠⠤⠤⢤⣉⠙⠢⠤⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠘⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⠀⠹⠂⠀⣰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠶⢦⣤⣀⣀⠀⠀⠀⠀⢀⣈⣛⣥⣤⠴⠾⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
def unknownEncounter():
    print_delay('You encounter a monster, you cannot identify what it is... [???/???]')
    print('''            ________
        _jgN########Ngg_
      _N##N@@""  ""9NN##Np_
     d###P            N####p
     "^^"              T####
                       d###P
                    _g###@F
                 _gN##@P
               gN###F"
              d###F
             0###F
             0###F
             0###F
             "NN@'

              ___
             q###r''')

def winGame():
    print('''╔═══╗─────────────╔╗───╔╗───╔╗
║╔═╗║────────────╔╝╚╗──║║──╔╝╚╗
║║─╚╬══╦═╗╔══╦═╦═╩╗╔╬╗╔╣║╔═╩╗╔╬╦══╦═╗╔══╗
║║─╔╣╔╗║╔╗╣╔╗║╔╣╔╗║║║║║║║║╔╗║║╠╣╔╗║╔╗╣══╣
║╚═╝║╚╝║║║║╚╝║║║╔╗║╚╣╚╝║╚╣╔╗║╚╣║╚╝║║║╠══║
╚═══╩══╩╝╚╩═╗╠╝╚╝╚╩═╩══╩═╩╝╚╩═╩╩══╩╝╚╩══╝
──────────╔═╝║
──────────╚══╝''')
    quit()
