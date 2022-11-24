from fruitmand import fruitmand

totalWeight = 0

watermeloen = {                                                  
    "name" : "watermelon",
    "weight" : 100,
    "color" : "green",
    "round" : True}

fruitmand.append(watermeloen)                                    

for fruit in fruitmand:                                          
    totalWeight += fruit["weight"]
print(f"{totalWeight} gram")