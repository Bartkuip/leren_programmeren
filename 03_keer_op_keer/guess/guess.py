import random
rondeInput = int(input("Hoeveel rondes wil je spelen?"))
punten = 0
ronde = 10

while ronde >= 0:
    randomNumber = random.randint(0,1000)
    while rondeInput >= 1:
        rondeInput -= 1
        ronde -= 1
        getalInput = int(input("Welk getal denk je dat het is?"))
        if getalInput == randomNumber:
            print(f"Je hebt gewonnen, het getal was {randomNumber}, +1 punt")
            punten += 1
            volgende = print("Wil je door naar de volgende ronde?").lower()
            if volgende == "ja":
                ronde -= 1
            elif volgende == "nee":
                ronde = 10
            else:
                print("Vul een goed antwoord in")
                
        elif abs(getalInput - randomNumber) < 50:
            if abs(getalInput - randomNumber) < 20:
                print("Je bent HEEL HEET (20)")
            else:
                print("Je bent heet (50 verschil)")
        elif abs(getalInput - randomNumber) > 50:
            print("Je bent koud")

        if getalInput > randomNumber:
                print("Lager")
        elif getalInput < randomNumber:
                print('Hoger')

print(f"{randomNumber} was het getal, L bozo")

