import random
import MLB_WP,MLB_WC,MLB_DS,MLB_LCS

wph = MLB_WP.wph
wpa = MLB_WP.wpa
teams = MLB_WP.teams

WC1W4 = 0
WC1W5 = 0
WC2W9 = 0
WC2WA = 0

DS1W13 = 0
DS1W14 = 0
DS1W15 = 0
DS1W43 = 0
DS1W44 = 0
DS1W45 = 0
DS1W53 = 0
DS1W54 = 0
DS1W55 = 0
DS2W63 = 0
DS2W64 = 0
DS2W65 = 0
DS2W93 = 0
DS2W94 = 0
DS2W95 = 0
DS2WA3 = 0
DS2WA4 = 0
DS2WA5 = 0
DS3W23 = 0
DS3W24 = 0
DS3W25 = 0
DS3W33 = 0
DS3W34 = 0
DS3W35 = 0
DS4W73 = 0
DS4W74 = 0
DS4W75 = 0
DS4W83 = 0
DS4W84 = 0
DS4W85 = 0

LCS1W14 = 0
LCS1W15 = 0
LCS1W16 = 0
LCS1W17 = 0
LCS1W24 = 0
LCS1W25 = 0
LCS1W26 = 0
LCS1W27 = 0
LCS1W34 = 0
LCS1W35 = 0
LCS1W36 = 0
LCS1W37 = 0
LCS1W44 = 0
LCS1W45 = 0
LCS1W46 = 0
LCS1W47 = 0
LCS1W54 = 0
LCS1W55 = 0
LCS1W56 = 0
LCS1W57 = 0
LCS2W64 = 0
LCS2W65 = 0
LCS2W66 = 0
LCS2W67 = 0
LCS2W74 = 0
LCS2W75 = 0
LCS2W76 = 0
LCS2W77 = 0
LCS2W84 = 0
LCS2W85 = 0
LCS2W86 = 0
LCS2W87 = 0
LCS2W94 = 0
LCS2W95 = 0
LCS2W96 = 0
LCS2W97 = 0
LCS2WA4 = 0
LCS2WA5 = 0
LCS2WA6 = 0
LCS2WA7 = 0

WSW14 = 0
WSW15 = 0
WSW16 = 0
WSW17 = 0
WSW24 = 0
WSW25 = 0
WSW26 = 0
WSW27 = 0
WSW34 = 0
WSW35 = 0
WSW36 = 0
WSW37 = 0
WSW44 = 0
WSW45 = 0
WSW46 = 0
WSW47 = 0
WSW54 = 0
WSW55 = 0
WSW56 = 0
WSW57 = 0
WSW64 = 0
WSW65 = 0
WSW66 = 0
WSW67 = 0
WSW74 = 0
WSW75 = 0
WSW76 = 0
WSW77 = 0
WSW84 = 0
WSW85 = 0
WSW86 = 0
WSW87 = 0
WSW94 = 0
WSW95 = 0
WSW96 = 0
WSW97 = 0
WSWA4 = 0
WSWA5 = 0
WSWA6 = 0
WSWA7 = 0

iterate = int(input("How many simulations would you like?"))

