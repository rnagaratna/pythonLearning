# sets and set theory

# Set is an unordered collection of items. 
# Everyset element is unique and must be immutable.
# However sets are mutable

# Characteristics
# 1. unordered
# 2. mutable
# 3. no Duplicates
# 4. can't contain mutable datatypes
# 5. sets are mutable 


### Creating sets

s = {} # this doesn't create set, this creates a dictoinary
print(type(s))

s = set() # this creates a set
print(type(s))
print(s)

s = {1,2} # 1D set
print(s)

# s = {1,2,{3,4}} --> This throws error because set inside a set. Set is mutable and it cant be a element of set

s = {1,2.3,True,'hello'} 
print(s) # output = {1, 2.3, 'hello'}, since sets doesn't allow duplicates and true is considered as 1 in python, true is not printed

s = {1,2.3,'okay',(4,5.6)} # tuple is immutable and it can be element
print(s)

s = set([1,2,3]) # this creates a set with element {1,2,3}
print(s) 
s = set((1,2,3))
print(s)

s1 = {1,2,3}
s2 = {2,1,3}
print(s1 == s2) # True - because tuple is unordered



### Accessing the elements - elements can't be accessed by indexing or slicing


### Editing the items - not allowed - Indexing doesn't work hence editing also won't work


### Adding/Updating items into set
# update adds multiple elements to sets whereas add adds only one element to a set
s = {1,2,3,4}
s.add(5) # Position of the addition can't be controlled
print(s)

s.update([5,6,7]) #adds multiple items to the set
print(s)
s.update((8,9)) #adds multiple items to the set
print(s)
s.add((10,11)) # adds tuple (10,11)
print(s)
# s.add([1,2,3]) --> this throws error
# print(s)


### Deleting set
s = {12,32,32}
del s
# print(s) --> throws error
# can't delete a perticular element from the set through indexing


s = {1,2,3,4,5}
s.discard(5) # discards the particular element
print(s)
s.discard(10) # doesn't throw error even if the element is not present

s = {1,2,3,4,5}
s.remove(5)
print(s)
# s.remove(10) ---> this throws error

s = {1,2,3,4,5}
s.pop() # it deletes an item randomly
print(s)

s = {1,2,3,4,5}
s.clear() # the list will get emptied
print(s)









############ OPERATIONS #############

## UNION operation( | )
s1 = {1,2,3,4,5}
s2 = {4,5,6,7}
print(s1 | s2)

## INTERSECTION ( & )
print(s1 & s2)

## DIFFERENCE ( - )
print(s1 - s2) # those in s1 which are not in s2
print(s2 - s1) # those in s2 which are not in s1

## SYMMETRIC DIFFERENCE ( ^ )
# prints everything except the commons
print(s1 ^ s2)

## membership operation
print(1 in s1)
print(6 not in s2)

## iteration
for i in s1:
    print(i)







############### FUNCTIONS ############

print(len(s1))
print(sum(s1))
print(min(s1))
print(max(s1))
print(sorted(s1, reverse=True)) ## Gives the result in List

s1 = {1,2,3,4,5}
s2 = {4,5,6,7}
print(s1.union(s2)) # s1 | s2

s1.update(s2) # s1 = s1 | s2
print(s1)
print(s2)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7}
s1.intersection(s2) # s1 & s2
s1.intersection_update(s2) # s1 = s1 & s2

"""

difference and difference_update
symmetric_difference and symmetric_difference_update

"""

# isdisjoint / issubset / issuperset
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.isdisjoint(s2)) # False

s1 = {1,2,3,4,5}
s2 = {6,7}
print(s1.isdisjoint(s2)) # True

s1 = {1,2,3,4,5}
s2 = {4,5}
print(s1.issubset(s2)) # S1 is not the subset of S2
print(s2.issubset(s1)) # S2 is the subset of S1

print(s1.issuperset(s2)) # s1 is superset of s1

s1 = {1,2,4}
s2 = s1.copy() #shallow copy



########### FROZEN SET ############
# It is an immutable version of python set

fs1 = frozenset([1,2,3])
fs2 = frozenset((1,2,3))
fs3 = frozenset({1,2,3})
print(fs1, fs2, fs3, sep="\n")

# all read functions work and write functions won't work on frozenset
# union, intersection, diff, symmetric diff, issubset, isdisjoint, issuperset - all works with frozenset
# add and delete functions donot work - pop, remove, discard, update, add
# use frozen set when the application is read only

fs = frozenset([1,2,frozenset[3,4]]) # 2D frozenset
print(fs)




############# Comprehension ##############
res = {i**2 for i in range(1,11)}
print(res)





### How indexing works in sets

# it is based on HASHING
# hash function
# it held in finding out the index position where the data has to be stored - this changes the order of the items in the set - hence it becomes unordered

# in array, searching happens in o(n)
# whereas in sets (and also in dictionary), it happens in o(1)

s = {1,4,12,43,54,15}
print(s)
