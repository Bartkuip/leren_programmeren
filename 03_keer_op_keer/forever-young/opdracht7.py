from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
robotArm.speed = 5
for x in range(0,5):
    robotArm.moveRight()
    for x in range(0,6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    robotArm.moveRight()
robotArm.wait()
    