for i in range(0,iterate):
    WC1 = MLB_WC.WC(4,5,wph[3][4])
    WC2 = MLB_WC.WC(9,10,wph[8][9])

    if(WC1 == 4):
        WC1W4 += 1
    elif(WC1 == 5):
        WC1W5 += 1
    else:
        print("ERROR: WC1")

    if(WC2 == 9):
        WC2W9 += 1
    elif(WC2 == 10):
        WC2WA += 1
    else:
        print("ERROR: WC2")

    # Division Series winner flags
    DS1,DS1_Wins = MLB_DS.DS(1,WC1,wph[0][WC1-1],wpa[0][WC1-1])
    DS2,DS2_Wins = MLB_DS.DS(6,WC2,wph[5][WC2-1],wpa[5][WC2-1])
    DS3,DS3_Wins = MLB_DS.DS(2,3,wph[1][2],wpa[1][2])
    DS4,DS4_Wins = MLB_DS.DS(7,8,wph[6][7],wpa[6][7])

    if(DS1 == 1 and DS1_Wins == 3):
        DS1W13 += 1
    elif(DS1 == 1 and DS1_Wins == 4):
        DS1W14 += 1
    elif(DS1 == 1 and DS1_Wins == 5):
        DS1W15 += 1
    elif(DS1 == 4 and DS1_Wins == 3):
        DS1W43 += 1
    elif(DS1 == 4 and DS1_Wins == 4):
        DS1W44 += 1
    elif(DS1 == 4 and DS1_Wins == 5):
        DS1W45 += 1
    elif(DS1 == 5 and DS1_Wins == 3):
        DS1W53 += 1
    elif(DS1 == 5 and DS1_Wins == 4):
        DS1W54 += 1
    elif(DS1 == 5 and DS1_Wins == 5):
        DS1W55 += 1
    else:
        print("ERROR: DS1")

    if(DS2 == 6 and DS2_Wins == 3):
        DS2W63 += 1
    elif(DS2 == 6 and DS2_Wins == 4):
        DS2W64 += 1
    elif(DS2 == 6 and DS2_Wins == 5):
        DS2W65 += 1
    elif(DS2 == 9 and DS2_Wins == 3):
        DS2W93 += 1
    elif(DS2 == 9 and DS2_Wins == 4):
        DS2W94 += 1
    elif(DS2 == 9 and DS2_Wins == 5):
        DS2W95 += 1
    elif(DS2 == 10 and DS2_Wins == 3):
        DS2WA3 += 1
    elif(DS2 == 10 and DS2_Wins == 4):
        DS2WA4 += 1
    elif(DS2 == 10 and DS2_Wins == 5):
        DS2WA5 += 1
    else:
        print("ERROR: DS2")

    if(DS3 == 2 and DS3_Wins == 3):
        DS3W23 += 1
    elif(DS3 == 2 and DS3_Wins == 4):
        DS3W24 += 1
    elif(DS3 == 2 and DS3_Wins == 5):
        DS3W25 += 1
    elif(DS3 == 3 and DS3_Wins == 3):
        DS3W33 += 1
    elif(DS3 == 3 and DS3_Wins == 4):
        DS3W34 += 1
    elif(DS3 == 3 and DS3_Wins == 5):
        DS3W35 += 1
    else:
        print("ERROR: DS3")

    if(DS4 == 7 and DS4_Wins == 3):
        DS4W73 += 1
    elif(DS4 == 7 and DS4_Wins == 4):
        DS4W74 += 1
    elif(DS4 == 7 and DS4_Wins == 5):
        DS4W75 += 1
    elif(DS4 == 8 and DS4_Wins == 3):
        DS4W83 += 1
    elif(DS4 == 8 and DS4_Wins == 4):
        DS4W84 += 1
    elif(DS4 == 8 and DS4_Wins == 5):
        DS4W85 += 1
    else:
        print("ERROR: DS4")

    LCS1_ls = max(DS1,DS3)
    LCS1_hs = min(DS1,DS3)
    LCS2_ls = max(DS2,DS4)
    LCS2_hs = min(DS2,DS4)

    LCS1,LCS1_Wins = MLB_LCS.LCS(LCS1_hs,LCS1_ls,wph[LCS1_hs-1][LCS1_ls-1],wpa[LCS1_hs-1][LCS1_ls-1])
    LCS2,LCS2_Wins = MLB_LCS.LCS(LCS2_hs,LCS2_ls,wph[LCS2_hs-1][LCS2_ls-1],wpa[LCS2_hs-1][LCS2_ls-1])

    if(LCS1 == 1 and LCS1_Wins == 4):
        LCS1W14 += 1
    elif(LCS1 == 1 and LCS1_Wins == 5):
        LCS1W15 += 1
    elif(LCS1 == 1 and LCS1_Wins == 6):
        LCS1W16 += 1
    elif(LCS1 == 1 and LCS1_Wins == 7):
        LCS1W17 += 1
    elif(LCS1 == 2 and LCS1_Wins == 4):
        LCS1W24 += 1
    elif(LCS1 == 2 and LCS1_Wins == 5):
        LCS1W25 += 1
    elif(LCS1 == 2 and LCS1_Wins == 6):
        LCS1W26 += 1
    elif(LCS1 == 2 and LCS1_Wins == 7):
        LCS1W27 += 1
    elif(LCS1 == 3 and LCS1_Wins == 4):
        LCS1W34 += 1
    elif(LCS1 == 3 and LCS1_Wins == 5):
        LCS1W35 += 1
    elif(LCS1 == 3 and LCS1_Wins == 6):
        LCS1W36 += 1
    elif(LCS1 == 3 and LCS1_Wins == 7):
        LCS1W37 += 1
    elif(LCS1 == 4 and LCS1_Wins == 4):
        LCS1W44 += 1
    elif(LCS1 == 4 and LCS1_Wins == 5):
        LCS1W45 += 1
    elif(LCS1 == 4 and LCS1_Wins == 6):
        LCS1W46 += 1
    elif(LCS1 == 4 and LCS1_Wins == 7):
        LCS1W47 += 1
    elif(LCS1 == 5 and LCS1_Wins == 4):
        LCS1W54 += 1
    elif(LCS1 == 5 and LCS1_Wins == 5):
        LCS1W55 += 1
    elif(LCS1 == 5 and LCS1_Wins == 6):
        LCS1W56 += 1
    elif(LCS1 == 5 and LCS1_Wins == 7):
        LCS1W57 += 1
    else:
        print("ERROR: LCS1")

    if(LCS2 == 6 and LCS2_Wins == 4):
        LCS2W64 += 1
    elif(LCS2 == 6 and LCS2_Wins == 5):
        LCS2W65 += 1
    elif(LCS2 == 6 and LCS2_Wins == 6):
        LCS2W66 += 1
    elif(LCS2 == 6 and LCS2_Wins == 7):
        LCS2W67 += 1
    elif(LCS2 == 7 and LCS2_Wins == 4):
        LCS2W74 += 1
    elif(LCS2 == 7 and LCS2_Wins == 5):
        LCS2W75 += 1
    elif(LCS2 == 7 and LCS2_Wins == 6):
        LCS2W76 += 1
    elif(LCS2 == 7 and LCS2_Wins == 7):
        LCS2W77 += 1
    elif(LCS2 == 8 and LCS2_Wins == 4):
        LCS2W84 += 1
    elif(LCS2 == 8 and LCS2_Wins == 5):
        LCS2W85 += 1
    elif(LCS2 == 8 and LCS2_Wins == 6):
        LCS2W86 += 1
    elif(LCS2 == 8 and LCS2_Wins == 7):
        LCS2W87 += 1
    elif(LCS2 == 9 and LCS2_Wins == 4):
        LCS2W94 += 1
    elif(LCS2 == 9 and LCS2_Wins == 5):
        LCS2W95 += 1
    elif(LCS2 == 9 and LCS2_Wins == 6):
        LCS2W96 += 1
    elif(LCS2 == 9 and LCS2_Wins == 7):
        LCS2W97 += 1
    elif(LCS2 == 10 and LCS2_Wins == 4):
        LCS2WA4 += 1
    elif(LCS2 == 10 and LCS2_Wins == 5):
        LCS2WA5 += 1
    elif(LCS2 == 10 and LCS2_Wins == 6):
        LCS2WA6 += 1
    elif(LCS2 == 10 and LCS2_Wins == 7):
        LCS2WA7 += 1
    else:
        print("ERROR: LCS2")


    WS,WS_Wins = MLB_LCS.LCS(LCS1,LCS2,wph[LCS1-1][LCS2-1],wpa[LCS1-1][LCS2-1])

    if(WS == 1 and WS_Wins == 4):
        WSW14 += 1
    elif(WS == 1 and WS_Wins == 5):
        WSW15 += 1
    elif(WS == 1 and WS_Wins == 6):
        WSW16 += 1
    elif(WS == 1 and WS_Wins == 7):
        WSW17 += 1
    elif(WS == 2 and WS_Wins == 4):
        WSW24 += 1
    elif(WS == 2 and WS_Wins == 5):
        WSW25 += 1
    elif(WS == 2 and WS_Wins == 6):
        WSW26 += 1
    elif(WS == 2 and WS_Wins == 7):
        WSW27 += 1
    elif(WS == 3 and WS_Wins == 4):
        WSW34 += 1
    elif(WS == 3 and WS_Wins == 5):
        WSW35 += 1
    elif(WS == 3 and WS_Wins == 6):
        WSW36 += 1
    elif(WS == 3 and WS_Wins == 7):
        WSW37 += 1
    elif(WS == 4 and WS_Wins == 4):
        WSW44 += 1
    elif(WS == 4 and WS_Wins == 5):
        WSW45 += 1
    elif(WS == 4 and WS_Wins == 6):
        WSW46 += 1
    elif(WS == 4 and WS_Wins == 7):
        WSW47 += 1
    elif(WS == 5 and WS_Wins == 4):
        WSW54 += 1
    elif(WS == 5 and WS_Wins == 5):
        WSW55 += 1
    elif(WS == 5 and WS_Wins == 6):
        WSW56 += 1
    elif(WS == 5 and WS_Wins == 7):
        WSW57 += 1
    elif(WS == 6 and WS_Wins == 4):
        WSW64 += 1
    elif(WS == 6 and WS_Wins == 5):
        WSW65 += 1
    elif(WS == 6 and WS_Wins == 6):
        WSW66 += 1
    elif(WS == 6 and WS_Wins == 7):
        WSW67 += 1
    elif(WS == 7 and WS_Wins == 4):
        WSW74 += 1
    elif(WS == 7 and WS_Wins == 5):
        WSW75 += 1
    elif(WS == 7 and WS_Wins == 6):
        WSW76 += 1
    elif(WS == 7 and WS_Wins == 7):
        WSW77 += 1
    elif(WS == 8 and WS_Wins == 4):
        WSW84 += 1
    elif(WS == 8 and WS_Wins == 5):
        WSW85 += 1
    elif(WS == 8 and WS_Wins == 6):
        WSW86 += 1
    elif(WS == 8 and WS_Wins == 7):
        WSW87 += 1
    elif(WS == 9 and WS_Wins == 4):
        WSW94 += 1
    elif(WS == 9 and WS_Wins == 5):
        WSW95 += 1
    elif(WS == 9 and WS_Wins == 6):
        WSW96 += 1
    elif(WS == 9 and WS_Wins == 7):
        WSW97 += 1
    elif(WS == 10 and WS_Wins == 4):
        WSWA4 += 1
    elif(WS == 10 and WS_Wins == 5):
        WSWA5 += 1
    elif(WS == 10 and WS_Wins == 6):
        WSWA6 += 1
    elif(WS == 10 and WS_Wins == 7):
        WSWA7 += 1
    else:
        print("ERROR: WS")

