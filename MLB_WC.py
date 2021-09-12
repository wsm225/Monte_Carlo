import random

def WC(hs,ls,wp):
    
    # Generates random numbers for wild card games
    WC_rand = random.random()

    # Simulates the wild card by comparing the compliment of the win probability of the winning team to the random number.
    # If the random number is less than this compliment then the lower seed wins otherwise the higher seed wins. The seed
    # value is returned as a result.
    if(WC_rand < 1 - wp): 
        return ls
    else:
        return hs
