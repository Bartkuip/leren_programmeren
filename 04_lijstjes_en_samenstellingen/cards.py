import random
kleuren = ("Klaveren", "Schoppen", "Harten", "Ruiten")
kaarten = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Boer", "Vrouw", "Heer", "Aas")
deck = []
teller = 0
deck.append("Joker")
deck.append("Joker")

for x in kleuren:
    for y in kaarten:
        deck.append(f"{x} {y}")

for y in range(7):
    randomKaart = random.choices(deck)
    teller += 1
    print(f"Kaart {teller} : {randomKaart}")
print(deck)






