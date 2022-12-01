from fruitmand import fruitmand
namenLijst = []
lengte = 0
for x in range(0, len(fruitmand)):
    nameList = len(fruitmand[x].get("name"))
    if nameList > lengte:
        lengte = nameList

for x in range(0, len(fruitmand)):
    if  lengte == len(fruitmand[x].get("name")):
        naam = fruitmand[x].get("name")
        kleur = fruitmand[x].get("color")
        gewicht = fruitmand[x].get("weight")
        break

kleurTranslation = {
    "green" : "groene",
    "red" : "rode",
    "orange" : "oranje",
    "brown" : "bruin",
    "black" : "zwart",
    "yellow" : "gele",
    "blue" : "blauw",
    "purple" : "paars",
    "pink" : "roze"
}

print(f'De "{naam}" ({lengte} letters) heeft een {kleur} kleur en een gewicht van {gewicht / 1000} kg.')