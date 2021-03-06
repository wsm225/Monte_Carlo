import random
import MLB_WP

def WC(hs,ls,wf):
    
    # Generates random numbers for wild card games
    WC_rand = random.random()

    # Assuming win flag (wf) is set to "x", simulates the wild card by comparing the compliment of the win probability of the winning team to the
    # random number. If the random number is less than this compliment then the lower seed wins otherwise the higher seed wins. The seed
    # value is returned as a result. When wf is set to "h" or "a" the function will return the seed of that winner.
    if(wf == 0):
        if(WC_rand < 1 - wp): 
            return ls
        else:
            return hs
    elif(wf == 4 or wf == 9):
        return hs
    else:
        return ls
