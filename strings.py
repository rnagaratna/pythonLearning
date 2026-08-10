# Strings - collection of character which are unicodes (not ascii)

### Creation of string
s1 = "Hello" 
s2 = 'Hello'
s3 = """
Hello
World
"""
s4 = '''
Okay
Google
'''

s5 = "it's raining outside"
s6 = 'He told "it is a good time"'
print(s6)

s7 = str('okay')
s8 = str(4)
print(s8)


### Accessing substrings from a string
s9 = "Hello World"
for i in s9:
    print(i)

for i in range(0,len(s9)):
    print(s9[i])

print(s9[10])

# Negative indexing
print()
s9 = "Hello World"
print(s9[-1])
print(s9[-2])
print(s9[-3])


# slicing
s9 = "Hello World"
print(s9[0:5])
print(s9[2:3])
print(s9[3:])
print(s9[:7])
print(s9[:])
print(s9[2:len(s9):2])
print(s9[6:0:-1])
print(s9[::-1]) # reversing a string


# slicing with negative indexing
s9 = "Hello World"
print(s9[-5:-1])
print(s9[-1:-7:-1])


### Editing and deleting in strings
s = "hello world"
# s[0] = 'H' -----> This throws error because python strings are immutable
# print(s)

del s
# print(s)  ---> This throws error because s is already deleted


### Operations on strings
# Airthmatic operation - addition and multiplication
print('delhi'+' bangalore')
print('delhi ' * 5)

# Relational operation (comapring strings lexiographically -> comparing based on ASCII values)
print('delhi' == 'mumbai')
print('delhi' == 'delhi')
print('delhi' > 'pune')
print('D' > 'd')


# Logical operation

# Empty strings are considered as FALSE
# if a string has characters, it is considered as TRUE
print('' and 'hello') # similar to 0 and 1, answer = 0 = ''
print('' or 'hello') # similar to 0 or 1, answer = 1 = 'hello'

print('hello' and 'world') # Answer = world, because world is checked at last 
print('hello' or 'world') # Answer = hello, because if one is TRUE in OR, the entire equation will be TRUE, hence it doesn't check the next one

print(not '')
print(not 'hello')



# Loops
for i in 'hello':
    print(i)

for i in 'delhi':
    print('delhi') # prints pune 5 times


# Membership operation
print('d' in 'Delhi')
print('D' not in 'Delhi')






#######
# FUNCTIONS with STRING
#######


# Common Function
s = "helloworld"
print(len(s))
print(max(s))
print(min(s))
print(sorted(s))
print(sorted(s, reverse=True))


# String Functions
s = "hello World is tHe anSWer. okay"
print(s.capitalize()) # only the first letter will be capital
print(s.title()) # First letter of every word will be capital
print(s.upper())
print(s.lower())
print(s.swapcase())

s = "tejas hegde is my name ej"
print(s.count('e'))
print(s.count('ej'))
print(s.find('ej')) # gives the first position of ej
print(s.find('x')) # gives -1 because x is not in the string
print(s.index('e')) # gives the first position of e
# print(s.index('x')) # throws error
# if a char is not present in the string and if index is used it throws error unlike find which gives -1

print(s.endswith('j'))
print(s.endswith('js'))
print(s.startswith('how'))



name = 'tejas'
gender = 'male'
sen1 = "my name is {} and gender is {}".format(name.capitalize(), gender)
sen2 = "my name is {} and gender is {}".format(gender, name.capitalize())
sen3 = "my name is {1} and gender is {0}".format(name.capitalize(), gender)
sen4 = "my name is {1} and gender is {0}".format(gender, name.capitalize())
print(sen1, sen2, sen3, sen4, sep="\n")



print("abcd123".isalnum())
print("abcd123%".isalnum())
print("abcd".isalpha())
print("abcd123".isdigit())
print("123".isdigit())
print("1name".isidentifier())


# SPLIT and JOIN
sen = "hi my name is tejas i am hellijiam"
print(sen.split())
print(sen.split("i"))

l = ['himng', 'my', 'nam dade', 'is', 'tasdejas', 'cdsi', 'am', 'hellijiam']
print(" ".join(l))
print(",".join(l))


# Replace
s = "hi my name is hello world"
print(s.replace('hell','heaven'))


# Strip
x = "               Hello            world"
print(x.strip())
