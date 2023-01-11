#open text file in read mode
text_file = open("input2.txt", "r")
 
#read whole file to a string
data = text_file.read()
 
#close file
text_file.close()

# print (data)
 
# print(data.split(","))

# print (data.split("\n"))

newData = data.split("\n")

newData2 = [string.split(",") for string in newData]

# print (newData2)

count = 0

for pair in newData2:
    # print (pair)
    arr1 = pair[0]
    arr2 = pair[1]
    
    # print (arr1)
    # print (arr2)
    
    numbers1 = arr1.split("-")
    numbers2 = arr2.split("-")
    
    # print (numbers1)
    # print (numbers2)
    
    
    lowerbound1 = int(numbers1[0])
    upperbound1 = int(numbers1[1])
    
    lowerbound2 = int(numbers2[0])
    upperbound2 = int(numbers2[1])
    
    '''
    print (lowerbound1)
    print (upperbound1)
    
    print (lowerbound2)
    print (upperbound2)
    '''
    
    if lowerbound1 >= lowerbound2 and lowerbound1 <= upperbound2:
        # print ("pair is {}".format(pair))
        count += 1 
    elif lowerbound2 >= lowerbound1 and lowerbound2 <= upperbound1:
        # print ("pair is {}".format(pair))
        count += 1
    elif upperbound1 >= lowerbound2 and upperbound1 <= upperbound2:
        # print ("pair is {}".format(pair))
        count += 1
    elif upperbound2 >= lowerbound1 and upperbound2 <= upperbound1:
        # print ("pair is {}".format(pair))
        count += 1

print (count)