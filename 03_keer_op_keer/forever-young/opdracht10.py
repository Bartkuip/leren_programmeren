from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
i = 9
while i >= 0:
    robotArm.grab()
    for x in range(0, i):
        robotArm.moveRight()
    i -= 1
    robotArm.drop()    
    for x in range(0, i):
        robotArm.moveLeft()
    i -= 1
    

# Na jouw code wachten tot het sluiten van de window:
#Draai de volgorde van de blokken om.

#Je mag maximaal 15 regels code gebruiken inclusief de import, het laden van de robotarm en de wait
