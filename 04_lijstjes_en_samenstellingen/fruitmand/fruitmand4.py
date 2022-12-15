from fruitmand import fruitmand
import random
aantal = int(input("Hoeveel fruit wil je pakken?"))
for x in range(0, aantal):
    randomFruit = random.choice(fruitmand)
    print(randomFruit['name'])