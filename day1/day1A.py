#open text file in read mode
text_file = open("input2.txt", "r")
 
#read whole file to a string
string = text_file.read()
 
#close file
text_file.close()

stringArray = string.splitlines()[1:len(string)]

tempArray = []
finalArray = []

for string in stringArray:
    if string == "":
        finalArray.append(tempArray);
        tempArray = [];
    else:
        int_ = int(string)
        tempArray.append(int_)

max_ = 0
index = 0;

for i, array in enumerate(finalArray):
    sum_ = sum(array)
    if sum_ > max_:
        max_ = sum_
        index = i + 1
        
print (index, max_)
    
    