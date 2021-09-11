import random

def LCS(hs,ls,wph,wpa):
    #For a list of random numbers
    LCS_rand = []

    # Counts the number of wins in the series
    LCS_Winsx = 0
    LCS_Winsy = 0

    # Creates a list of random numbers
    for x in range(1,8):
        LCS_rand.append(random.random())

    # Checks if team 4 won the previous series
    for x in range(0,7):
        if(x == 0 or x == 1 or x == 5 or x == 6):
            if(LCS_rand[x] < 1 - wph):
                LCS_Winsy += 1
            else:
                LCS_Winsx += 1
        else:
            if(LCS_rand[x] < 1 - wpa):
                LCS_Winsy += 1
            else:
                LCS_Winsx += 1
        
        LCS_Wins = LCS_Winsx + LCS_Winsy

        if(LCS_Winsx == 4):
            return hs,LCS_Wins
        elif(LCS_Winsy == 4):
            return ls,LCS_Wins
        else:
            continue