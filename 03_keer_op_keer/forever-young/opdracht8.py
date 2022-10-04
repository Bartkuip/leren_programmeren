from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
robotArm.moveRight()
for x in range(0,7):
    robotArm.grab()
    for x in range(0,8):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(0,8):
        robotArm.moveLeft()
robotArm.wait()

