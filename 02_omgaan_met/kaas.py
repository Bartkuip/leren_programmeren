geel = input("is de kaas geel? (alleen antwoorden met ja en nee, hoofdletter gevoelig)")
if geel == "nee":
    schimmel = input("heeft de kaas blauwe schimmel?")
    if schimmel == "ja":
        korst = input("heeft de kaas een korst?")
        if korst == "ja":
            print('Blue de Rochbaron')
        else:
            print("Foume d'Ambert")
    else: 
        korst = input("heeft de kaas een korst?")
        if korst == "ja":
            print("Camembert")
        else:
            print("Mozzarella") 
else:
    gaten = input("Zitten er gaten in?")
    if gaten == "ja":
        duur = input("Is de kaas duur?")
        if duur == "ja":
            print("Emmenthaler")
        else:
            print("Leerdammer")
    else:
        hard = input("Is de kaas hard als steen?")
        if hard == "ja":
            print("Parmigiano Reggiano")
        else:
            print("Goudse kaas")


