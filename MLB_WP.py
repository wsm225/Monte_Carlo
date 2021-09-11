
teams = []
team_wins = []
team_index = 1

# Asks the user to input each team that make the playoffs w/ their season win%
for team_index in range(0,10):
    teams.append(input("Which team is the #%d seed team?" % (team_index+1)))
    team_wins.append(float(input("What was their win percentage?")))
    print("\n")

# The following function calculates the win probability between two teams given their season win percentage.
# The function is Bill James' log5 method.
def win_prob(p,q):
    wp = (p-p*q)/(p+q-2*p*q)
    return wp

# teams = ["SFG","MIL","NYM","LAD","SDP","HOU","BOS","CHW","TBR","OAK"]
# team_wins = [0.649,0.577,0.548,0.597,0.588,0.615,0.603,0.579,0.595,0.588]

# Dictionary for home field advantage by team
hfa = {
    "BOS" : 0.036,
    "TBR" : 0.032,
    "NYY" : 0.039,
    "TOR" : 0.034,
    "BAL" : 0.031,
    "CHW" : 0.034,
    "CLE" : 0.035,
    "KCR" : 0.032,
    "MIN" : 0.031,
    "DET" : 0.031,
    "HOU" : 0.034,
    "OAK" : 0.035,
    "LAA" : 0.033,
    "SEA" : 0.032,
    "TEX" : 0.033,
    "NYM" : 0.031,
    "PHI" : 0.034,
    "WSH" : 0.034,
    "ATL" : 0.034,
    "MIA" : 0.030,
    "CHC" : 0.033,
    "MIL" : 0.033,
    "CIN" : 0.032,
    "STL" : 0.036,
    "PIT" : 0.032,
    "SFG" : 0.035,
    "LAD" : 0.036,
    "SDP" : 0.032,
    "COL" : 0.034,
    "ARI" : 0.033
}

wp1h = []
wp1a = []
wp2h = []
wp2a = []
wp3h = []
wp3a = []
wp4h = []
wp4a = []
wp5h = []
wp5a = []
wp6h = []
wp6a = []
wp7h = []
wp7a = []
wp8h = []
wp8a = []
wp9h = []
wp9a = []
wpAh = []
wpAa = []

for x in range(0,len(teams)):
    wp1h.append(win_prob(team_wins[0]+hfa[teams[0]],team_wins[x]-hfa[teams[0]]))
    wp1a.append(win_prob(team_wins[0]-hfa[teams[x]],team_wins[x]+hfa[teams[x]]))
    wp2h.append(win_prob(team_wins[1]+hfa[teams[1]],team_wins[x]-hfa[teams[1]]))
    wp2a.append(win_prob(team_wins[1]-hfa[teams[x]],team_wins[x]+hfa[teams[x]]))
    wp3h.append(win_prob(team_wins[2]+hfa[teams[2]],team_wins[x]-hfa[teams[2]]))
    wp3a.append(win_prob(team_wins[2]-hfa[teams[x]],team_wins[x]+hfa[teams[x]]))
    wp4h.append(win_prob(team_wins[3]+hfa[teams[3]],team_wins[x]-hfa[teams[3]]))
    wp4a.append(win_prob(team_wins[3]-hfa[teams[x]],team_wins[x]+hfa[teams[x]]))
    wp5h.append(win_prob(team_wins[4]+hfa[teams[4]],team_wins[x]-hfa[teams[4]]))
    wp5a.append(win_prob(team_wins[4]-hfa[teams[x]],team_wins[x]+hfa[teams[x]]))
    wp6h.append(win_prob(team_wins[5]+hfa[teams[5]],team_wins[x]-hfa[teams[5]]))
    wp6a.append(win_prob(team_wins[5]-hfa[teams[x]],team_wins[x]+hfa[teams[x]]))
    wp7h.append(win_prob(team_wins[6]+hfa[teams[6]],team_wins[x]-hfa[teams[6]]))
    wp7a.append(win_prob(team_wins[6]-hfa[teams[x]],team_wins[x]+hfa[teams[x]]))
    wp8h.append(win_prob(team_wins[7]+hfa[teams[7]],team_wins[x]-hfa[teams[7]]))
    wp8a.append(win_prob(team_wins[7]-hfa[teams[x]],team_wins[x]+hfa[teams[x]]))
    wp9h.append(win_prob(team_wins[8]+hfa[teams[8]],team_wins[x]-hfa[teams[8]]))
    wp9a.append(win_prob(team_wins[8]-hfa[teams[x]],team_wins[x]+hfa[teams[x]]))
    wpAh.append(win_prob(team_wins[9]+hfa[teams[9]],team_wins[x]-hfa[teams[9]]))
    wpAa.append(win_prob(team_wins[9]-hfa[teams[x]],team_wins[x]+hfa[teams[x]]))

# print("%s has a %3f chance of beating %s if they are the home team." % (teams[3],wp45h,teams[4]))
# print("However, if %s is the away team, they have a %3f chance of beating %s." % (teams[3],wp45a,teams[4]))

wph = [wp1h,wp2h,wp3h,wp4h,wp5h,wp6h,wp7h,wp8h,wp9h,wpAh]
wpa = [wp1a,wp2a,wp3a,wp4a,wp5a,wp6a,wp7a,wp8a,wp9a,wpAa]