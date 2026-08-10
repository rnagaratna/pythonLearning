# Creating a new file and doing 'w' operation


file = "fileHandling1/sample1.txt"


f = open(file,'w')
f.write("Hello World")
f.close()
# f.write('hello') # throws error, since file is closed this will not work


# this erases the previous content of the file and writes the new content - if we try to write on the existing file
f = open(file,'w')
f.write("\nhow are you doing??")
f.close()

# Write multiline strings
f = open(file,'w')
f.write("Okay Google\n")
f.write("how are you doing?\n")
f.close()


# Write in a file which is already present
f = open(file,'a') # append mode
f.write("I am fine\nI am doing great\n\n")
f.close()



# Writing large number of lines
l = ['hello\n','hi\n','how are you?\n\n','what are you doing?\n','i am fine\n']
f = open(file,'a')
f.writelines(l)
f.close()


### Reading from file
# read = Reads entire file at a time
# readline = reads file line by line
f = open(file, 'r')
s = f.read()
f.close()
print(s)

# reading only 15 character
f = open(file,'r')
s = f.read(15) # reads only 15 character
print(s)
f.close()


# readline()
print()
f = open(file, 'r')
s1 = f.readline()
s2 = f.readline()
print(s1, s2, sep = "")
f.close()


print("Readlines using loops")
# reading all lines from the file
f = open(file, 'r')
while True: 
    data = f.readline()
    if data == "":
        break
    else: print(data,end="")
f.close()






# Using context manager "with" - this closes the file automaticatally

file = "fileHandling1/sample2.txt"
with open(file,'w') as f:
    f.write("This is abcd\nsample2 file\nto check the WITH function\nThis closes the file automatically")

with open(file,'r') as f:
    x = f.read()
print(x)

with open(file,'r') as f:
    print(f.read(10))
    print(f.read(10)) # this reads the next 10 character and the the initial 10

    # this helps to read very big files in memory

bigL = ["hello world\n" for i in range(500)]
bigL.insert(0,'1\n')
newFileHandle = open("fileHandling1/newfile.txt",'w')

with open(file,'w') as f:
    f.writelines(bigL)

with open(file,'r') as f:
    tempSize = 10

    data = f.read(tempSize)
    while len(data) > 0: # there are strings
        newFileHandle.write(data)
        data = f.read(tempSize)

newFileHandle.close()


### 
bigL = ["hello world\n" for i in range(500)]
with open(file,'w') as f:
    f.writelines(bigL)

with open(file,'r') as f:
    chunkSize = 10
    while len(f.read(chunkSize)) > 0:
        print(f.rear(chunkSize),end='***')
        f.read(chunkSize)
        
    



###### SEEK and TELL function
# f.tell() - tells the index from where the processing has to start

file = "fileHandling1/sample1.txt"
with open(file,'r') as f:
    f.read(9)
    print(f.tell())

# f.seek() - the cursor(the result of tell) can be set to any position

print()
file = "fileHandling1/sample1.txt"
with open(file,'r') as f:
    print(f.read(9))
    print(f.tell())
    f.seek(0) # resetting the index to 0
    print(f.tell())
    print(f.read(9))
    f.seek(18)
    print(f.tell())
    print(f.read())


## Using seek while writting onto the file
file = "fileHandling1/sample3.txt"
with open(file,'w') as f:
    f.write("Hello")
    f.seek(0) # cursor reset to 0
    f.write('X') # H will be replaced by X
