############################
###  LIST COMPREHENSION  ###
############################


# it is a consise way of creating list
# newlist = [expression for items in iterable if condition = True]
# more efficient and powerfull, requires fewer number of lines, transforms iterative statements into formulas


# add 1 to 10 number in the list
l = []
for i in range(1,11):
    l.append(i)
print(l)

# add 1 to 10 in list using list comprehension
L = [i for i in range(1,11)]
print(L)


# scaler multiplication of a vector
v = [2,3,4]
s = -3
x = []
for i in v:
    x.append(i*s)
print(x)

# scaler multiplication of a vector using list comprehension
v = [2,3,4]
s = -3
result = [i*s for i in v]
print(result)


# Squares of the list
n = [1,2,3,4,5]
result = [i**2 for i in n]
print(result)


# all numbers divisible by 5 in range 1 to 50
print([i for i in range(1,51) if i%5 == 0])


# find languages that states with p
languages = ['python','java','c','php','c++','ruby','prompt']
result = [language for language in languages if language.startswith('p')]
print(result)


### Nested ifs with list comprehension

# make new list from myfruit if item is present in basket and also starts with 'a'
basket = ['apple','cherry','almond','guava','banana']
myfruits = ['apple','kivi','grapes','banana','almond']
# print([fruit for fruit in myfruits if fruit in basket and fruit.startswith('a')])
res = [fruit for fruit in myfruits if fruit in basket if fruit.startswith('a')]
print(res)

# print (3,3) matrix using list comprehension -> nested
res = [[j for i in range(1,4)] for j in range (1,4)] # j is outer loop, i is inner loop
print(res)

print([[[i*j*k for i in range(1,3)] for j in range(1,3)] for k in range(1,3)]) # 3D matrix


# Cartesian product
l1 = [1,2,3,4]
l2 = [5,6,7,8]
res = [i*j for i in l1 for j in l2]
print(res)







####################################################
################### ZIP FUNCTION ###################
####################################################


# it returns a zip object, which is an iterator of the tuple where the 1st item of each iterator are paired together, second item of each iterator is paired together and so on
# if the lenght of the iterator is different, the the smallest iterator decides the lenght of the new iterator

l1 = [1,2,3,4]
l2 = [5,6,7,8]
# l3 = zip(l1,l2)
# l3 = list(l3)
l3 = list(zip(l1,l2))
print(l3)

# Program to add the items of 2 lists indexwise
l1 = [1,2,3,4]
l2 = [5,6,7,8]
# l3 = list(zip(l1,l2))
# print([i+j for i,j in l3])
print([i+j for i,j in zip(l1,l2)])


l1 = [1,2,3] # this decides the lenght of the ziped list
l2 = [1,2,3,4,5,6]
print(list(zip(l1,l2)))








####################################################
#################### ENUMERATOR ####################
####################################################

# the enumerate() method adds a counter to an iterable and returns it (the enumerate object)
l = ['a','b','c','d']
x = enumerate(l)
print(x)
y = list(x)
print(y)


l = ['a','b','c','d']
x = list(enumerate(l, start=11)) # [(11, 'a'), (12, 'b'), (13, 'c'), (14, 'd')]
print(x)


l = [('tejas',32), ('hello',12), ('world',19), ('good', 9)]
# sort this based on the first item
print(sorted(l))
print(sorted(l, reverse=True))

# sort this based on the second item
print(sorted(l,key=lambda x:x[1])) # this lambda function tells to sort based on second item, i.e, item at index 1
print(sorted(l, key=lambda x:x[1], reverse=True))
