fruit = ('appel', 'peer', 'banaan', 'kers', 'druif', 'bes')

stopFruit = input('waar stoppen?\n')

index = 0
doorgaan = False
while not doorgaan:
    print(fruit[index])
    doorgaan = False
    if fruit[index] == stopFruit:
        doorgaan = True
    index += 1