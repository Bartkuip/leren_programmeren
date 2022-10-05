from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
teller = 9
for x in range(0,9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "":
        print("test")
        robotArm.wait()
    else: #kan ook elif doen met alle kleuren: if color in [etc, etc]
        for x in range(0, teller):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(0, teller):
            robotArm.moveLeft()
        teller -= 1