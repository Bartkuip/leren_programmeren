from functions import *
firstRound = True
n1, n2 = False, False
while True:
    if firstRound:
        print(''' 
        A) getallen optellen?
        B) getallen aftrekken?
        C) getallen vermenigvuldigen?
        D) getallen delen?
        E) getal ophogen?
        F) getal verlagen?
        G) getal verdubbelen?
        H) getal halveren?
        ''')
    else:
        print(f''' 
        Wat wil je met {n1} doen?
        A) getallen optellen?
        B) getallen aftrekken?
        C) getallen vermenigvuldigen?
        D) getallen delen?
        E) getal ophogen?
        F) getal verlagen?
        G) getal verdubbelen?
        H) getal halveren?
        ''')

    choice = input("Wat wil je uitrekenen?").lower()
    if choice in ("e", "f"):
        n2 = 1
    elif choice in ("g", "h"):
        n2 = 2
    elif choice in ("quit", "q"):
        quit()

    if n1 == False:
        n1 = numberInput()
    if n2 == False:
        n2 = numberInput()
    
    if choice in ("a", "e"):
        answer = addition(n1, n2)
        operator = "+"
    elif choice in ("b", "f"):
        answer = subtraction(n1, n2)
        operator = "-"
    elif choice in ("c", "g"):
        answer = multiplication(n1, n2)
        operator = "*"
    elif choice in ("d", "h"):
        answer = division(n1, n2)
        operator = "/"

    print(f"{n1} {operator} {n2} = {answer}")
    n1 = answer
    n2 = False
    firstRound = False
