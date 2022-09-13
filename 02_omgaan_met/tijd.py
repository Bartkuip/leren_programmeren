tijdUren = int(input("Hoeveel uur"))
tijdMinuten = int(input("Hoeveel minuten"))

eindUren = 23 - tijdUren
eindMinuten = 60 - tijdMinuten

print('nog', eindUren, 'uur')
print('nog', eindMinuten, 'minuten')

leeftijd = int(input("Hoe oud bent u"))
leeftijd *= 3
print(leeftijd)

if leeftijd >= 16:
    print("Je bent oud genoeg")
else:
    print('bek dicht')