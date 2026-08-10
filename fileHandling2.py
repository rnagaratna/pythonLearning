# Text files wont work with binary files
# working with files is not a good type to work with other data types in python - like dictionary, tuples, integers etc
# Everything in the files will be stored in Text Format (String) - reading, writing everything should be in string

### disadvantage 1 - Text files wont work with binary files like images
file = "fileHandling2/ss1.png"

with open(file, 'r') as f:
   #f.read() # This throws error, because image can't be processed
    pass

# Solution for disadvantage 1
# Creating a copy of image - ss.png 
with open(file, 'rb') as rf: # read binary = rb, here it reads binary data from the image
    with open('fileHandling2/ss_copy.png','wb') as wf: # Write binary
        wf.write(rf.read())


### disadvantage 2 - not good for other data types int/float/list/tuples
# int
file = "fileHandling2/sample1.txt"
with open(file,'w') as f:
    # f.write(5) # throws error - write performs only on strings
    pass


file = "fileHandling2/sample1.txt"    
with open(file,'w') as f:
    f.write('5')
with open(file,'r') as f:
    #print(f.read() + 5) # error - 5 which we read from the file is in str format
    print(int(f.read()) + 5)
    
# dict
file = "fileHandling2/sample1.txt"
d = {
    'name' : 'tejas',
    'age' : 23,
    'place' : 'karnataka'
}

with open(file,'w') as f:
    # f.write(d) --> This throws error because d should in string
    f.write(str(d))  #But now the data can't be accessed in Key Value Pair and reconverting  back to dictionary is not possible
# solution - serialization and deserialization

with open(file,'r') as f:
    print(f.read())
    print(type(f.read))
   #print(dict(f.read()) # we cannot convert str to dict
    

# solution for disadvantage 2 - serialization and deserialization


####################### serialization and deserialization ######################
## Serialization - it is a process of converting to python datatype to JSON format
## Deserialization - [JSON] -> [Python Datatype]

## JSON - Javascript on notation, it is an univeral data format that can be understood by all programming language

## serialization  and deserialization using json module
# list
import json
file = "fileHandling2/sample2.json"
l = [1,2,3,4,2,3,4,'\n']
with open(file,'w') as f:
    json.dump(l,f,indent=4) # what to dump(serialize) and file handler
    
with open(file,'r') as f:
    l1 = json.load(f) # Printing the list
print(l1)
print(type(l1)) # list



# dict
import json
file = "fileHandling2/sample3.json"
d = {
    'name' : 'tejas',
    'age' : 23,
    'place' : 'karnataka'
}
with open(file,'w') as f:
    json.dump(d,f,indent='\n')

with open(file,'r') as f: # deserialization
    d1 = json.load(f) # Printing the dictionary
print(d1)
print(type(d1)) # dictionary




# Tuple
# if we dump tuple, it will store in list format
# if we load it, it will be in list format only but we can covert it into tuple using tuple() function
import json
file = "fileHandling2/sample4.json"
t = (1,2,31,2,3)
with open(file, 'w') as f:
    json.dump(t,f) # this is stored as LIST and not as a tuple


### Serialization and Deserialisation on Custom Objects
import json 
class Tejas:
    def __init__(self):
        self.name = "tejas"
        self.age = 34
        self.gender = 'm'
        self.place = "Bangalore"

tejas = Tejas()


def showObjectAs1(obj):
    if isinstance(obj, Tejas):
        return "{} --> {} --> {} --> {}".format(obj.name, obj.age, obj.gender, obj.place)
    
def showObjectAs2(obj):
    if isinstance(obj, Tejas):
        return {
            'name':obj.name,
            'gender':obj.gender,
            'age':obj.age,
            'place':obj.place
        }

    
with open('fileHandling2/sample4.json','w') as f:
    # json.dump(tejas,f)  --->  Throws error, because object can't be serialized in this way
    # Python wants us to specify how this data object should be serialized
    json.dump(tejas,f,default=showObjectAs1,indent=4)


######  Working with multiple objects #####
 
class Tejas:
    def __init__(self,name='tejas',age='10',gender='m',place="bangalore"):
        self.name = name
        self.age = age
        self.gender = gender
        self.place = place

tejas1 = Tejas()
tejas2 = Tejas('Ganesh',43,'m','mumbai')


def showObjectAs1(objs):
    print(objs[0])
    return "{} --> {} --> {} --> {}".format(objs[0].name, objs[1].age, objs[0].gender, objs[1].place)

    
with open('fileHandling2/sample4.json','w') as f:
    json.dump([tejas1, tejas2],f,default=showObjectAs1,indent=4) # this creates a loop automatically first sending tejas1 and then tejas2



#####


with open('fileHandling2/sample5.json','w') as f:
    json.dump(tejas,f,default=showObjectAs2,indent=4)

with open('fileHandling2/sample5.json','r') as f:
    d = json.load(f)
    print(d)
    print(type(d))

### But what if i want entire onject to be stored in the file and retrive it and perform the function of the class on it
# This can be done by conveting object to binary

## PICKLING ##
# It is a process where a object is converted to byte stream, unpickling is a reverse process [byte stream] --> [object]

class Tejas:
    def __init__(self):
        self.name = "tejas"
        self.age = 34
        self.gender = 'm'
        self.place = "Bangalore"
    
    def showInfo(self):
        print("Hello, I am {} and I am from {}".format(self.name, self.place))

tejas = Tejas()


import pickle
with open("fileHandling2/sample6.pkl",'wb') as f: # in binary
    pickle.dump(tejas, f)

with open("fileHandling2/sample6.pkl",'rb') as f:
    person = pickle.load(f) # now i can perform all the function of Tejas Class on this person
    
person.showInfo()
