from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3

teller = 9
for x in range(0,9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        for x in range(0,9):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(0,teller):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveRight()
    teller -=1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()