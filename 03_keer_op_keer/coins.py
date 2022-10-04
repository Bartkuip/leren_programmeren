# name of student: Bart Korver
# number of student: 99027534
# purpose of program: Count change
# function of program: 
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #te betalen is 
paid = int(float(input('Paid amount: ')) * 100) #wat je hebt betaald
change = paid - toPay #wisselgeld = betaald - te betalen =

if change > 0: #als wisselgeld 0 is dan:
  coinValue = 500 #value van de coin = 500
  
  while change > 0 and coinValue > 0: #als wisselgeld groter is dan 0 en waarde van de coin groter is dan 0:
    nrCoins = change // coinValue #aantal coins = wisselgeld // waarde

    if nrCoins > 0: # als number of coins groter is dan 0:
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #print nrcoins, coinvalue
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #

# comment on code below: hij checked elke keer wat de coinvalue is, van 5 euro naar 3 euro naar 2 euro naar 50 cent etc
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #als je klaar bent met rekenen laat hij zien hoeveel wisselgeld je nog moet krijgen/had moeten krijgen
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')