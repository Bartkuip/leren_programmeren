from functions import *
import config
from functions import print_delay

story = 0
fireball = 0
green = False

while True:
    print_delay("CONTROLS: ATTACK: a, attack, hit, damage, d and HEAL: h, heal, recover \n")
    print_delay("Welcome, in this game you will attempt to escape the dungeon whilst fighting monsters on your way. \n") 
    goblinEncounter()    
    while story == 0:
        if config.playerHealth >= 0:
            attack = input("What attack do you want to use?").lower()
            if attack in ["attack", "hit", "damage", "d", "a"]:
                playerHealth = config.playerHealth
                damage = damage()
                config.goblinHealth -= damage
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.goblinHealth)
                if config.goblinHealth <= 0:
                    levelUp()
                    orcEncounter()
                    story += 1
            elif attack in ["heal", "recover", "h"]:
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.goblinHealth)
                heal = heal()
                config.playerHealth += heal
            else:
                attackDialogue()

            enemyDamage = damageGoblin()
            config.playerHealth -= enemyDamage
        else:
            endGame()
        
    while story == 1:
        if config.playerHealth >= 0:
            attack = input("What attack do you want to use?").lower()
            if attack in ["attack", "hit", "damage", "d", "a"]:
                playerHealth = config.playerHealth
                damage = damage()
                config.orcHealth -= damage
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.orcHealth)
                if config.orcHealth <= 0:
                    levelUp()
                    trollEncounter()
                    story += 1
            elif attack in ["heal", "recover", "h"]:
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.orcHealth)
                heal = heal()
                config.playerHealth += heal
            else:
                attackDialogue()

            enemyDamage = damageOrc()
            config.playerHealth -= enemyDamage
        else:
            endGame()

    while story == 2:
        if config.playerHealth >= 0:
            attack = input("What attack do you want to use?").lower()
            if attack in ["attack", "hit", "damage", "d", "a"]:
                print("Attack list: attack or heal")
                playerHealth = config.playerHealth
                damage = damage()
                config.trollHealth -= damage
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.trollHealth)
                if config.trollHealth <= 0:
                    levelUp()
                    gerlardEncounter()
                    story += 1
            elif attack in ["heal", "recover", "h"]:
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.trollHealth)
                print("Attack list: attack or heal")
                heal = heal()
                config.playerHealth += heal
            else:
                attackDialogue()

            enemyDamage = damageTroll()
            config.playerHealth -= enemyDamage
        else: 
            endGame()
    while story == 3:
        if config.playerHealth >= 0:
            attack = input("What attack do you want to use?").lower()
            if attack in ["attack", "hit", "damage", "d", "a"]:
                playerHealth = config.playerHealth
                damage = damage()
                config.gerlardHealth -= damage
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.gerlardHealth)
            elif attack in ["heal", "recover", "h"]:
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.gerlardHealth)
                heal = heal()
                config.playerHealth += heal
            else:
                attackDialogue()

            enemyDamage = damageGerlard()
            config.playerHealth -= enemyDamage
        else:
            config.playerHealth = 100
            print('You are back to',config.playerHealth,'health')
            print_delay('GERLARD THE OVERLORD has defeated you, you are now in the purgatory \n')
            zombieEncounter()
            story += 1

    while story == 4:
        if config.playerHealth >= 0:
            attack = input("What attack do you want to use?").lower()
            if attack in ["attack", "hit", "damage", "d", "a"]:
                playerHealth = config.playerHealth
                damage = damage()
                config.zombieHealth -= damage
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.zombieHealth)
                if config.zombieHealth <= 0:
                    levelUp()
                    story += 1
            elif attack in ["heal", "recover", "h"]:
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.zombieHealth)
                heal = heal()
                config.playerHealth += heal
            else:
                attackDialogue()

            enemyDamage = damageGoblin()
            config.playerHealth -= enemyDamage
        else:
            print("gz")
            quit()
    while story == 5:
        direction = input("Where do you want to go? left or right")
        if direction in ["l", "left"]:
            print('You decided to go left')
            print('You walk over a trip wire, the walls slowly come towards you for an inevitable death.')
            print('fkin noob gg ez shouldve picked right git gud')
            endGame()
        elif direction in ["r", "right"]:
            print('You decided to go right')
            unknownEncounter()
            story += 1
        else:
            print('left or right?')

    while story == 6:
        if config.playerHealth >= 0:
            attack = input("What attack do you want to use?").lower()
            if attack in ["attack", "hit", "damage", "d", "a"]:
                print("Attack list: attack or heal")
                playerHealth = config.playerHealth
                damage = damage()
                config.unknownHealth -= damage
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.unknownHealth)
                if config.unknownHealth <= 0:
                    levelUp()
                    print("You enter a maze..")
                    directionMaze = input("Do you want to go left or right?")
                    story += 1

            elif attack in ["heal", "recover", "h"]:
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.unknownHealth)
                print("Attack list: attack or heal")
                heal = heal()
                config.playerHealth += heal
            else:
                attackDialogue()

            enemyDamage = damageUnknown()
            config.playerHealth -= enemyDamage
        else: 
            endGame()

    while story == 7:  
        if directionMaze == "left":
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
                endGame()
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
                story += 1
            else:
                print("Select a button!")
        elif directionMaze == "right":
            print("You ran into a trap..")
            quit()
        else:
            print("Select left or right.")
            directionMaze = input("Do you want to go left or right?")
        
    while story == 8:
        print("You pressed the yellow button, a random door opens... you proceed with caution")
        directionMaze2 = input("Do you want to go left or right?").lower()
        if directionMaze2 == "left":
            print("You walk right into a trap")
            endGame()
        elif directionMaze2 == "right":
            print("You encounter GERLARD THE OVERLORD.")
            print("Select a move")
            config.playerHealth += 100
            print(config.playerHealth)
            story += 1
        else:
            print("Select left or right!")
            directionMaze == "a"
            color = "yellow"
    while story == 9:
        if config.playerHealth >= 0:
            attack = input("What attack do you want to use?").lower()
            if attack in ["attack", "hit", "damage", "d", "a"]:
                playerHealth = config.playerHealth
                damage = damage()
                config.gerlardHealth -= damage
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.gerlardHealth)
                if config.gerlardHealth <= 0:
                    print("Congratulations")
                    endGame()
            elif attack in ["heal", "recover", "h"]:
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.gerlardHealth)
                heal = heal()
                config.playerHealth += heal
            if fireball == 1:
                if attack in ["fireball", "fire", "f"]:
                    playerHealth = config.playerHealth
                    damage = damageFire()
                    config.gerlardHealth -= damage
                    print("Your health is", config.playerHealth)
                    print("The enemy health is", config.gerlardHealth)
                    if config.gerlardHealth <= 0:
                        winGame()      
            else:
                attackDialogue()

            enemyDamage = damageGerlard()
            config.playerHealth -= enemyDamage
        else:
            print("You died to gerlard.")
            quit()