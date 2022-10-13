lengte = 8
breedte = 3
hoogte = 1.5
kubiekePrijsUitgraven = 25
kubiekePrijsGrond = 32.50
kilometerAfstand = 60
kubiekeTotaal = lengte * breedte * hoogte

print(kubiekeTotaal * kubiekePrijsUitgraven)
print(kubiekeTotaal * kubiekePrijsGrond)
print(f"Totale prijs is: {kubiekePrijsGrond * kubiekeTotaal + kubiekePrijsUitgraven *kubiekeTotaal} euro")
print(f"Voorrij kosten zijn: {2.05 * kilometerAfstand + 250} euro")
#60 kilometer afstand, 250+ 2.05 per km