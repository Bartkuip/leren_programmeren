boodschappen = {}
keuze = True

while keuze:
    boodschapInput = input("Voeg een boodschap toe").lower()
    boodschapAantal = input(f"Hoeveel {boodschapInput} wil je?")
    if boodschapInput in boodschappen.keys():
        boodschappen.update({boodschapInput: boodschapAantal})
    boodschappen[boodschapInput] = boodschapAantal
    boodschappenRepeat = input("Wil je nog iets toevoegen?")
    if boodschappenRepeat == "nee":
        keuze = False
    else:
        keuze = True

print("-[BOODSCHAPPENLIJST]-")
for x, y in boodschappen.items():
    print(f"{y}x {x.capitalize()}")

print("---------------------")



