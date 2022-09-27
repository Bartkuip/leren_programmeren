scoreE = int(input("Wat is score: E"))
scoreP = int(input("Wat is score: P"))
scoreO = int(input("Wat is score: O"))
scoreS = int(input("Wat is score: S"))
totalScore = scoreE + scoreP - scoreO - scoreS

if scoreP == 8 and scoreE > 4 and scoreO == 0 and scoreS == 0:
    print("GOED!")
elif scoreS == 0 and totalScore > 7 and totalScore < 13 or scoreS == 1 and totalScore > 9:
    print("VOLDOENDE!")
else: 
    print("NIET GOED EN NIET VOLDOENDE!")
