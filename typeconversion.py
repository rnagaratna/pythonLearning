print(5+5.6) # implicit type conversion


# Explicit type conversion

print(type(int("4"))) # STR to INT
print(type(str(6.7))) # FLOAT to STR / INT to STR



fnum = input('Enter first number') #'2'
snum = input('Enter second number') #'2'
result = int(fnum) + int(snum) #4
print(result) #4
print(type(fnum)) # o/p - <class 'str'> # typeconversion in python doesn't change the original data, it creates new value and we work on that new value.
