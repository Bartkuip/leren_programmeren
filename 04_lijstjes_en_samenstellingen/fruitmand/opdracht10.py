from fruitmand import fruitmand
from operator import itemgetter

fruitmand = sorted(fruitmand , key = itemgetter('weight', 'name'), reverse=True)

for fruit in fruitmand: 
    print(fruit['weight'], fruit['name'])

    #lambda