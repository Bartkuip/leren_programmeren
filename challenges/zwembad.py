lengte = 8
breedte = 3
hoogte = 1.5
kubiekePrijsUitgraven = 25
kubiekePrijsGrond = 32.50
kubiekeTotaal = lengte * breedte * hoogte

print(kubiekeTotaal * kubiekePrijsUitgraven)
print(kubiekeTotaal * kubiekePrijsGrond)
print(f"Totale prijs is: {kubiekePrijsGrond * kubiekeTotaal + kubiekePrijsUitgraven *kubiekeTotaal} euro")
