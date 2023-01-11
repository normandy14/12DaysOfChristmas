#open text file in read mode
text_file = open("input2.txt", "r")
 
#read whole file to a string
data = text_file.read()
 
#close file
text_file.close()
 
# print(data)

stringArray = data.splitlines()

# print (stringArray)

arrayOfChars = []

stringOf3Array = []

multiples = int(len(stringArray) / 3)
# print (multiples)

for i in range(multiples):
    stringsOf3 = stringArray[i*3:(i*3)+3]
    # print (stringsOf3)
    stringOf3Array.append(stringsOf3)
    
# print (stringOf3Array)

for arrayOf3 in stringOf3Array:
    # print (arrayOf3)
    string1 = arrayOf3[0]
    string2 = arrayOf3[1]
    string3 = arrayOf3[2]
    
    charArray1 = list(string1)
    charArray2 = list(string2)
    charArray3 = list(string3)
    
    # print (charArray1)
    # print (charArray2)
    # print (charArray3)
    
    for c in charArray1:
        if c in charArray2 and c in charArray3:
            # print (c)
            arrayOfChars.append(c)
            break

# print (arrayOfChars)

value = 0

for c in arrayOfChars:
    if c.islower():
        value += ord(c) - 96
    else:
        value += ord(c) - 38
        
print (value)