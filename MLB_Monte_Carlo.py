import random
import MLB_WP,MLB_WC,MLB_DS,MLB_LCS

# Stores the teams and their win perecentages calculated in the MLB_WP file into a local variable.
wph = MLB_WP.wph
wpa = MLB_WP.wpa
teams = MLB_WP.teams

# Initializes a count for every winner/game count possibility in each round of the playoffs
WCW = [0,0,0,0]
DSW = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
LCSW = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
WSW = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

iterate = int(input("How many simulations would you like? "))

# Preforms the simulation for the number of times required by the user.
for i in range(0,iterate):

    # Stores the outcome of each Wild Card game
    WC1 = MLB_WC.WC(4,5,wph[3][4])
    WC2 = MLB_WC.WC(9,10,wph[8][9])

    # Checks which team wins each game and increments the respective counter. Reports an error if an outcome is not 
    # determined.
    if(WC1 == 4):
        WCW[0] += 1
    elif(WC1 == 5):
        WCW[1] += 1
    else:
        print("ERROR: WC1")

    if(WC2 == 9):
        WCW[2] += 1
    elif(WC2 == 10):
        WCW[3] += 1
    else:
        print("ERROR: WC2")

    # Simulates the Division Series
    DS1,DS1_Wins = MLB_DS.DS(1,WC1,wph[0][WC1-1],wpa[0][WC1-1])
    DS2,DS2_Wins = MLB_DS.DS(6,WC2,wph[5][WC2-1],wpa[5][WC2-1])
    DS3,DS3_Wins = MLB_DS.DS(2,3,wph[1][2],wpa[1][2])
    DS4,DS4_Wins = MLB_DS.DS(7,8,wph[6][7],wpa[6][7])

    # Checks the outcomes of the Division Series and increments the respective counter. Returns an error if possible outcomes
    # are not achieved.
    if(DS1 == 1 and DS1_Wins == 3):
        DSW[0] += 1
    elif(DS1 == 1 and DS1_Wins == 4):
        DSW[1] += 1
    elif(DS1 == 1 and DS1_Wins == 5):
        DSW[2] += 1
    elif(DS1 == 4 and DS1_Wins == 3):
        DSW[3] += 1
    elif(DS1 == 4 and DS1_Wins == 4):
        DSW[4] += 1
    elif(DS1 == 4 and DS1_Wins == 5):
        DSW[5] += 1
    elif(DS1 == 5 and DS1_Wins == 3):
        DSW[6] += 1
    elif(DS1 == 5 and DS1_Wins == 4):
        DSW[7] += 1
    elif(DS1 == 5 and DS1_Wins == 5):
        DSW[8] += 1
    else:
        print("ERROR: DS1")

    if(DS2 == 6 and DS2_Wins == 3):
        DSW[9] += 1
    elif(DS2 == 6 and DS2_Wins == 4):
        DSW[10] += 1
    elif(DS2 == 6 and DS2_Wins == 5):
        DSW[11] += 1
    elif(DS2 == 9 and DS2_Wins == 3):
        DSW[12] += 1
    elif(DS2 == 9 and DS2_Wins == 4):
        DSW[13] += 1
    elif(DS2 == 9 and DS2_Wins == 5):
        DSW[14] += 1
    elif(DS2 == 10 and DS2_Wins == 3):
        DSW[15] += 1
    elif(DS2 == 10 and DS2_Wins == 4):
        DSW[16] += 1
    elif(DS2 == 10 and DS2_Wins == 5):
        DSW[17] += 1
    else:
        print("ERROR: DS2")

    if(DS3 == 2 and DS3_Wins == 3):
        DSW[18] += 1
    elif(DS3 == 2 and DS3_Wins == 4):
        DSW[19] += 1
    elif(DS3 == 2 and DS3_Wins == 5):
        DSW[20] += 1
    elif(DS3 == 3 and DS3_Wins == 3):
        DSW[21] += 1
    elif(DS3 == 3 and DS3_Wins == 4):
        DSW[22] += 1
    elif(DS3 == 3 and DS3_Wins == 5):
        DSW[23] += 1
    else:
        print("ERROR: DS3")

    if(DS4 == 7 and DS4_Wins == 3):
        DSW[24] += 1
    elif(DS4 == 7 and DS4_Wins == 4):
        DSW[25] += 1
    elif(DS4 == 7 and DS4_Wins == 5):
        DSW[26] += 1
    elif(DS4 == 8 and DS4_Wins == 3):
        DSW[27] += 1
    elif(DS4 == 8 and DS4_Wins == 4):
        DSW[28] += 1
    elif(DS4 == 8 and DS4_Wins == 5):
        DSW[29] += 1
    else:
        print("ERROR: DS4")

    # Ensures the lower seed has the homefield advantage
    LCS1_ls = max(DS1,DS3)
    LCS1_hs = min(DS1,DS3)
    LCS2_ls = max(DS2,DS4)
    LCS2_hs = min(DS2,DS4)

    # Simulates the League Championship Series
    LCS1,LCS1_Wins = MLB_LCS.LCS(LCS1_hs,LCS1_ls,wph[LCS1_hs-1][LCS1_ls-1],wpa[LCS1_hs-1][LCS1_ls-1])
    LCS2,LCS2_Wins = MLB_LCS.LCS(LCS2_hs,LCS2_ls,wph[LCS2_hs-1][LCS2_ls-1],wpa[LCS2_hs-1][LCS2_ls-1])

    # Checks the outcome of each League Champhionship Series and increments the respective counter. Returns an error if 
    # possible outcomes are not achieved.
    if(LCS1 == 1 and LCS1_Wins == 4):
        LCSW[0] += 1
    elif(LCS1 == 1 and LCS1_Wins == 5):
        LCSW[1] += 1
    elif(LCS1 == 1 and LCS1_Wins == 6):
        LCSW[2] += 1
    elif(LCS1 == 1 and LCS1_Wins == 7):
        LCSW[3] += 1
    elif(LCS1 == 2 and LCS1_Wins == 4):
        LCSW[4] += 1
    elif(LCS1 == 2 and LCS1_Wins == 5):
        LCSW[5] += 1
    elif(LCS1 == 2 and LCS1_Wins == 6):
        LCSW[6] += 1
    elif(LCS1 == 2 and LCS1_Wins == 7):
        LCSW[7] += 1
    elif(LCS1 == 3 and LCS1_Wins == 4):
        LCSW[8] += 1
    elif(LCS1 == 3 and LCS1_Wins == 5):
        LCSW[9] += 1
    elif(LCS1 == 3 and LCS1_Wins == 6):
        LCSW[10] += 1
    elif(LCS1 == 3 and LCS1_Wins == 7):
        LCSW[11] += 1
    elif(LCS1 == 4 and LCS1_Wins == 4):
        LCSW[12] += 1
    elif(LCS1 == 4 and LCS1_Wins == 5):
        LCSW[13] += 1
    elif(LCS1 == 4 and LCS1_Wins == 6):
        LCSW[14] += 1
    elif(LCS1 == 4 and LCS1_Wins == 7):
        LCSW[15] += 1
    elif(LCS1 == 5 and LCS1_Wins == 4):
        LCSW[16] += 1
    elif(LCS1 == 5 and LCS1_Wins == 5):
        LCSW[17] += 1
    elif(LCS1 == 5 and LCS1_Wins == 6):
        LCSW[18] += 1
    elif(LCS1 == 5 and LCS1_Wins == 7):
        LCSW[19] += 1
    else:
        print("ERROR: LCS1")

    if(LCS2 == 6 and LCS2_Wins == 4):
        LCSW[20] += 1
    elif(LCS2 == 6 and LCS2_Wins == 5):
        LCSW[21] += 1
    elif(LCS2 == 6 and LCS2_Wins == 6):
        LCSW[22] += 1
    elif(LCS2 == 6 and LCS2_Wins == 7):
        LCSW[23] += 1
    elif(LCS2 == 7 and LCS2_Wins == 4):
        LCSW[24] += 1
    elif(LCS2 == 7 and LCS2_Wins == 5):
        LCSW[25] += 1
    elif(LCS2 == 7 and LCS2_Wins == 6):
        LCSW[26] += 1
    elif(LCS2 == 7 and LCS2_Wins == 7):
        LCSW[27] += 1
    elif(LCS2 == 8 and LCS2_Wins == 4):
        LCSW[28] += 1
    elif(LCS2 == 8 and LCS2_Wins == 5):
        LCSW[29] += 1
    elif(LCS2 == 8 and LCS2_Wins == 6):
        LCSW[30] += 1
    elif(LCS2 == 8 and LCS2_Wins == 7):
        LCSW[31] += 1
    elif(LCS2 == 9 and LCS2_Wins == 4):
        LCSW[32] += 1
    elif(LCS2 == 9 and LCS2_Wins == 5):
        LCSW[33] += 1
    elif(LCS2 == 9 and LCS2_Wins == 6):
        LCSW[34] += 1
    elif(LCS2 == 9 and LCS2_Wins == 7):
        LCSW[35] += 1
    elif(LCS2 == 10 and LCS2_Wins == 4):
        LCSW[36] += 1
    elif(LCS2 == 10 and LCS2_Wins == 5):
        LCSW[37] += 1
    elif(LCS2 == 10 and LCS2_Wins == 6):
        LCSW[38] += 1
    elif(LCS2 == 10 and LCS2_Wins == 7):
        LCSW[39] += 1
    else:
        print("ERROR: LCS2")


    # Simulates the World Series
    WS,WS_Wins = MLB_LCS.LCS(LCS1,LCS2,wph[LCS1-1][LCS2-1],wpa[LCS1-1][LCS2-1])

    # Checks the outcome of each League Champhionship Series and increments the respective counter. Returns an error if 
    # possible outcomes are not achieved.
    if(WS == 1 and WS_Wins == 4):
        WSW[0] += 1
    elif(WS == 1 and WS_Wins == 5):
        WSW[1] += 1
    elif(WS == 1 and WS_Wins == 6):
        WSW[2] += 1
    elif(WS == 1 and WS_Wins == 7):
        WSW[3] += 1
    elif(WS == 2 and WS_Wins == 4):
        WSW[4] += 1
    elif(WS == 2 and WS_Wins == 5):
        WSW[5] += 1
    elif(WS == 2 and WS_Wins == 6):
        WSW[6] += 1
    elif(WS == 2 and WS_Wins == 7):
        WSW[7] += 1
    elif(WS == 3 and WS_Wins == 4):
        WSW[8] += 1
    elif(WS == 3 and WS_Wins == 5):
        WSW[9] += 1
    elif(WS == 3 and WS_Wins == 6):
        WSW[10] += 1
    elif(WS == 3 and WS_Wins == 7):
        WSW[11] += 1
    elif(WS == 4 and WS_Wins == 4):
        WSW[12] += 1
    elif(WS == 4 and WS_Wins == 5):
        WSW[13] += 1
    elif(WS == 4 and WS_Wins == 6):
        WSW[14] += 1
    elif(WS == 4 and WS_Wins == 7):
        WSW[15] += 1
    elif(WS == 5 and WS_Wins == 4):
        WSW[16] += 1
    elif(WS == 5 and WS_Wins == 5):
        WSW[17] += 1
    elif(WS == 5 and WS_Wins == 6):
        WSW[18] += 1
    elif(WS == 5 and WS_Wins == 7):
        WSW[19] += 1
    elif(WS == 6 and WS_Wins == 4):
        WSW[20] += 1
    elif(WS == 6 and WS_Wins == 5):
        WSW[21] += 1
    elif(WS == 6 and WS_Wins == 6):
        WSW[22] += 1
    elif(WS == 6 and WS_Wins == 7):
        WSW[23] += 1
    elif(WS == 7 and WS_Wins == 4):
        WSW[24] += 1
    elif(WS == 7 and WS_Wins == 5):
        WSW[25] += 1
    elif(WS == 7 and WS_Wins == 6):
        WSW[26] += 1
    elif(WS == 7 and WS_Wins == 7):
        WSW[27] += 1
    elif(WS == 8 and WS_Wins == 4):
        WSW[28] += 1
    elif(WS == 8 and WS_Wins == 5):
        WSW[29] += 1
    elif(WS == 8 and WS_Wins == 6):
        WSW[30] += 1
    elif(WS == 8 and WS_Wins == 7):
        WSW[31] += 1
    elif(WS == 9 and WS_Wins == 4):
        WSW[32] += 1
    elif(WS == 9 and WS_Wins == 5):
        WSW[33] += 1
    elif(WS == 9 and WS_Wins == 6):
        WSW[34] += 1
    elif(WS == 9 and WS_Wins == 7):
        WSW[35] += 1
    elif(WS == 10 and WS_Wins == 4):
        WSW[36] += 1
    elif(WS == 10 and WS_Wins == 5):
        WSW[37] += 1
    elif(WS == 10 and WS_Wins == 6):
        WSW[38] += 1
    elif(WS == 10 and WS_Wins == 7):
        WSW[39] += 1
    else:
        print("ERROR: WS")

