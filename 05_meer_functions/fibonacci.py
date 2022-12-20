fiboList = [0,1]
def fibonacci(input):
    a, b = 0, 1
    for x in range(input):
        new = a + b
        a = b
        b = new
        fiboList.append(new)
    return
userInput = int(input("Hoeveel getallen?"))
fibonacci(userInput)
print(fiboList)

lengte = len(fiboList)
print(f"De laatste 2 gedeeld door elkaar: {fiboList[lengte - 1] / fiboList[lengte - 2]}")
