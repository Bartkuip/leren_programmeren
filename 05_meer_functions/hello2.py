def halloWereld(y):
    end = ""
    for x in range(1, y + 1):
        end += f"Hello from function town {x}\n!"
    return end    

userInput = int(input("Hoeveel?"))
print(halloWereld(userInput))