# Compiles the counters for each round into new lists for quick lookup
WC = [0,0,0,WCW[0],WCW[1],0,0,0,WCW[2],WCW[3]]
DS3 = [DSW[0],DSW[18],DSW[21],DSW[3],DSW[6],DSW[9],DSW[24],DSW[27],DSW[12],DSW[15]]
DS4 = [DSW[1],DSW[19],DSW[22],DSW[4],DSW[7],DSW[10],DSW[25],DSW[28],DSW[13],DSW[16]]
DS5 = [DSW[2],DSW[20],DSW[23],DSW[5],DSW[8],DSW[11],DSW[26],DSW[29],DSW[14],DSW[17]]
LCS4 = [LCSW[0],LCSW[4],LCSW[8],LCSW[12],LCSW[16],LCSW[20],LCSW[24],LCSW[28],LCSW[32],LCSW[36]]
LCS5 = [LCSW[1],LCSW[5],LCSW[9],LCSW[13],LCSW[17],LCSW[21],LCSW[25],LCSW[29],LCSW[33],LCSW[37]]
LCS6 = [LCSW[2],LCSW[6],LCSW[10],LCSW[14],LCSW[18],LCSW[22],LCSW[26],LCSW[30],LCSW[34],LCSW[38]]
LCS7 = [LCSW[3],LCSW[7],LCSW[11],LCSW[15],LCSW[19],LCSW[23],LCSW[27],LCSW[31],LCSW[35],LCSW[39]]
WS4 = [WSW[0],WSW[4],WSW[8],WSW[12],WSW[16],WSW[20],WSW[24],WSW[28],WSW[32],WSW[36]]
WS5 = [WSW[1],WSW[5],WSW[9],WSW[13],WSW[17],WSW[21],WSW[25],WSW[29],WSW[33],WSW[37]]
WS6 = [WSW[2],WSW[6],WSW[10],WSW[14],WSW[18],WSW[22],WSW[26],WSW[30],WSW[34],WSW[38]]
WS7 = [WSW[3],WSW[7],WSW[11],WSW[15],WSW[19],WSW[23],WSW[27],WSW[31],WSW[35],WSW[39]]

