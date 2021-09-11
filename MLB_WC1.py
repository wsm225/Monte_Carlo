import random

def WC1(wp45,wp9A):
    # Generates random numbers for wild card games
    WC1_rand = random.random()
    WC2_rand = random.random()
    # If the random number is less than the proabibility that team 5 will beat team 4 then the winner flag for team 5
    # will be set to true otherwise the flag for team 4 will be set to true
    if(WC1_rand < 1 - wp45 and WC2_rand < 1 - wp9A): 
        return "5A"
    elif(WC1_rand < 1 - wp45 and WC2_rand >= 1- wp9A):
        return "59"
    elif(WC1_rand >= 1 - wp45 and WC2_rand < 1 - wp9A):
        return "4A"
    elif(WC1_rand >= 1 - wp45 and WC2_rand >= 1 - wp9A):
        return "49"
    else:
        return "ERROR"