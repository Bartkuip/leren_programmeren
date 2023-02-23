def solution(text, ending): #ending lengte van ending, string slicing duimpje omhoog
    return ending in text[len(ending):]

    

input1 = input("Input 1 ")
input2 = input("Input 2 ")

print(solution(input1, input2))