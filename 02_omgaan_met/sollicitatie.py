ervaringDier = int(input("Hoeveel jaar ervaring heeft u met dieren-dressur?"))
ervaringJongleren = int(input("Hoeveel jaar ervaring heeft u met jongleren"))
ervaringAcrobatiek = int(input("Hoeveel jaar ervaring heeft u in de acrobatiek"))
diploma = input("Heeft u een MBO-4 Diploma? Alleen antwoorden met ja of nee ")
rijbewijs = input("Heeft u een vrachtwagen rijbewijs")
hoed = input("Bent u in bezit van een hoge hoed?")
gender = input("Bent u een man/vrouw?")
if gender == "man":
    snor = int(input("Hoe lang is uw snor in centimeter")) #10 of hoger
    haar = 0
if gender == "vrouw":
    rood = input("Heeft u rood en krullend haar?")
    if rood == "ja":
        haar = int(input("Hoelang is uw haar in centimeter")) #20cm of langer
        snor = 0
lengte = int(input("Hoelang bent u in centimeters?"))
kilo = int(input("Hoe zwaar weegt u?"))
certificaat = input("Bent u in bezit van een 'Overleven met gevaarlijk personeel certificaat?'")
input("Speel je league of legends?")
input("Favoriete pizza?")
input("Heeft u een laptop?")
input("Favoriete basketbal speler?")

punten = 0
if ervaringDier >= 3:
    punten += 1
    ervaringJongleren = 0
    ervaringAcrobatiek = 0
if ervaringJongleren >=4:
    punten += 1
    ervaringAcrobatiek = 0
if ervaringAcrobatiek >=5:
    punten += 1
if diploma == "ja":
    punten += 1
if rijbewijs == "ja":
    punten += 1
if hoed == "ja":
    punten += 1
if snor >= 10:
    punten += 1
if haar >= 20:
    punten += 1
if lengte >= 150:
    punten += 1
if kilo <= 90:
    punten += 1
if certificaat == "ja":
    punten += 1
if punten >= 8:
    print("Je bent aangenomen")

print(punten)