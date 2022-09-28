iphone = float(input("Hoe duur is de iphone"))
samsung = float(input("Hoe duur is de samsung?"))
verschil1 = iphone - samsung
verschil2 = samsung - iphone


if iphone and samsung <= 900:
    if iphone > samsung:
        print(f"de iPhone is het duurst, de telefoon kost {iphone} euro")
        print(f"de samsung is het goedkoopst, de telefoon kost {samsung} euro")
        if verschil1 < 50:
            print(f"het advies is dus de alsnog iphone te kopen, deze is namelijk {verschil1} euro duurder dan de samsung")
        elif verschil1 > 50:
            print(f"het advies is dus de samsung te kopen, deze is namelijk {verschil1} euro goedkoper dan de iphone")

    elif iphone < samsung:
        print(f"de samsung is het duurst, de telefoon kost {samsung} euro")
        print(f"de iphone is het goedkoopst, de telefoon kost {iphone} euro")
        if verschil2 <= 50:
            print(f"het advies is dus de iphone te kopen, deze is namelijk {verschil2} euro goedkooper dan de samsung")
        elif verschil2 > 50:
            print(f"het advies is dus de iphone te kopen, deze is namelijk {verschil2} euro goedkoper dan de iphone")
    elif iphone == samsung:
        print(f"koop de iphone")

else:
    print("De telefoons zijn te duur!")

    