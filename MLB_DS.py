import random
import MLB_WP

# Takes in the seeds of the two teams along with the number of wins each has currently in the series and outputs the seed of the series winner.
def DS(hs,ls,wfh,wfl):
    # For a list of random numbers
    DS_rand = []

    # Counts the number of wins in the series
    DS_Winsx = 0 + wfh
    DS_Winsy = 0 + wfl

    # Looks up the win probability for the higher seeded team for home and away games
    wph = MLB_WP.wph[hs-1][ls-1]
    wpa = MLB_WP.wpa[hs-1][ls-1]

    # Creates a list of random numbers
    for x in range(1,6):
        DS_rand.append(random.random())

    # Runs the simulation for the series and increments the win count for the winning team
    for x in range(0,5-(wfh+wfl)):

        # Checks who has home field advantage. Games 1,2,&5 are played at the home of the higher seed while the rest are 
        # played at the home of the lower seed.
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
        
        # Counts the number of games played
        DS_Games = DS_Winsx + DS_Winsy

        # Checks if either team has won 3 games and returns the seed of the team that does and how many games were played
        if(DS_Winsx == 3 or wfh == 3):
            return hs,DS_Games
        elif(DS_Winsy == 3 or wfl == 3):
            return ls,DS_Games
        else:
            continue
