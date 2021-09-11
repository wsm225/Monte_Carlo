# Monte_Carlo

Overview:

This is a simple Python code I developed that can run a Monte Carlo simulation. According to Investopedia, a Monte Carlo simulation is a
simulation that is "used to model the probability of different outcomes in a process that cannot easily be predicted due to the intervention of
random variables." For this code, it is simulating the entirity of the Major League Baseball postseason in which 10 teams compete to win the
World Series and be crowned the best team in baseball for that particular year. The program begins by asking the user to input all of the teams
that will be competing along with their win percentage in order (top 5 spots go to the league in which the winningest team that year belongs to
with the top 3 spots going to the division winners followed by 2 non-division winning wild card teams. Next 5 goes to the other league following
the same order). Once all teams are entered the program will then ask the user for the number of simulations the user wishes to run. The program
will then start stepping through each part of the postseason keeping track of the winners of each round and the number of games required to win
the particular round (the wild card round has 1 game, the division series round has a maximum of 5 games, and the league championship and 
World Series rounds each have a maximum of 7 games). This process loops for the desired number of times at which point the systems outputs a 
report stating how many times the teams won each round which is then broken down to the frequency of how many games were played to win that 
round.

Simulation:

To determine a winner for each game the program utilizes the random package in Python which has a random function that generates a random number
between 0 and 1. The program calculates the win probability(+) for a team against their opponent using Bill James' log5 function (for more info
see: en.wikipedia.org/wiki/Log5) which is compared to the randomly generated number. Assuming the number is less than the win probability of the
lower seeded team, then that team gets a win otherwise the higher seeded team gets the win. Each round has its own module (except for the World
Series which shares the module of the league championship game) that keeps track of the number of wins and outputs the seed and number of games
when the determined number of wins is met (1 for the wild card, 3 for the division series, and 4 for the league championship and world series).

Notes:

This progam was designed primarily as means of practicing Python and as a learning opportunity for simulations in general. A lot of the math and
ideas behind this program have been used in plenty of sports statistics and sports gambling sites. However, their models tend to be more advanced
accounting for the contributions of players and venues and probably plenty of other variables. As such, the results should be taken with a grain
of salt and should not be used for life changing bets. 

(+) For the win probabilities I came up with a rough home field advantage bonus that in theory should boost the home team's win probability.
The bonus was calculated by first determining each teams all time win percentage at their current home stadium (found using retrosheet.org).
These win perecentages were then normalized to each other by dividing the win percentage of any team divided by the sum of all the win 
percentages (disclaimer: there may be a better way to calculate this bonus that doesn't involve summing percentages but for the sake of 
simplicity I opted to use this method). This bonus is then added to the win percentage of the home team and subtracted from the visiting team 
prior to the calculation of the win probability. Future updates might change the visiting team penalty to be a better reflection of that team's 
ability to win on the road.
