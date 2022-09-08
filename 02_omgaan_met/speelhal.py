ticket = float(7.45)
minuteOne = float(0.37 / 5)
friends = input('Hoeveel vrienden')
minutes = input('Hoeveel minuten')

print(round(ticket * int(friends), 2), 'euro kosten tickets')
print(round(minuteOne * int(minutes) * int(friends), 2), 'extra kosten voor VR' )