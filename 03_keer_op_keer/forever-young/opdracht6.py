from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
i = 6

# Jouw python instructies zet je vanaf hier:
for x in range(0, 7):
    robotArm.moveRight()
for x in range(0, 8):
    for x in range(7, 0, -i):
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
        i -= 1
        for x in range (0, 2):
            robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

#Verplaats alle blokken één plek naar rechts. 
#Zorg ervoor dat de volgorde van de blokken gelijk blijft. 


