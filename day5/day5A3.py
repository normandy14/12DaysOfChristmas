#open text file in read mode
text_file = open("input2.txt", "r")
 
#read whole file to a string
data = text_file.read()
 
#close file
text_file.close()

# print (data)

# How many lists in file?

newData = data.split("\n")

# print (newData)

inputMaxIndex = 0

for i, line in enumerate(newData):
    # print (i)
    # print (line)
    if line == "":
        inputMaxIndex = i

# print (inputMaxIndex)

newData2 = newData[0:inputMaxIndex-1]
# print (newData2)


depthOfList = 0
for string in newData2:   
    # print (string)
    depthOfList += 1

#  print (depthOfList)

# 1, 5, 9
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []

i = 0
while i < depthOfList:
    # print (i)
    item1 = newData[i][1]
    item2 = newData[i][5]
    item3 = newData[i][9]
    item4 = newData[i][13]
    item5 = newData[i][17]
    item6 = newData[i][21]
    item7 = newData[i][25]
    item8 = newData[i][29]
    item9 = newData[i][33]
    # print (item)
    if item1 != ' ':
        list1.append(item1)
    if item2 != ' ':
        list2.append(item2)
    if item3 != ' ':
        list3.append(item3)
    if item4 != ' ':
        list4.append(item4)
    if item5 != ' ':
        list5.append(item5)
    if item6 != ' ':
        list6.append(item6)
    if item7 != ' ':
        list7.append(item7)
    if item8 != ' ':
        list8.append(item8)
    if item9 != ' ':
        list9.append(item9)
    i += 1

print (list1)
print (list2)
print (list3)
print (list4)
print (list5)
print (list6)
print (list7)
print (list8)
print (list9)

newData3 = newData[depthOfList+2:len(newData)]

# print (newData3)


# 5, 12, 17
instructions = []
for move in newData3:
    instruction = []
    # print (move)
    
    try:
        e = int(move[5:7])
        move1 = move[5:7]
        move2 = move[13]
        move3 = move[18]
    except:
        move1 = move[5]
        move2 = move[12]
        move3 = move[17]
    
    # print (move1)
    # print (move2)
    # print (move3)
    
    instruction = [move1, move2, move3]
    
    # print (instruction)
    instructions.append(instruction)

print (instructions)


for instruction in instructions:
    numToMove = instruction[0]
    listSrc = instruction[1]
    listDest = instruction[2]
    # print (listSrc)
    # print (listDest)
    
    if listSrc == str(1):
        listSrc = list1
    elif listSrc == str(2):
        listSrc = list2
    elif listSrc == str(3):
        listSrc = list3
    elif listSrc == str(4):
        listSrc = list4
    elif listSrc == str(5):
        listSrc = list5
    elif listSrc == str(6):
        listSrc = list6
    elif listSrc == str(7):
        listSrc = list7
    elif listSrc == str(8):
        listSrc = list8
    elif listSrc == str(9):
        listSrc = list9
        
    if listDest == str(1):
        listDest = list1
    elif listDest == str(2):
        listDest = list2
    elif listDest == str(3):
        listDest = list3
    elif listDest == str(4):
        listDest = list4
    elif listDest == str(5):
        listDest = list5
    elif listDest == str(6):
        listDest = list6
    elif listDest == str(7):
        listDest = list7
    elif listDest == str(8):
        listDest = list8
    elif listDest == str(9):
        listDest = list9
    
    print ("intruction = {}".format(instruction))
    print ("numToMove = {}".format(numToMove))
    print ("listSrc = {}".format(listSrc))
    print ("listDest = {}".format(listDest))
    
    i = 0
    instructionsToMove = []
    while i < int(numToMove) and int(numToMove) <= len(listSrc):
        item = listSrc[i]
        # print ("item = {}".format(item))
        instructionsToMove.append(item)
        # print (instructionsToMove)
        i += 1
    newList = listSrc[len(instructionsToMove):] #listSrc
    newList2 = instructionsToMove + listDest #listDest
    print (instructionsToMove)
    print (listDest)
    print ("newList = {}".format(newList))
    print ("newList2 = {}".format(newList2))
    
    if instruction[1] == str(1):
        list1 = newList
    elif instruction[1] == str(2):
        list2 = newList
    elif instruction[1] == str(3):
        list3 = newList
    elif instruction[1] == str(4):
        list4 = newList
    elif instruction[1] == str(5):
        list5 = newList
    elif instruction[1] == str(6):
        list6 = newList
    elif instruction[1] == str(7):
        list7 = newList
    elif instruction[1] == str(8):
        list8 = newList
    elif instruction[1] == str(9):
        list9 = newList

    
    # print ("instruction = {}".format(instruction))
    if instruction[2] == str(1):
        list1 = newList2
    elif instruction[2] == str(2):
        list2 = newList2
    elif instruction[2] == str(3):
        list3 = newList2
    elif instruction[2] == str(4):
        list4 = newList2
    elif instruction[2] == str(5):
        list5 = newList2
    elif instruction[2] == str(6):
        list6 = newList2
    elif instruction[2] == str(7):
        list7 = newList2
    elif instruction[2] == str(8):
        list8 = newList2
    elif instruction[2] == str(9):
        list9 = newList2
    
    print (list1)
    print (list2)
    print (list3)
    print (list4)
    print (list5)
    print (list6)
    print (list7)
    print (list8)
    print (list9)

'''
        # print (i)
        if listSrc[i] == " ":
            item = listSrc[i + 1]
            i += 1
        else:
            item = listSrc[i]
            # print (item)
            i += 1
        instructionsToMove.append(item)
    # print (instructionsToMove)
    newList = instructionsToMove + listDest
    # print (newList)
    newList2 = []
    i = 0
    while i < len(newList):
        item = newList[i]
        if item != " ":
            newList2.append(item)
        i += 1
    print (newList2)
    # newList2 == list1 or list2 or list3

print (list1)
print (list2)
print (list3)

'''