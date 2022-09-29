from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
robotArm.moveRight()
robotArm.moveRight()
robotArm.drop()
robotArm.moveLeft()
robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
robotArm.moveLeft()
robotArm.grab()
for x in range(0, 9):
    robotArm.moveRight()
robotArm.drop()
for x in range(10, 2, -1):
    robotArm.moveLeft()
robotArm.grab()
for x in range(1, 9):
    robotArm.moveRight()
robotArm.drop()
for x in range(10, 3, -1):
    robotArm.moveLeft()
robotArm.grab()
for x in range(2, 9):
    robotArm.moveRight()
robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
#Verplaats de hele stapel blokken één plek naar rechts.
# Zorg ervoor dat de volgorde van de blokken gelijk blijft.
