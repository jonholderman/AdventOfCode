import re

# Elf Scoring
#
# Paper = 2 / B / Y
# Rock = 1 / A / X
# Scissors = 3 / C / Z
#
# Loss = 0
# Draw = 3
# Win = 6
#
# Rock(1) > Scissors(3)
# Scissors(3) > Paper(2)
# Paper(2) > Rock (1)
#

dict_lookup = {
    "A X": [4, "Draw"],
    'A Y': [8, "Win"],
    'A Z': [3, "Loss"],
    'B X': [1, "Loss"],
    'B Y': [5, "Draw"],
    'B Z': [9, "Win"],
    'C X': [7, "Win"],
    'C Y': [2, "Loss"],
    'C Z': [6, "Draw"]
}

scoreSum = 0
numberOfWins = 0
numberOfLoses = 0
numberOfDraws = 0

regex = r"([ABC])\s([XYZ])"

with open('input.txt') as file:
    for index, line in enumerate(file):

        line_result = dict_lookup[line.strip()]

        scoreSum = scoreSum + line_result[0]

        if(line_result[1] == "Draw"):
            numberOfDraws = numberOfDraws + 1
        elif(line_result[1] == "Loss"):
            numberOfLoses = numberOfLoses + 1
        elif(line_result[1] == "Win"):
            numberOfWins = numberOfWins + 1

        #result = re.search(regex, line)
        #opp_move = result.group(1)
        #my_move = result.group(2)
        #if(opp_move == 'A'):
        #print("Line {}: {}".format(index, line.strip()))

print("Total Score: {}".format(scoreSum))
print("Total Wins: {}".format(numberOfWins))
print("Total Draws: {}".format(numberOfDraws))
print("Total Loses: {}".format(numberOfLoses))