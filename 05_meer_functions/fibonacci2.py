fiboList = [0, 1]
def fibonacci(a, b, n):
    if n == 2:
        return 1
    else:
        new = a + b
        a = b
        b = new
        fiboList.append(new)
        return n * fibonacci(a, new, n-1)

userInput = int(input("Hoeveel?"))
fibonacci(0, 1, userInput)
print(fiboList)