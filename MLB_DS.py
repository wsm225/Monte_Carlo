import random

def DS(hs,ls,wph,wpa):
    #For a list of random numbers
    DS_rand = []

    # Counts the number of wins in the series
    DS_Winsx = 0
    DS_Winsy = 0

    # Creates a list of random numbers
    for x in range(1,6):
        DS_rand.append(random.random())

    # Checks if team 4 won the previous series
    for x in range(0,5):
        if(x == 0 or x == 1 or x == 4):
            if(DS_rand[x] < 1 - wph):
                DS_Winsy += 1
            else:
                DS_Winsx += 1
        else:
            if(DS_rand[x] < 1 - wpa):
                DS_Winsy += 1
            else:
                DS_Winsx += 1
        
        DS_Wins = DS_Winsx + DS_Winsy

        if(DS_Winsx == 3):
            return hs,DS_Wins
        elif(DS_Winsy == 3):
            return ls,DS_Wins
        else:
            continue