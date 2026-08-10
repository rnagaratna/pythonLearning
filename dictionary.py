################### DICTIOANRY ####################
# 1. collection of key - value pair
# 2. also called as maps or associative array in other languages

# Characteristics
# 1. mutable
# 2. indexing has no meaning
# 3. key can't be mutable datatype
# 4. unordered
# 5. if key is not unique, then that key will hold the latest value


# KEY in dictionary can't be mutable datatype
# Why should be the key a immutable datatype?? 
# because dictionary uses hashing on keys to find out where to store the items - if the key is mutable, then the hash function for that key should also change and a new place in the memory should be alloted to all the items in the dictionary which takes a lot of time.


#### creating dict

d1 = {} # empty dictionary
d2 = {'name':'tejas','gender':'male'} # 1D-homogeneous
d3 = {'name':'tejas','gender':'male', (1,2,3):'okya'} #1D-heterogeneous

d4 = {
    'name':'tejas',
    'college':'bit',
    'sem':4,
    'subjects':{
        'maths':45,
        'english':54,
        'dsa':25,
    }
}         #### 2D dictionary
print(d4)

d5 = dict([(1,2),(3,4),(5,6)])
print(d5)
d6 = dict([('name','tejas'),('age',25),(3,3)])
print(d6)
d7 = dict(((1,2),(3,4),(5,6)))
print(d7)

# if key is not unique, then that key will hold the latest value
d8 = {'name':'tejas','name':'rahul'}
print(d8)

# mutable items as keys
d9 = {'name':'tejas', [1,2,3]:2} # throws error



###### Accessing the dict #######
d = {'name':'tejas', 'age':45, 'gender':'male'}

print(d['name'])
print(d.get('age'))


###### Adding new key vaalue pair #######
d['place'] = 'bangalore'
d['weight'] = 45
print(d)


###### Remove key value pair #######
# pop, popitem, del, clear

d = {'name': 'tejas', 'age': 45, 'gender': 'male', 'place': 'bangalore', 'weight': 40}
d.pop('place') ## deletes the key and value of the given key
print(d)

d = {'name': 'tejas', 'age': 45, 'gender': 'male', 'place': 'bangalore', 'weight': 45}
d.popitem() ## deletes last key value pair
print(d)

d = {'name': 'tejas', 'age': 45, 'gender': 'male', 'place': 'bangalore', 'weight': 45}
del d['name']
print(d)
del d 
# print(d) --> throws error

d = {'name': 'tejas', 'age': 45, 'gender': 'male', 'place': 'bangalore', 'weight': 45}
d.clear()
print(d)


d4 = {
    'name':'tejas',
    'college':'bit',
    'sem':4,
    'subjects':{
        'maths':45,
        'english':54,
        'dsa':25,
    }
} 
print(d4['subjects']['dsa'])
d4['subjects']['cn'] = 16
print(d4)




###### editing the key value pairs #####

d4['subjects']['dsa'] = 100
print(d4)


######### OPERATIONS ############
# membership - acts on keys and not value

print('tejas' in d4) # checks for key with name 'tejas' = False
print('name' in d4) # true

# iterations
d = {'name': 'tejas', 'age': 45, 'gender': 'male', 'place': 'bangalore', 'weight': 45}
for i in d:
    print(i, d[i])


########## FUNCTIONS #########
# len and sorted
d = {'name': 'tejas', 'age': 45, 'gender': 'male', 'place': 'bangalore', 'weight': 45}
print(len(d))
print(sorted(d)) # sorts all keys in the list
print(sorted(d,reverse=True))
print(min(d))
print(max(d))
 
print(d.items()) # gives all key value pairs within a tuple
print(d.keys())
print(d.values())

d1 = {1:2,3:4,5:6}
d2 = {5:4,7:8}
d1.update(d2)
print(d1)

d1 = {1:2,3:4,5:6}
d2 = {5:4,7:8}
d2.update(d1)
print(d2)








################# DICTIONARY COMPREHENSION ################
### Expression {key:value for var in iterables}

# print 10 numbers and their square in k-v pairs
res = {i:i**2 for i in range(1,11)}
print(res)

res = {i:i**2 for i in range(1,11) if i%2 == 1} # number:square of odd numbers
print(res)

# update a dict from km to half of km 
dists = {'delhi':1000, 'bangalore':3000, 'chennai': 2500}
res = {i:j*0.5 for (i,j) in dists.items()}
print(res)

res = {i:dists[i]/2 for i in dists}
print(res)


# Zip and dictionary comprehension (dc)
days = ['su','mo','tu','we','th','fr','sa']
temp = [1,2,3,4,5,6,7]

# x = dict(zip(days,temp))
# print(x)
res = {i:j for (i,j) in zip(days,temp)}
print(res)



# if condition with dc
p = {'ipad':21, 'mobile':0, 'pc':1, 'earphone':0,'charger':54} # display those with no stocks
res = {k:v for (k,v) in p.items() if v>0}
print(res)


# nested comprehension
# print tables from 2 to 4 in the following manner

"""
{
    2:{1:2, 2:4, 3:6, 4:8, ...},
    3:{1:3, 2:6, 3:9, 4:12, ...},
    4:{1:4, 2:8, 3:12, 4:16, ...}
}
"""

res = {j:{i:i*j for i in range(1,11)} for j in range(2,4)}
print(res)