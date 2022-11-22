import random
zakMM = ["rood", "blauw", "groen", "geel", "bruin"]

dictionary = {}
while True:
    try:
        addMM = int(input("Hoeveel M&M(s) wil je toevoegen"))
        break
    except:
        print("Voer aantal M&Ms in")


for x in zakMM:
    dictionary[x] = 0

for i in range(0, addMM):
    randomNumber = random.randint (0, len(zakMM)- 1)
    dictionary[zakMM[randomNumber]] += 1
print(dictionary)




