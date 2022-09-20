import functions
import config

story = 0
while True:    
    while story == 0:
        if config.playerHealth >= 0:
            attack = input("What attack do you want to use?").lower()
            if attack in ["attack", "hit", "damage", "d", "a"]:
                playerHealth = config.playerHealth
                damage = functions.damage()
                config.goblinHealth -= damage
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.goblinHealth)
                if config.goblinHealth <= 0:
                    functions.levelUp()
                    print("----YOU HAVE ENCOUNTERED A NEW ENEMY: ORC ----[",config.orcHealth,"/",config.orcHealth,"]")
                    story += 1
            elif attack in ["heal", "recover", "h"]:
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.goblinHealth)
                heal = functions.heal()
                config.playerHealth += heal
            else:
                functions.attackDialogue()

            enemyDamage = functions.damageGoblin()
            config.playerHealth -= enemyDamage
        else:
            functions.endGame()
        
    while story == 1:
        if config.playerHealth >= 0:
            attack = input("What attack do you want to use?").lower()
            if attack in ["attack", "hit", "damage", "d", "a"]:
                playerHealth = config.playerHealth
                damage = functions.damage()
                config.orcHealth -= damage
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.orcHealth)
                if config.orcHealth <= 0:
                    functions.levelUp()
                    print("----YOU HAVE ENCOUNTERED A NEW ENEMY: TROLL ----[",config.trollHealth,"/",config.trollHealth,"]")
                    story += 1
            elif attack in ["heal", "recover", "h"]:
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.orcHealth)
                heal = functions.heal()
                config.playerHealth += heal
            else:
                functions.attackDialogue()

            enemyDamage = functions.damageOrc()
            config.playerHealth -= enemyDamage
        else:
            functions.endGame()

    while story == 2:
        if config.playerHealth >= 0:
            attack = input("What attack do you want to use?").lower()
            if attack in ["attack", "hit", "damage", "d", "a"]:
                print("Attack list: attack or heal")
                playerHealth = config.playerHealth
                damage = functions.damage()
                config.trollHealth -= damage
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.trollHealth)
                if config.trollHealth <= 0:
                    functions.levelUp()
                    print("----YOU HAVE ENCOUNTERED A NEW ENEMY: GERLARD THE OVERLORD----[",config.gerlardHealth,"/",config.gerlardHealth,"]")
                    story += 1
            elif attack in ["heal", "recover", "h"]:
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.trollHealth)
                print("Attack list: attack or heal")
                heal = functions.heal()
                config.playerHealth += heal
            else:
                functions.attackDialogue()

            enemyDamage = functions.damageTroll()
            config.playerHealth -= enemyDamage
        else: 
            functions.endGame()
    while story == 3:
        if config.playerHealth >= 0:
            attack = input("What attack do you want to use?").lower()
            if attack in ["attack", "hit", "damage", "d", "a"]:
                playerHealth = config.playerHealth
                damage = functions.damage()
                config.gerlardHealth -= damage
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.gerlardHealth)
            elif attack in ["heal", "recover", "h"]:
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.gerlardHealth)
                heal = functions.heal()
                config.playerHealth += heal
            else:
                functions.attackDialogue()

            enemyDamage = functions.damageGerlard()
            config.playerHealth -= enemyDamage
        else:
            config.playerHealth = 100
            print('You are back to',config.playerHealth,'health')
            print('GERLARD THE OVERLORD has defeated you, you are now in the purgatory')
            print("----YOU HAVE ENCOUNTERED A NEW ENEMY: ZOMBIE ----[",config.zombieHealth,"/",config.zombieHealth,"]")
            story += 1

    while story == 4:
        if config.playerHealth >= 0:
            attack = input("What attack do you want to use?").lower()
            if attack in ["attack", "hit", "damage", "d", "a"]:
                playerHealth = config.playerHealth
                damage = functions.damage()
                config.zombieHealth -= damage
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.zombieHealth)
                if config.zombieHealth <= 0:
                    functions.levelUp()
                    story += 1
            elif attack in ["heal", "recover", "h"]:
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.zombieHealth)
                heal = functions.heal()
                config.playerHealth += heal
            else:
                functions.attackDialogue()

            enemyDamage = functions.damageGoblin()
            config.playerHealth -= enemyDamage
        else:
            print("gz")
            quit()
    while story == 5:
        direction = input("Where do you want to go? left or right")
        if direction in ["l", "left"]:
            print('You decided to go left')
            print('You encounter a monster, it slices you in half without hesitation.')
            functions.endGame()
        elif direction in ["r", "right"]:
            print('You decided to go right')
            print('You encounter a monster, you cannot identify what it is... [???/???]')
            story += 1
        else:
            print('left or right?')

    while story == 6:
        if config.playerHealth >= 0:
            attack = input("What attack do you want to use?").lower()
            if attack in ["attack", "hit", "damage", "d", "a"]:
                print("Attack list: attack or heal")
                playerHealth = config.playerHealth
                damage = functions.damage()
                config.unknownHealth -= damage
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.unknownHealth)
                if config.unknownHealth <= 0:
                    functions.levelUp()
                    story += 1
            elif attack in ["heal", "recover", "h"]:
                print("Your health is", config.playerHealth)
                print("The enemy health is", config.unknownHealth)
                print("Attack list: attack or heal")
                heal = functions.heal()
                config.playerHealth += heal
            else:
                functions.attackDialogue()

            enemyDamage = functions.damageUnknown()
            config.playerHealth -= enemyDamage
        else: 
            functions.endGame()

    while story == 7:
        functions.endGame()