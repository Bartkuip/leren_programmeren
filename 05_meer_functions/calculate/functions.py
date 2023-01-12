def addition(n1 : int, n2 : int):
    answer = n1 + n2
    return answer

def subtraction(n1 : int, n2 : int):
    answer = n1 - n2
    return answer

def multiplication(n1 : int, n2 : int):
    answer = n1 * n2
    return answer

def division(n1 : int, n2 : int):
    answer = n1 / n2
    return answer

def numberInput():
    while True:
        try:
            number = float( input("Voer een nummer in: "))
            break
        except:
            print("Voer een geldig nummer in.")
    return number
