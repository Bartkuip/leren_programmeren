# stel de vraag ? aan de gebruiker
# zolang er geen quit word geantwoord stel je vraag opnieuw
# print het aantal keer dat de vraag is gesteld

aantal = 0
question = input("?")
while True:
    if question == "quit":
        print(aantal)
        quit()
    else:
        aantal +=1
        question = input("?")
        
    





