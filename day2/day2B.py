# A is rock
# B is paper
# C is scissor

# X is lose
# Y is draw
# Z is win


def score(player1, outcome):
    rock = 1
    paper = 2
    scissor = 3

    lose = 0
    tie = 3
    win = 6
    
    score = 0
    
    if player1 == "A" and outcome == "X":   # rock
        score += lose
        score += scissor
    elif player1 == "A" and outcome == "Y":
        score += tie
        score += rock
    elif player1 == "A" and outcome == "Z":
        score += win
        score += paper
    elif player1 == "B" and outcome == "X": # paper
        score += lose
        score += rock
    elif player1 == "B" and outcome == "Y":
        score += tie
        score += paper
    elif player1 == "B" and outcome == "Z":
        score += win
        score += scissor
    elif player1 == "C" and outcome == "X": # scissor
        score += lose
        score += paper
    elif player1 == "C" and outcome == "Y":
        score += tie
        score += scissor
    elif player1 == "C" and outcome == "Z":
        score += win
        score += rock
    return score

#open text file in read mode
text_file = open("input2.txt", "r")
 
#read whole file to a string
data = text_file.read()
 
#close file
text_file.close()
 
# print(data)

stringArray = data.splitlines()
# print (stringArray)

total = 0
for s in stringArray:
    amount = score(s[0], s[2])
    total += amount
print (total)