import random
import time
rondeInput = int(input("Hoeveel rondes wil je spelen?"))
while rondeInput > 20:
    print("Geef een input onder 20, max rondes is 20!")
    rondeInput = int(input("Hoeveel rondes wil je spelen?"))
randomNumber = random.randint(0,1000)
punten = 0
raden = 0
rondeInputMax = 20

def hogerLager():
    if getalInput > randomNumber:
        print("Lager")
    elif getalInput < randomNumber:
        print('Hoger')

while rondeInput >= 1 or rondeInputMax <= 0:
    print(f"Je hebt nog {rondeInput} rondes om te spelen")
    rondeInputMax -= 1
    rondeInput -= 1
    randomNumber = random.randint(0,1000)
    while raden <= 9:
        raden += 1
        getalInput = int(input("Welk getal denk je dat het is?"))
        if getalInput == randomNumber:
            print(f"Je hebt gewonnen, het getal was {randomNumber}, +1 punt")
            punten += 1
            volgende = input("Wil je door naar de volgende ronde?").lower()
            if volgende == "ja":
                break
            elif volgende == "nee":
                print(f"je hebt {punten} punt(en)")
                time.sleep(10)
                quit()

        elif abs(getalInput - randomNumber) < 50:
            hogerLager()
            if abs(getalInput - randomNumber) < 20:
                print("HEEL HEET")
            else:
                print("Heet")
        elif abs(getalInput - randomNumber) > 50:
            hogerLager()
            print("Koud")
    while raden >= 10:
        print("Helaas je hebt het niet geraden binnen 10 beurten")
        volgende = input("Wil je door naar de volgende ronde?").lower()
        if volgende == "ja":
            raden = 0
        else:
            print(f"je hebt {punten} punt(en)")
            quit()
        
        



print(f"Helaas was dit de laatste ronde, je hebt {punten} punt(en)")