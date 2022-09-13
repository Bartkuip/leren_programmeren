#bart korver 99027534
pizzaSmall = 5.00
pizzaMedium = 8.00
pizzaBig = 11.00

var = 0 # do while bestuderen
while var == 0:
    try:
        pizzaSmallAmount = int(input("Hoeveel kleine pizza's wilt u (26 centimeter)"))
        var += 1
    except:
        print("Vul een heel getal in")
while var == 1:
    try:
        pizzaMediumAmount = int(input("Hoeveel medium pizza's wilt u (32 centimeter)"))
        var += 1
    except:
        print("Vul een heel getal in")
while var == 2:
    try: 
        pizzaBigAmount = int(input("Hoeveel grote pizza's wilt u (36 centimeter)"))
        var += 1
    except:
        print("Vul een heel getal in")
total = pizzaSmall * pizzaSmallAmount + pizzaMedium * pizzaMediumAmount + pizzaBig * pizzaBigAmount

print('Een totaal bedrag van:', total,'euro voor de', pizzaSmallAmount, 'kleine pizza(s),', pizzaMediumAmount, ' medium pizza(s) en'
, pizzaBigAmount, ' grote pizza(s)')
print(pizzaSmallAmount ,'x kleine pizzas')
print(pizzaMediumAmount ,'x medium pizzas')
print(pizzaBigAmount, 'x grote pizza' )
print(total, 'euro in totaal')

