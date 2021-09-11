import random

def WC(hs,ls,wp):
    # Generates random numbers for wild card games
    WC_rand = random.random()
    # If the random number is less than the proabibility that team 5 will beat team 4 then the winner flag for team 5
    # will be set to true otherwise the flag for team 4 will be set to true
    if(WC_rand < 1 - wp): 
        return ls
    else:
        return hs