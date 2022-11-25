from fruitmand import fruitmand
del fruitmand[4]
fruitKleur = []

for x in range(len(fruitmand)):
    if fruitmand[x]['color'] in fruitKleur:
        print("Die kleur heb ik al!")
    else:
        fruitKleur.append((fruitmand[x]['color']))
print(fruitKleur)