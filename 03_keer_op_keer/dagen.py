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
