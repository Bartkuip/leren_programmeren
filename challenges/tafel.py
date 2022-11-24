# tafel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


# for x in range(1, len(tafel) + 1):
#     print(f"Tafel van {x}")
#     for y in tafel:
#         print(f"{x} * {y} = {x * y}") 

lijst = [5, 12, 19, 27, 3]
lijst.append(25)
lijst.remove(12)
lijst.pop(0)
lijst.insert(0, 36)
lijst.clear()
for x in range(1, 4):
    lijst.append(x)
for x in range(4, 51):
    lijst.append(x)


print(lijst)
print(sum(lijst))

print(lijst[25])