WC = [0,0,0,WC1W4,WC1W5,0,0,0,WC2W9,WC2WA]
DS3 = [DS1W13,DS3W23,DS3W33,DS1W43,DS1W53,DS2W63,DS4W73,DS4W83,DS2W93,DS2WA3]
DS4 = [DS1W14,DS3W24,DS3W34,DS1W44,DS1W54,DS2W64,DS4W74,DS4W84,DS2W94,DS2WA4]
DS5 = [DS1W15,DS3W25,DS3W35,DS1W45,DS1W55,DS2W65,DS4W75,DS4W85,DS2W95,DS2WA5]
LCS4 = [LCS1W14,LCS1W24,LCS1W34,LCS1W44,LCS1W54,LCS2W64,LCS2W74,LCS2W84,LCS2W94,LCS2WA4]
LCS5 = [LCS1W15,LCS1W25,LCS1W35,LCS1W45,LCS1W55,LCS2W65,LCS2W75,LCS2W85,LCS2W95,LCS2WA5]
LCS6 = [LCS1W16,LCS1W26,LCS1W36,LCS1W46,LCS1W56,LCS2W66,LCS2W76,LCS2W86,LCS2W96,LCS2WA6]
LCS7 = [LCS1W17,LCS1W27,LCS1W37,LCS1W47,LCS1W57,LCS2W67,LCS2W77,LCS2W87,LCS2W97,LCS2WA7]
WS4 = [WSW14,WSW24,WSW34,WSW44,WSW54,WSW64,WSW74,WSW84,WSW94,WSWA4]
WS5 = [WSW15,WSW25,WSW35,WSW45,WSW55,WSW65,WSW75,WSW85,WSW95,WSWA5]
WS6 = [WSW16,WSW26,WSW36,WSW46,WSW56,WSW66,WSW76,WSW86,WSW96,WSWA6]
WS7 = [WSW17,WSW27,WSW37,WSW47,WSW57,WSW67,WSW77,WSW87,WSW97,WSWA7]

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