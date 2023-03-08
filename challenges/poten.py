def potenCalc(giraf, struis, zebra):
    giraf *= 4
    struis *= 2 
    zebra *= 4
    total = giraf + struis + zebra
    return total

girafInput = int(input("Hoeveel giraffen?"))
struisInput = int(input("Hoeveel struisvogels?"))
zebraInput = int(input("Hoeveel zebras?"))
total = potenCalc(girafInput, struisInput, zebraInput)

print(total)

