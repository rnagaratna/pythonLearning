#### syntax error ####

# leaving symbols like colon,brackets
# Misspelling a keyword
# Incorrect indentation
# empty if/else/loops/class/functions

# SyntaxError : missing parenteses
# print 'hello world'

# SyntaxError : invalid syntax
# if a == 3    
    #print('Hello')

# SyntaxError : invalid syntax
# iff a == 3:   
    #print('Hello world')

# IndentationError
# if a == 3:
#print('hello world')  

# IndexError - when trying to access an item at an invalid index
# L = [1,2,3]
# L[100]

# ModuleNotFoundError - when a module could not found
# import mathi
# math.floor(5.3)

# KeyError - when a key is not found
# d = {'name':'nitish'}
# d['age']

# TypeError - when an operation or function is applied to an object of an inappropriate type
# 1 + 'a'

# ValueError - when a function's argument is of an inappropriate type
# int('a')

# NameError - when an object could not found
# print(k)

# AttributeError
# L = [1,2,3]
# L.upper()


##### Exception #####
# Try Except Block

# reading a file which is not present --> Throws error --> FileNotFoundError

# with open('okaygoogle.txt','r') as f:
#     f.read()

# Traceback (most recent call last):
#   File "e:\pythonLearning\exceptionHandling.py", line 4, in <module>
#     with open('okaygoogle.txt','r') as f:
#          ~~~~^^^^^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'okaygoogle.txt'


try:
    with open('okaygoogle.txt','r') as f:
        f.read()
except:
    print("Sorry, file not found")


# there are 2 possible errors but showing same message for both the errors
try :
    with open('okaygoogle.txt','r') as f: # first error, if file not found
        print(f.read())
        print(m) # second error, if m variable not found
except:
    print('some error occured')

        
# Printing name of the error
try:
    with open('okaygoogle.txt','r') as f:
        f.read()
except Exception as e:
    print(e)
    print(e.with_traceback)


m = 0
# Exception for different types of error
try:
    # f = open('okaygoogle.txt','r') # no file with okaygoogle.txt
    f = open('fileHandling2/sample1.txt') # file is present
    print(f.read())
    print(m) # m is not defined
    print(21/0) # divide by zero error

except FileNotFoundError:
    print("File not found")

except NameError:
    print("Variable not found")

except ZeroDivisionError:
    print("can't divide by 0")

except: # default - any other error than nameerror and filenotfountfounderror
    print("Some error occured")


# Exception handling can be done for both syntax and exception errors but lot of time we use it onlt for exceptions


### Try - Except - Else

# file = 'fileHandling2/sample1.txt'
file = 'helloworld.txt'
try:
    f = open(file,'r')

except FileNotFoundError:
    print("File not found error")

except Exception as e:
    print(e.with_traceback)

else: # this block of code gets executed if the try block was executed.
    # if the except block is executed that is, if there was some error, then this else block will not be executed
    print(f.read())




### Try - Except - Else - Finally

file = 'fileHandling2/sample1.txt'
# file = 'helloworld.txt'
try:
    f = open(file,'r')

except FileNotFoundError:
    print("File not found error")

except Exception as e:
    print(e.with_traceback)

else: # this block of code gets executed if the try block was executed.
    # if the except block is executed that is, if there was some error, then this else block will not be executed
    print(f.read())

finally:
    print("""
This block gets printed anyways
1. Try -> Else -> Finally
2. Except -> finally
""")
    


### Raise Exception 
# You can throw an error

# raise NameError("This is a name error") # this raises error
# raise FileNotFoundError
# raise ModuleNotFoundError

class Bank:
    def __init__(self, balance):
        self.balance = balance

    def withDraw(self, amount):
        if amount<0:
            raise Exception("Amount can't be less than 0")
        elif amount > self.balance:
            raise Exception("Amount can't be greater than balance")
        
        self.balance -= amount

obj = Bank(10000)
try:
    obj.withDraw(-50000)
except Exception as e:
    print(e)
else:
    print("Ramaining amount = {}".format(obj.balance))




### Creating Custom Exception

class MyException(Exception): # custom exception class
    def __init__(self, message):
        print(message)

class Bank:
    def __init__(self, balance):
        self.balance = balance

    def withDraw(self, amount):
        if amount<0:
            raise MyException("Amount can't be less than 0")
        elif amount > self.balance:
            raise MyException("Amount can't be greater than balance")
        
        self.balance -= amount

obj = Bank(10000)
try:
    obj.withDraw(50000)
except MyException as e:
    pass
else:
    print("Ramaining amount = {}".format(obj.balance))



# why we need custon exception
#### Google Example ####
print("\n")
class SecurityError(Exception):
    def __init__(self, message):
        print(message)

    def logout(self):
        print("Logging out of all device")

class Google:

    def __init__(self, name, email, password, device):
        self.name = name
        self.email = email
        self.password = password
        self.device = device

    def login(self, email, password, device):
        if self.device != device:
            raise SecurityError("There is a security breach")
        
        if self.email == email and self.password == password:
            print("Welcome")

        else:
            print("Login Error")

obj = Google("tejas",'hello@gmail.com','1234','android')
try:
    obj.login('hello@gmail.com','1234','android') # change android to windows and check
except SecurityError as e:
    e.logout()
else: 
    print("Welcome {}".format(obj.name))
finally:
    print("Closing DB connections")
