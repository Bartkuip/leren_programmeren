from fruitmand import fruitmand
kleurenLijst = []
for x in range(len(fruitmand)):
    if fruitmand[x]['color'] not in kleurenLijst:
        kleurenLijst.append((fruitmand[x]['color']))
        
        
print(f"Je hebt keuze uit de kleuren: {' '.join(kleurenLijst)}")
kleurInput = input("Welke kleur wil je gebruiken? ").lower()


rond, nietRond, welRond = 0, 0, 0

for x in range(len(fruitmand)):
    kleurLijst = fruitmand[x].get("color")
    if kleurLijst == kleurInput:
        if fruitmand[x].get("round"):
            rond += 1
            welRond += 1
        else:
            rond -= 1
            nietRond += 1


#“Er zijn {X} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}”
if welRond > nietRond:
    print(f"Er zijn {rond} meer ronde vruchten dan niet ronde vruchten in de kleur{kleurInput}")
elif nietRond > welRond:
    print(f"Er zijn {rond} minder ronde vruchten dan ronde vruchten in de kleur '{kleurInput}'")
else:
    print(f"Evenveel ronde vruchten als niet ronde vruchten")