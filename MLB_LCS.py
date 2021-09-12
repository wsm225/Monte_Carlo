import random

def LCS(hs,ls,wph,wpa):
    # For a list of random numbers
    LCS_rand = []

    # Counts the number of wins in the series
    LCS_Winsx = 0
    LCS_Winsy = 0

    # Creates a list of random numbers
    for x in range(1,8):
        LCS_rand.append(random.random())

    # Runs the simulation for the series and increments the win count for the winning team
    for x in range(0,7):

        # Checks who has home field advantage. Games 1,2,6,&7 are played at the home of the higher seed while the rest are
        # played at the home of the lower seed.
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

        # Counts the number of games played in the series
        LCS_Games = LCS_Winsx + LCS_Winsy

        # Checks if either team reaches 4 wins then returns the seed and the number of games completed.
        if(LCS_Winsx == 4):
            return hs,LCS_Games
        elif(LCS_Winsy == 4):
            return ls,LCS_Games
        else:
            continue
