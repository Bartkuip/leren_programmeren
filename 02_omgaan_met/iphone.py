iphone = float(input("Hoe duur is de iphone"))
samsung = float(input("Hoe duur is de samsung?"))
verschil1 = iphone - samsung
verschil2 = samsung - iphone

if iphone > samsung:
    print(f"de iPhone is het duurst, de telefoon kost {iphone} euro")
    print(f"de samsung is het goedkoopst, de telefoon kost {samsung} euro")
    print(f"het advies is dus de samsung te kopen, deze is namelijk {verschil1} euro goedkoper dan de iphone")
elif iphone < samsung:
    print(f"de samsung is het duurst, de telefoon kost {samsung} euro")
    print(f"de iphone is het goedkoopst, de telefoon kost {iphone} euro")
    print(f"het advies is dus de iphone te kopen, deze is namelijk {verschil2} euro goedkoper dan de samsung")
