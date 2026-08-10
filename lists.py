########### LISTS ###########

# Basics:
# 1. It is a datatype to store multiple items under one names
# 2. Dynamic datatype
# 3. Helps to handle large datas of same type

# Differences between Array and Lists:
# 1. Fixed versus Dynamic Size, i.e List is Dyanamic Array
# 2. Arrays are homogeneous i.e only one data type can be stored, whereas lists are heterogeneous
# 3. Speed of execution of List is slow compared to Arrays
# 4. Lists occupy more space than Arrays

# How lists are stored in memory?
# 1. Arrays create continuous memory bloc
# 2. Whereas lists are Referential Array, i.e, list stores address of the data - since the address is stored, this removes that only homogenous data has to be stored. But this demands more space and time.

# Characteristic of list
# 1. Lists are Ordered
# 2. Lists are mutable unlike strings
# 3. heterogeneous
# 4. Items can be dulpicated
# 5. Can be nested
# 6. Dynamic
# 7. Items can be accessed
# 8. Can contain any kind of objects in list - functions, user functions, built in function etc




## Creating a list
print([]) #empty list
print([1,2,3]) #1D homogeneous
print([1,2,3,[4,6]]) #2D heterogeneous
print([[[1,2],[3,4]],[[5,6],[7,8]]]) #3D homogeneous
print([1,2,3.5,"Hello",5+8j]) #Heterogeneous
print(list('hello'))


## Accessing items from a list

# Positive and negative indexing
l = [1,2,3,4,5,6,7]
print(l[0])
print(l[4])
print(l[-1])
print(l[-5])

l = [1,2,3,[4,5]]
print(l[3])
print(l[3][0])
print(l[3][-2])

l = [[[1,2],[3,4]],[[5,6],[7,8]]]
print(l[1])
print(l[1][0][0])



# slicing
l = [1,2,3,4,5,6,7,8,9]
print(l[:3])
print(l[-3:])
print(l[::-1]) # reversing the list
print(l[0::2])



## Adding items to a list
l = [1,2,3,4]
l.append(5) # append adds ONE value at the end of the list
m = [1,2,3,4]
m.extend([5,6,7]) # extend adds MULTIPLE value at the end of the list
n = [1,2,3,4]
n.append([6,7,8]) # it appends [6,7,8] as a list within n
o = [1,2,3,4]
o.extend('delhi') # it adds d e l h i into the list as saperate items
p = [1,2,3,4]
p.append('pune') # adds pune as a single item at the end of the list
print(l,m,n,o,p,sep="\n")

l = [1,2,3,4,5]
l.insert(1,100) # insert 100 at index 1
print(l)



## Editing items in a list
# Editing with indexing
l = [1,2,3,4,5]
l[1] = 500
print(l)

# Editing with slicing
l = [1,2,3,4,5,6]
l[1:4] = [200,300,400]
print(l)

l[1:4] = [200,300]
print(l)

## Deleting items from a list (del, remove, pop, clear)
l = [1,2,3,4,5,6]
del l
# print(l) ----> This throws error because l doesn't exist anymore

l = [1,2,3,4,5,6]
del l[-1]
print(l)

l = [1,2,3,4,5,6,7]
del l[2:5]
print(l)
 
l = [1,2,3,4,5,6,7]
l.remove(3) # remove function works on values, i.e, here it removes the value 3 from the list
print(l)
# l.remove('x')   ----> This throws error since x is not in the list
# print(l)

l = [1,2,3,4,5,6,7]
l.pop(0) # removes the value at 0th index
l.pop() # if index is not mentioned, it removes the last item
print(l)

l = [1,2,3,4,5,6,7]
l.clear() # it clears the list. l will become empty
print(l)



#### Operations on list

#airthmatic - addition and multiplication
l1 = [1,2,3,4]
l2 = [5,6,7]
print(l1+l2)
print(l1*3)

#membership operator
l = [1,2,3,4,5,6,7]
print(5 in l)
print(5 not in l)

l = [1,2,3,[4,5]]
print(5 in l)
print(5 in l[-1])
print([4,5] in l)

# Loops
l1 = [1,2,3,4,5]
l2 = [3,4,5,6,7,[8,9],0]
for i in l1:
    print(i)

for i in l2:
    print(i)

l3 = [[[1,2],[3,4]],[[5,6],[7,8]]]
for i in l3:
    print(i)






############ FUNCTIONS

# Common functions - len, min, max, sorted

l = [1,2,3,4,5,6,0]
print(len(l))
print(min(l)) # acts only for homogeneous data
print(max(l))
print(sorted(l))
print(sorted(l,reverse=True))


l = [1,2,3,1,2,3,4,5,1,1,1,1,1,1]
print(l.count(1))
print(l.count(0)) # 0, doesn't throw error even if the element is not present

print(l.index(1))
print(l.index(3))
# print(l.index('x')) # Error, because not present

l.reverse() # permanently reverses the list
print(l)

# sorted is not a permanent change - temporory action
# sort is permanent
l = [1,3,1,8,3,10]
print(l)
print(sorted(l))
print(l)
l.sort()
print(l)
l.sort(reverse=True)

# Copy creates a shallow copy i.e same list at a new address
l = [1,2,3,4,5,6]
print(id(l))
m = l.copy()
print(id(m))
print(l,m)



### Traversing a list
# item wise traversing
l = [1,2,3,4,5]
for i in l:
    print(i)

# index based traversing
l = [1,2,3,4,5]
for i in range(0,len(l)):
    print(l[i])


### Disadvantages of Python lists
# slow, risky usage, eats up more memory

# Risky usage
a = [1,2,3]
b = a
print(a,b)
a.append(4)
print(a,b) #bcoz lists are mutable

a = [1,2,3]
b = a.copy()
print(a,b)
a.append(4)
print(a,b)
