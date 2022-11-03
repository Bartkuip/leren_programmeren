lengte = float(input("Hoe lang?"))
breedte = float(input("Hoe breed?"))
hoogte = float(input("Hoe hoog?"))
tegelKeuze = input("Wat voor tegels wilt u hebben, standaard, rood of kleur").lower()
aantalTegels = (lengte * hoogte * 2) + (breedte * hoogte * 2) + (breedte * lengte)
vierkanteMeter = lengte * breedte
kubiekeTotaal = lengte * breedte * hoogte
kubiekePrijsUitgraven = 25
kubiekePrijsGrond = 32.50
uitgraven = round(kubiekeTotaal * kubiekePrijsUitgraven, 2)
grond = round(kubiekeTotaal * kubiekePrijsGrond, 2)
totaalTegel = 0
kilometerAfstand = input("Hoeveel kilometer moeten wij rijden")
#alles is nu hardcoded voor 60 kilometer afstand, kan ik evt aanpassen
#if statement voor de m3
if tegelKeuze == "standaard" and kubiekeTotaal < 20:
    totaalTegel =  aantalTegels * 250
elif tegelKeuze == "standaard" and kubiekeTotaal >= 20:
    totaalTegel =  aantalTegels * 200
elif tegelKeuze == "rood" and kubiekeTotaal < 20:
    totaalTegel =  aantalTegels * 250 + 25
elif tegelKeuze == "rood" and kubiekeTotaal >= 20:
    totaalTegel =  aantalTegels * 200 + 20
elif tegelKeuze == "kleur" and kubiekeTotaal < 20:
    totaalTegel =  aantalTegels * 250 + 125
elif tegelKeuze == "kleur" and kubiekeTotaal >= 20:
    totaalTegel = aantalTegels * 200 + 100

#if kubiekeTotaal < 20 and kilometerAfstand > 50:


totaalPrijs = round(uitgraven + grond + totaalTegel + 2.05 * kilometerAfstand + 250 ,2)


print(f"Uitgraven:                 €{uitgraven}")
print(f"Afvoeren grond:            €{grond}")
print(f"Voorrijkosten:             €{2.05 * kilometerAfstand + 250}")
print(f"Beton + tegel              €{totaalTegel}")
print(f"Totaal:                    €{totaalPrijs}")
