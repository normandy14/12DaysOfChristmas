#open text file in read mode
text_file = open("input2.txt", "r")
 
#read whole file to a string
data = text_file.read()
 
#close file
text_file.close()
 
# print(data)

newData = data.split("\n")

# print (newData)


finalArray = []

for string in newData:
    # print (string)
    for i in range(len(string)-3):
        sub4 = string[i:i+4]
        # print (sub4)
        if len(sub4) == len(set(sub4)):
            # print (i + 4)
            # print (sub4)
            finalArray.append(i + 4)
            break
            
print (finalArray)
# finalStr = ' '.join(finalArray)
# print (finalStr)