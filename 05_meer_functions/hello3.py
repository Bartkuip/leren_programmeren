def halloWereld(i):
    for x in range(1, 11):
        print(f"{x} * {i} = {x * i}")
    return

userInput = int(input("Hoeveel?"))
print(halloWereld(userInput))