import sys

# set initial step size so python does not throw errors
step = 1

# read the binary text file sent from stdin
inputstring = sys.stdin.read()

# check to see if the file is encoded in ASCII 7 or 8 bit
if(len(inputstring) % 8 == 1):
    step = 8
if(len(inputstring) % 7 == 1):
    step = 7

# split the string into 7 or 8 bit binary numbers and append them into a list
listnum = [inputstring[i:i+step] for i in range(0, len(inputstring), step)]

# delete the last element in the list (the new line character)
del listnum[-1]

# step through the list and change each element from its binary value to int
for i in range(0, len(listnum)):
    listnum[i] = int(listnum[i],2)

result = ''

# step through list again this time casting each element to a character and append that to result

for i in range(0, len(listnum)):
    result += chr(listnum[i])


# print the decoded message 

print result
