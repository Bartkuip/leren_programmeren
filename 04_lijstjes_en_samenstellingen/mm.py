import random
mm = ("oranje", "blauw", "groen", "bruin")
hoeveelMM = int(input("Hoeveel MM wil je in de zak hebben"))
zakMM = []

for x in range(hoeveelMM):
    randomNumber = random.randint(0,3)
    zakMM.append(mm[randomNumber])

print(zakMM)

