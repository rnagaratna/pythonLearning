# Integer 
print(8)

# Float
print(8.55)

# String
print("Hello World")

# Boolean
print(True)
print(False)

# Complex
print(5 + 6j)

# List
print([2,5,True,"Hello"])

# Tuple
print((1,2,False))

# Sets
print({1,2,"Hello"})

# Dictionary - key value pairs
print({'name':'Tejas', 'age':45, 'Gender':'M'})

# None
print(None)

# Type
print(type(3))
print(type(5.6))
print(type(True))
print(type([1,2,3]))





##########################
##       OPERATORS      ##
##########################


# airthmatic operators
print(1+2)
print(2-1)
print(1*5)
print(1/5)
print(5//3) # integer division - only keeps the integer part
print(5%2) 
print(6**2)


# Relational operators
print(4>5)
print(4<5)
print(5==6)
print(5!=6)
print(4<=5)
print(4>=5)


# Logical operators - and , or
print(1 or 0)
print(1 and 1)
print(0 or 0)
print(0 and 1)
print(not 1)
print(not 0)


# Bitwise operators - acts on each bit

# bitwise and operation
print(2 & 3) 
# answer = 2
# 2 = 010
# 3 = 011
# answer = 010 = 2

# bitwise or operation
print(2 | 3)
#answer = 3
# 2 = 010
# 3 = 011
# answer = 011 = 3

# bitwise XOR operation - same bit = 0, different bit = 1
print(2 ^ 3)
#answer = 1
# 2 = 010
# 3 = 011
# answer = 001 = 1

# bitwise not
print(~3)
#answer = 4
# 3 = 011
# answer = 100 = 4

# left shift 
print(4 >> 2) # binary pattern of 4 is being shifted by 2 places towards left
# right shift
print(4 << 2) # binary pattern of 4 is being shifted by 2 places towards right



# Assignment operators
a = 2
a += 2 # a = a+2
print(a)



# Membership operators
# in / not in
print('d' in 'delhi') # True
print('D' in 'delhi') # False
print('D' not in 'delhi') # True
print(1 in [1,2,3,4]) # True