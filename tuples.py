# Same as list, except that tuple is immutable whereas as lists are mutable
# tuple is immutable list

# Characteristics
# 1. Ordered
# 2. Immutable
# 3. Allows Duplicates

# Diff between Lists and Tuples: 
# 1. Syntax
# 2. Mutability
# 3. Tuples are faster than list since it is immutable
# 4. Tuples take less memory then list
# 5. Built in function is more in list
# 6. list is more error prone compared to list
# 7. Usability 


### Creating tuples
t = () # creating empty tuple

# printing tuple with one element
t = (2) # this is not a tuple
print(t)
print(type(t)) # integer

t = (2,) # this is a single element tuple # adding a comma is mandatory to become a tuple
print(t)
print(type(t)) # Tuple


t = (1,2,3,4) # homogeneous tuple
t = (1,2.5,True,'hello') # heterogeneous
t = (1,2,3,(4,5,6)) # 2D Tuple


t = tuple('world') # tuple of each letter
print(t)



### ACCESSING items from tuples
# same as lists and string
# Contents - positive indexing, negative indexing, slicing, indexing of 2D tuple

t = (1,2,3,4)
print(t[0])
print(t[-1])
print(t[0:4])
print(t[0:4:2])
print(t[-3:-1])

t = (1,2,3,(4,5))
print(t[-1][0])


### Editing items in tuple
t = (1,2,3)
# t[1] = 100 --> Throws error


### Adding items in tuple --> can't be done because tuples are immutable

### Deleting tuples 
# entire tuple can be deleted, single element/subtuple cannot be deleted
del t


### Operations of tuples
# addition and multiplication
t1 = (1,2,3,4)
t2 = (5,6,7)
print(t1+t2)
print(t1*3)

# membership operator
print(2 in t1)
print(5 not in t2)

# iteration
for i in t1:
    print(i)




### Function

t1 = (1,2,3,4)
print(len(t1))
print(sum(t1))
print(min(t1))
print(max(t1))
print(sorted(t1,reverse=True))

t = (1,2,3,4,5,2,3,4,1,4,2,3)
print(t.count(4))
print(t.count(10)) # answer = 0

print(t.index(4))
# print(t.index(10)) # throws error since 10 is not present



###### TUPLE UNPACKING ##########

a,b,c = (1,2,3)
print(a,b,c)

# a,b = (1,2,3)  --> Gives error
# print(a,b)

a = 1; b= 2
a,b = b,a
print(a,b)

a,b,*others = (1,'okay',3,4,'hello') #(1 --> a), ('okay' --> b), ([3,4,'hello'] --> others) # the left over elements after assigning to a,b will be stored in others in the form of a list []
print(a,b,others)


# ZIP function
a = (1,2,3,4)
b = (5,6,7,8)
print(list(zip(a,b)))
print(tuple(zip(a,b)))


res = (i for i in range(0,101) if i%5 == 0) ## TUPLE comprehension
print(tuple(res))
