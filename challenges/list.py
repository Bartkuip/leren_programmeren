import random

naam = input("Wat is je naam?")
nummer = int(input("Complimenten"))
complimenten = (f'Je bent geweldig: {naam}',f'Je bent aardig: {naam}',f'Je bent lief: {naam}',f'Je bent knap: {naam}',f'Je bent slim: {naam}')
vorig_getal = 0

for x in range(nummer):
    getal = random.randint(0, 4)
    while getal == vorig_getal:
        getal = random.randint(0,4)
    print(complimenten[getal])
    vorig_getal = getal