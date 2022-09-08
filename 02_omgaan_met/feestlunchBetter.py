croissant = float(0.39)
stokbrood = float(2.78)
korting = float(0.50)

croissantAmount = int(input('Hoeveel croissants'))
stokbroodAmount = int(input('Hoeveel stokbroden'))
kortingAmount = int(input ('Hoeveel kortingsbonnen'))
total = croissant * croissantAmount + stokbrood * stokbroodAmount - korting * kortingAmount

print(round(croissant * int(croissantAmount),2), 'euro kosten de croissants')
print(round(stokbrood * int(stokbroodAmount), 2), 'euro kosten de stokbroden')
print(round(korting * int(kortingAmount), 2), 'euro korting')
print(total, 'euro')


