def halloWereld(fname):
    for x in range(1, fname + 1):
        test = print(f"{x} * {x} = {x * x}")
    return test

userInput = int(input("Hoeveel?"))
print(halloWereld(userInput))