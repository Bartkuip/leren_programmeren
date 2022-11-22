dagen = ("Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag", "Zondag")

alledagen = "dagen in de week bestaan uit"
for x in dagen:
    alledagen += " " + x + ','
print(alledagen)

werkdagen = "werkdagen in de week zijn:"
for x in dagen[0:5]:
    werkdagen += " " + x + ','
print(werkdagen)

weekenddagen = "weekenddagen in de week zijn:"
for x in dagen[5:7]:
    weekenddagen += " " + x + ','
print(weekenddagen)

omgedraaidalledagen = "alle dagen omgedraaid zijn:"
for x in dagen[::-1]:
    omgedraaidalledagen += " " + x + ','
print(omgedraaidalledagen)

omgedraaidwerk = "omgedraaide werkdagen in de week zijn:"
for x in dagen[-3::-1]:
    omgedraaidwerk += " " + x + ','
print(omgedraaidwerk)

omgedraaidweekend = "omgedraaide weekenddagen in de week zijn:"
for x in dagen[:4:-1]:
    omgedraaidweekend += " " + x + ','
print(omgedraaidweekend)