# A decorator in python is a function that recieves another function as input and adds some other functionality(decoration) to it and returns it

# function is a first class citizen
def modify(func, number): 
    return func(number)

def square(number):
    return number**2

print(modify(square, 5)) # sending function square as a input to modify function




##### Decorators #####
# Closure - run the below code on python tutor
def myDec(fun):
    def wrapper():
        print("*******************")
        print(fun())
        print("*******************")
    return wrapper

def greet():
    return "Hello"

a = myDec(greet) # this gets a function Wrapper
a()



# The above set of code can be written as below :) Both are same

def myDec(fun):
    def wrapper():
        print("*******************")
        print(fun())
        print("*******************")
    return wrapper

@myDec
def greet():
    return "Hello"

greet()






### Printing executing time of a function using decorators
import time

def timer(fun):
    def wrapper(*args):
        start = time.time()
        fun(*args)
        end = time.time()
        print("Time taken by the",fun.__name__," is", end-start, "secs")
    return wrapper

@timer
def greet():
    print("Hello world")
    time.sleep(1)

@timer
def square(num):
    print(num**2)
    time.sleep(1)

@timer
def power(a,b):
    print(a**b)
    time.sleep(1)

greet()
square(21)
power(123,12)





######

def sanityCheck(datatype):
    def outerWrapper(fun):
        def innerWrapper(*args):
            if type(*args) == datatype :
                fun(*args)
            else: print("This datatype isn't supported")
        return innerWrapper
    return outerWrapper

@sanityCheck(int)
def square(num):
    print(num**2)

@sanityCheck(str)
def greet(name):
    print("Hello,",name)

square(4)
square('okay')
greet("Tejas")
greet(0)
