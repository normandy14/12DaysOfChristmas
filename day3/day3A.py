#open text file in read mode
text_file = open("input.txt", "r")
 
#read whole file to a string
data = text_file.read()
 
#close file
text_file.close()
 
# print(data)

stringArray = data.splitlines()

print (stringArray)

charArray = []
   
for string in stringArray:
    midpoint = int(len(string)/2)
    string1 = string[0:midpoint]
    string2 = string[midpoint:len(string)]
    
    string1Array = list(string1)
    # print (string1Array)
    
    string2Array = list(string2)
    # print (string2Array)
    
    for c in string2Array:
        if c in string1Array:
            # print (c)
            charArray.append(c)
            break

value = 0
# print (charArray)

for c in charArray:
    if c.islower():
        value += ord(c) - 96
    else:
        value += ord(c) - 38
        
print (value)
        