import pprint

#open text file in read mode
text_file = open("input.txt", "r")
 
#read whole file to a string
data = text_file.read()
 
#close file
text_file.close()
 
# print(data)

newData = data.split("\n")

# print (newData)

'''
finalArray = []

for row in newData:
    newRow = list(map(int, row))
    finalArray.append(newRow)
'''
    
newData2 = [list(map(int, row)) for row in newData] 
    
pprint.pprint (newData2)
    
numPerimeterOpen = len(newData) * 2 + (len(newData[0]) - 2) * 2

print (numPerimeterOpen)

'''
for i in range(len(newData)):
    print (newData[i])
'''

# start first top left corner
# end last bottom right corner

startCorner =  newData2[1][1] # is always is 

endCorner = newData2[len(newData2)-2][len(newData2[0])-2] # which is newData[len(newData2)-1]

# print (startCorner)

# print (endCorner)

'''
endOfGrid = len(newData2[0]) - 2

print (endOfGrid)
'''        