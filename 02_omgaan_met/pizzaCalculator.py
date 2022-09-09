#bart korver 99027534
pizzaSmall = 5.00
pizzaMedium = 8.00
pizzaBig = 11.00

pizzaSmallAmount = int(input("Hoeveel kleine pizza's wilt u (26 centimeter)"))
pizzaMediumAmount = int(input("Hoeveel medium pizza's wilt u (32 centimeter)"))
pizzaBigAmount = int(input("Hoeveel grote pizza's wilt u (36 centimeter)"))
total = pizzaSmall * pizzaSmallAmount + pizzaMedium * pizzaMediumAmount + pizzaBig * pizzaBigAmount

print('Een totaal bedrag van:', total,'euro voor de', pizzaSmallAmount, 'kleine pizza(s),', pizzaMediumAmount, ' medium pizza(s) en'
, pizzaBigAmount, ' grote pizza(s)')


