from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
robotArm.speed = 5
for x in range(0,4):
    for x in range(0,4):
        robotArm.grab()
        for x in range(0,5):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(0,5):
            robotArm.moveLeft()
    robotArm.moveRight()
robotArm.wait()
#Verplaats alle stapels vijf stappen naar rechts.

