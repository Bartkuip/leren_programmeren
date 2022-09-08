croissant = float(0.39)
stokbrood = float(2.78)
korting = float(0.50)

croissantAmount = int(input('Hoeveel croissants'))
stokbroodAmount = int(input('Hoeveel stokbroden'))
kortingAmount = int(input ('Hoeveel kortingsbonnen'))
total = croissant * croissantAmount + stokbrood * stokbroodAmount - korting * kortingAmount

print('De feestlunch kost je bij de bakker', round(total, 2),
'euro voor de', croissantAmount, 'croissantjes en de', stokbroodAmount, 'stokbroden als de'
, kortingAmount, 'kortingsbonnen nog geldig zijn!')



#‘De feestlunch kost
# je bij de bakker 18.88 euro voor de 17 
# croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!’