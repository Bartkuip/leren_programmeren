while True: 
    try:
        getal = int(input("Welk getal wil je gebruiken?"))
        for x in range(1,11):
            print (x * getal)
    except:
        print('l bozo')
    