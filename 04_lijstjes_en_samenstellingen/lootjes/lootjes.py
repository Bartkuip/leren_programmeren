import random
nameList = []
shuffleList = []
lootjesGen = {}
newNames = True
shuffling = False
while newNames:
    userInput = input("Wat is je naam?")
    if userInput not in nameList:
        nameList.append(userInput)
        shuffleList.append(userInput)
        repeatInput = input("Wil je nog een naam toevoegen?")
        if repeatInput == "ja":
            newNames = True
        else:
            if len(nameList) < 3:
                print("Niet genoeg namen")
                quit()
            else:
                newNames = False
                shuffling = True
    else:
        print("Die naam heb ik al!")
        
while shuffling: 
    random.shuffle(shuffleList)
    shuffling = False
    for x in range(len(nameList)):
        if nameList[x] != shuffleList[x]:
            lootjesGen[nameList[x]] = shuffleList[x]
        else:
            shuffling = True    

for x, y in lootjesGen.items():
    print(f"{y} heeft {x.capitalize()}")