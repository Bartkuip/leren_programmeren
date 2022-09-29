from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:


# Na jouw code wachten tot het sluiten van de window:
robotArm.grab()
for x in range(0,9):
    robotArm.moveRight()
robotArm.drop()
for x in range(9, 4, -1):
    robotArm.moveLeft()
robotArm.grab()
for x in range(0, 5):
    robotArm.moveRight()
robotArm.drop()
for x in range(9, 7, -1):
    robotArm.moveLeft()
robotArm.grab()
for x in range(7, 9):
    robotArm.moveRight()
robotArm.drop()
robotArm.wait()