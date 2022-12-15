from fruitmand import fruitmand
for x in range(0, len(fruitmand)):
    if fruitmand[x].get('name') == 'druif':
        fruitmand.remove(fruitmand[x])
        break
fruitKleur = []

for x in range(len(fruitmand)):
    if fruitmand[x]['color'] not in fruitKleur:
        fruitKleur.append((fruitmand[x]['color']))
        
print(fruitKleur)