#open text file in read mode
text_file = open("input.txt", "r")
 
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
i = 0
while i < depthOfList:
    # print (i)
    item1 = newData[i][1]
    item2 = newData[i][5]
    item3 = newData[i][9]
    # print (item)
    if item1 != ' ':
        list1.append(item1)
    if item2 != ' ':
        list2.append(item2)
    if item3 != ' ':
        list3.append(item3)
    i += 1

print (list1)
print (list2)
print (list3)


newData3 = newData[depthOfList+2:len(newData)]

# print (newData3)


# 5, 12, 17
instructions = []
for move in newData3:
    instruction = []
    # print (move)
    
    move1 = move[5]
    move2 = move[12]
    move3 = move[17]
    
    # print (move1)
    # print (move2)
    # print (move3)
    
    instruction = [move1, move2, move3]
    
    # print (instruction)
    instructions.append(instruction)

# print (instructions)


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
        
    if listDest == str(1):
        listDest = list1
    elif listDest == str(2):
        listDest = list2
    elif listDest == str(3):
        listDest = list3
    
    print ("intruction = {}".format(instruction))
    print ("numToMove = {}".format(numToMove))
    print ("listSrc = {}".format(listSrc))
    print ("listDest = {}".format(listDest))
    
    i = 0
    instructionsToMove = []
    while i < int(numToMove):
        item = listSrc[i]
        # print ("item = {}".format(item))
        instructionsToMove.append(item)
        # print (instructionsToMove)
        i += 1
    instructionsToMove
    newList = listSrc[len(instructionsToMove):] #listSrc
    newList2 = instructionsToMove + listDest #listDest
    print ("newList = {}".format(newList))
    print ("newList2 = {}".format(newList2))
    
    if instruction[1] == str(1):
        list1 = newList
    elif instruction[1] == str(2):
        list2 = newList
    elif instruction[1] == str(3):
        list3 = newList
    
    # print ("instruction = {}".format(instruction))
    if instruction[2] == str(1):
        list1 = newList2
    elif instruction[2] == str(2):
        list2 = newList2
    elif instruction[2] == str(3):
        list3 = newList2
    
    print (list1)
    print (list2)
    print (list3)

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