# Generates a report for each team that documents the frequency of their wins. The Wild Card teams get a unique line for
# the Wild Card round.
for x in range(0,len(teams)):
    if(x == 3 or x == 4 or x == 8 or x == 9):
        print("%s chances of winning:" %(teams[x]))
        print("* Wild Card: %.2f%%" % (WC[x]/iterate*100))
        print("* Division Series: %.2f%%" % ((DS3[x]+DS4[x]+DS5[x])/iterate*100))
        print("    - in 3 games: %.2f%%" % (DS3[x]/iterate*100))
        print("    - in 4 games: %.2f%%" % (DS4[x]/iterate*100))
        print("    - in 5 games: %.2f%%" % (DS5[x]/iterate*100))
        print("* League Championship Series: %.2f%%" % ((LCS4[x]+LCS5[x]+LCS6[x]+LCS7[x])/iterate*100))
        print("    - in 4 games: %.2f%%" % (LCS4[x]/iterate*100))
        print("    - in 5 games: %.2f%%" % (LCS5[x]/iterate*100))
        print("    - in 6 games: %.2f%%" % (LCS6[x]/iterate*100))
        print("    - in 7 games: %.2f%%" % (LCS7[x]/iterate*100))
        print("* World Series: %.2f%%" % ((WS4[x]+WS5[x]+WS6[x]+WS7[x])/iterate*100))
        print("    - in 4 games: %.2f%%" % (WS4[x]/iterate*100))
        print("    - in 5 games: %.2f%%" % (WS5[x]/iterate*100))
        print("    - in 6 games: %.2f%%" % (WS6[x]/iterate*100))
        print("    - in 7 games: %.2f%%\n" % (WS7[x]/iterate*100))
    else:
        print("%s chances of winning:" %(teams[x]))
        print("* Division Series: %.2f%%" % ((DS3[x]+DS4[x]+DS5[x])/iterate*100))
        print("    - in 3 games: %.2f%%" % (DS3[x]/iterate*100))
        print("    - in 4 games: %.2f%%" % (DS4[x]/iterate*100))
        print("    - in 5 games: %.2f%%" % (DS5[x]/iterate*100))
        print("* League Championship Series: %.2f%%" % ((LCS4[x]+LCS5[x]+LCS6[x]+LCS7[x])/iterate*100))
        print("    - in 4 games: %.2f%%" % (LCS4[x]/iterate*100))
        print("    - in 5 games: %.2f%%" % (LCS5[x]/iterate*100))
        print("    - in 6 games: %.2f%%" % (LCS6[x]/iterate*100))
        print("    - in 7 games: %.2f%%" % (LCS7[x]/iterate*100))
        print("* World Series: %.2f%%" % ((WS4[x]+WS5[x]+WS6[x]+WS7[x])/iterate*100))
        print("    - in 4 games: %.2f%%" % (WS4[x]/iterate*100))
        print("    - in 5 games: %.2f%%" % (WS5[x]/iterate*100))
        print("    - in 6 games: %.2f%%" % (WS6[x]/iterate*100))
        print("    - in 7 games: %.2f%%\n" % (WS7[x]/iterate*100))
