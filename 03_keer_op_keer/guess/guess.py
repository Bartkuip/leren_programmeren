import random
rondeInput = int(input("Hoeveel rondes wil je spelen?"))
randomNumber = random.randint(0,1000)
punten = 0
raden = 0

def hogerLager():
    if getalInput > randomNumber:
        print("Lager")
    elif getalInput < randomNumber:
        print('Hoger')

while rondeInput >= 1:
    print(f"Je hebt nog {rondeInput} rondes om te spelen")
    #raden = 0
    rondeInput -= 1
    randomNumber = random.randint(0,1000)
    while raden <= 9:
        raden += 1
        #print(randomNumber)
        getalInput = int(input("Welk getal denk je dat het is?"))
        if getalInput == randomNumber:
            print(f"Je hebt gewonnen, het getal was {randomNumber}, +1 punt")
            punten += 1
            volgende = input("Wil je door naar de volgende ronde?").lower()
            if volgende == "ja":
                break
            elif volgende == "nee":
                print(f"je hebt {punten} punt(en)")
                quit()

        elif abs(getalInput - randomNumber) < 50:
            hogerLager()
            if abs(getalInput - randomNumber) < 20:
                print("HEEL HEET")
            else:
                print("heet")
        elif abs(getalInput - randomNumber) > 50:
            hogerLager()
            print("koud")
    while raden >= 10:
        print("Helaas je hebt het niet geraden binnen 10 beurten")
        volgende = input("Wil je door naar de volgende ronde?").lower()
        if volgende == "ja":
            raden = 0
        elif volgende == "nee":
            print(f"je hebt {punten} punt(en)")
            quit()
        
        



print(f"Helaas was dit de laatste ronde, je hebt {punten} punt(en)")