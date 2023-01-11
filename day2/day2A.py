# A is rock
# B is paper
# C is scissor

# X is rock
# Y is paper
# Z is scissor

def score(player1, player2):
    score = 0
    lose = 0
    tie = 3
    win = 6
    if player1 == "A" and player2 == "X":
        score += 1
        score += tie
    elif player1 == "A" and player2 == "Y":
        score += 2
        score += win
    elif player1 == "A" and player2 == "Z":
        score += 3
        score += lose
    elif player1 == "B" and player2 == "X":
        score += 1
        score += lose
    elif player1 == "B" and player2 == "Y":
        score += 2
        score += tie
    elif player1 == "B" and player2 == "Z":
        score += 3
        score += win
    elif player1 == "C" and player2 == "X":
        score += 1
        score += win
    elif player1 == "C" and player2 == "Y":
        score += 2
        score += lose
    elif player1 == "C" and player2 == "Z":
        score += 3
        score += tie
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