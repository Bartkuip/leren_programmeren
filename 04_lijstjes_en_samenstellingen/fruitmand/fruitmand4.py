from fruitmand import fruitmand
import random
aantal = int(input("Hoeveel fruit wil je pakken?"))
for x in range(0, aantal):
    max = random.randint(0, len(fruitmand) - 1)
    print(fruitmand[max]['name'])