names = {}
def nameFunction():
    newNames = True
    while newNames:
        inputNaam = input("Wat is je naam?")
        inputLeeftijd = input("Wat is je leeftijd")
        if inputNaam == "stop" or inputLeeftijd == "stop":
            newNames = False
        elif inputNaam not in names.keys():
            names[inputNaam] = inputLeeftijd
        else:
            print("Die naam heb ik al")
    return

nameFunction()
for x, y in names.items():
    print(f"{x.capitalize()} is {y} jaar")
