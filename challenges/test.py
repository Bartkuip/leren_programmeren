i = 0
while True:
    quit = input("Do you want to quit? ")
    if quit in ["yes","y","quit","ja","j"]:
        print("Bedankt voor je tijd")
        print(f"Vraag was {i} gesteld")
        quit()
    else:
        i += 1
        print(i)