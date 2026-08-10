# ################# FUNCTIONS IN PYTHON ################

# Helps in code reusability

# 2 types of function
# 1. Built in function
# 2. User defined function

# 2 principles of function:
# 1. Abstraction
# 2. Decomposition

# Components of function:
# 1. def keyword
# 2. name of function
# 3. (input): """docsstring to understand what this function does"""
# 4. logic and code
# 5. return

# def is_even (i) :
#     """
#     what does this code do
#     """
#     code
#     return

# is_even(5)


# i is parameter
# when the value is passed from the main body it is arguement
# that is, 5 is argument, i is parameter


# How functions are executed in memory??
# Local and global scope

# Benefits of functions
# 1. code modularity
# 2. code readability
# 3. code reusability




def is_even(num):
    """
    # this is called as a docstring
    This function returns if the given number is even or odd
    input - any valid integer
    output - odd or even
    created on 4th June 2026
    """
    if type(num) != int:
        return 'invalid datatype'
    elif num%2 == 0:
        return 'even'
    else: return 'odd'

for i in range(1,11):
    x = is_even(i)
    print(x)

print(is_even('hello'))


print(is_even.__doc__) # to view the docstring of a function
print(print.__doc__)




############### Types of Arguements ###############

# 1. Default Argument
def power(a=1,b=1): # a=1, b=1 are the default values, whenever the corresponding values are not passed the default value will be used
    print("The value of a is {} and value of b is {}".format(a,b))
    return a**b

print(power(2,3)) #a=2, b=3
print(power(2)) #a=2, b=1
print(power()) #a=1, b=1



# 2. Positional Arguments
def power(a=1,b=1):
    return a**b

print(power(2,3))
# it means that 1st argument reaches first parameter, 2nd argument to 2nd parameter



# 3. Keyword Argument
def power(a=1,b=1):
    print("The value of a is {} and value of b is {}".format(a,b))
    return a**b

print(power(b=2,a=3))



### *args and **kwargs - are special Python keywords, used to pass the variable lenght of arguments to the functions
# order of argument matters: normal argument >> *args >> **kwargs

# *args helps to pass a variable number of "non-keyword arguments" to a function
def addNum(*args):   # args is the name of the variable
    print(type(args)) ## Tuple
    sum = 0
    for i in args:
        sum += i
    return sum

print(addNum(1,2))
print(addNum(1,2,3,4,5,6,7,8,9,10))

def multipy(*hello):   # hello is name of the variable
    print(type(hello))
    sum = 1
    for i in hello:
        sum *= i
    return sum

print(multipy(1,2,3))
print(multipy(1,2,3,4,5,6,7,8,9,10))



# **kwargs - allows us to pass variable number of "KeyWord argument"
# keyword argument means they contain a "keyvalue pair", like a python dictionary
def display(**kwargs):
    #kwargs will be dictionary
    for (k,v) in kwargs.items():
        print(k, '-->', v)

display(india='delhi',sl='colombo',nepal='katmandu')
display(india=5,sl=6,nepal=7)


#How functions are executed in memory??
#Local and global scope


#### if no return statement

def is_even(num):
    if num%2 == 0:
        print('even')
    else: print('odd')

print(is_even(5)) # output = odd
                  # return value  = None
# if there is no return statement in the program, default value it returns is None, hence None also gets printed
L = [1,2,3]
print(L.append(4)) # this prints None, because append function doesn't prints anything
print(L)





##### Local versus Global variable #####
# 1. from funtions we can only access (cannot change) the global variable
# 2. from global frame we can't access local variable of the function

def simple(y):
    print(x)
    print(x+1)
x = 5
simple(x)
print(x)

def f(y):
    x = 1
    x += 1
    print(x)
x=5
f(x)
print(x)

# def h(y):             Throws error
#     x += 1            because x is in main/global scope and its value cannot be
# x = 5                 changed in local scope           
# h(x)                  however it can be done using global keyword
# print(x)

def h(y):
    global x # telling the comp to use global x
    x += 1
    print(x)
x = 5
h(x)
print(x)



def f(x):
    x = x + 1
    print('in f(x): x = ',x)
    return x

x = 3
z = f(x)
print('in main program scope: z =', z)
print('in main program scope: x =', x)


############# NESTED FUNCTIONS ############
def f():
    def g():
        print("Inside function g")
    g()
    print("Inside function f")
    g()

f()
# g() --> throws error, can't be accessed through main program. g is hidden

def f():
    def g():
        print("Inside function g")
        # f() --> creates infinite printings
    g()
    print("Inside function f")
f()


def g(x):
    def h():
        x = 'abc'
        print(x)
    x = x + 1
    print('in g(x): x =', x)
    h()
    return x

x = 3
z = g(x)
print(x, z)




##### Functions in python is a first class citizen #####
# Function in python acts as a datatype
def square(num):
    return num**2

print(type(square)) # type and id
print(id(square))

x = square # reassign
print(id(x)) ## x is also refereing to square (same memory address)
print(x(5))
print(square(5))

del square # deleting a function
print(x(4)) # x still works
# print(square(4))  --> throws error because square is deleted



def square(num):
    return num**2

sqList = [1,2,3,square] # storing
print(sqList[-1])
print(sqList[-1](5)) ## square of 5


# functions are immutable
s = {square} # this code runs means square is immutable
print(s)


# returning a function
def f():  
    def x(a,b):
        return(a+b)
    return x  

val = f()(3,4) # f() returns function x, and this results into x(3,4), that is the function inside a function can be accessed from main like this
print(val)


# function as argument
def fa(): 
    print("inside fun a")
    return
def fb(z):                      # z gets fa as parameter
    print("inside fun b")
    return z()                  # returning fa()

print(fb(fa))
# output - inside fun b, inside fun a