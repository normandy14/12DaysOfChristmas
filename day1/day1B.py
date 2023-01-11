#open text file in read mode
text_file = open("input2.txt", "r")
 
#read whole file to a string
string = text_file.read()
 
#close file
text_file.close()

stringArray = string.splitlines()[1:len(string)]
# print (stringArray)
stringArray.append("")

tempArray = []
finalArray = []

for string in stringArray:
    if string == "":
        finalArray.append(tempArray);
        tempArray = [];
    else:
        int_ = int(string)
        tempArray.append(int_)

max_ = []
index = 0;

for i, array in enumerate(finalArray):
    sum_ = sum(array)
    # print (sum_)
    max_.append(sum_)
        
 
max_.sort()
max_ = max_[len(max_)-3:len(max_)]
print (max_)
amount = sum(max_)
print (amount)