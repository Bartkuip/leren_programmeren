iphone = float(input("Hoe duur is de iphone"))
samsung = float(input("Hoe duur is de samsung?"))
verschil = abs(iphone - samsung)

if verschil:
    print(f"de iPhone is het duurst, de telefoon kost {iphone} euro")
    print(f"de samsung is het goedkoopst, de telefoon kost {samsung} euro")
    print(f"het advies is dus de samsung te kopen, deze is namelijk {verschil} euro goedkoper dan de iphone")
elif verschil <= 50:
    print(f"de samsung is het duurst, de telefoon kost {samsung} euro")
    print(f"de iphone is het goedkoopst, de telefoon kost {iphone} euro")
    print(f"het advies is dus de iphone te kopen, deze is namelijk {verschil} euro duurder dan de samsung")