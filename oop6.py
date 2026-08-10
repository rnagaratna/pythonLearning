##################### DESTRUCTOR #####################

# def __del__(self): 
# it removes the object from memory
# it is used to write the configuration related code - closing the connection with db, disconnection from internet


class Example:
    def __init__(self):
        print("Inside Constructor")

    def __del__(self):
        print("Inside Destructor")

obj = Example()
del obj
print("In main function")

# untill all the reference are deleted destructor will not be called

class Example:
    def __init__(self):
        print("Inside Constructor")

    def __del__(self):
        print("Inside Destructor")

obj = Example()
a = obj
del obj # now this will not call destructor because a is still present

print("In main function")

del a # now this calls the destructor
print("In main function")





## dir, isinsatnce, issubclass
class Test:
    def __init__(self):
        self.hello = 4
        self.world = 'world'
        self.__okay = 'google' # _Test__okay

    def greet(self):
        print("Hello, i am {}".format(self.okay))

obj1 = Test()
print(dir(obj1))

print(isinstance(obj1,Test))
print(isinstance(obj1,Example))

class A:
    pass

class B(A):
    pass

print(issubclass(A,B)) # A is not a subclass of B
print(issubclass(B,A)) # B is a subclass of A






# Class Method versus Static Method



### Differences between single and double underscores in python variable and method names

## _var
# indicates a name is meant for internal use. It is used as an hint to programmer. Please let the variable use inside the class
# for a _var, child class can access it

class A:
    def __init__(self):
        self._var = 10 # just telling the programmer, not to use it from outside the class. But if he wants, he can use.

a = A()
print(a._var)


## var_
# suppose you want to use a keyword as variable, it can be used by adding a underscore after the variable like class_

class_ = input("Enter word 'class': ")
print(class_)



## __var
# private + name mangling

## __var__
# Magic method

## _
# a temporary variable
# don't care variable







########## Magic Methods ###########
### repr versus str

# str is meant to show to users and is readable
# repr is meant for programmers for debugging for being unambigous


a = 'hello'
print(str(a))
print(repr(a))

import datetime
a = datetime.datetime.now()
b = str(a)

print(a, b)
print()
print(str(a), str(b))
print()
print(repr(a), repr(b))
print()





## How can objects be saved in sets, even if they are mutable????
# because python checks for hashable type and not immutable type 
# objects are hashable and hence can be saved in sets
# the __hash__ function should return an interger, here object returns an interger, whereas the List doesn't return any integer

class A:
    def __init__(self):
        print("Constructor")
    def hello(self):
        print("hello")

a = A()
s = {a}
print(s)