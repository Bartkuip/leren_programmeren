lengte = float(input("Hoe lang?"))
breedte = float(input("Hoe breed?"))
hoogte = float(input("Hoe hoog?"))
kubiekePrijsUitgraven = 25
kubiekePrijsGrond = 32.50
kilometerAfstand = 60
kubiekeTotaal = lengte * breedte * hoogte
totaalPrijs = round(kubiekePrijsGrond * kubiekeTotaal + kubiekePrijsUitgraven *kubiekeTotaal, 2)

print(round(kubiekeTotaal * kubiekePrijsUitgraven, 2))
print(round(kubiekeTotaal * kubiekePrijsGrond, 2))
print(f"Totale prijs is: {totaalPrijs} euro")
print(f"Voorrij kosten zijn: {2.05 * kilometerAfstand + 250} euro")