dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

stopDag = input("Tot welke dag wil je tellen?")
index = 0
doorgaan = False
while not doorgaan:
    print(dagen[index])
    doorgaan = False
    if dagen[index] == stopDag:
        doorgaan = True
    index += 1

#tweede uitwerking:
#doeVolgendeDag = True
#while doeVolgendeDag:
#    print(dagen[index])
#    doeVolgendeDag = dagen[index] != stopDag
 #   index += 1
