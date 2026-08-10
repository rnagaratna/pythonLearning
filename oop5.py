##################### POLYMORPHISM #####################

# Having multiple faces

# 1. Method overriding
# 2. Method overloading
# 3. Operator overloading

# Method overriding
# parent and child has the same method, in that case child's method will be called


### METHOD OVERLOADING  
# class with multiple methods of the same name, but behaves differently because of the input
# improves the readability


class Shape:
    def area(self, radius):
        return 3.14*radius*radius
    
    def area(self, len, wid):
        return len*wid
    
c1 = Shape()
# print(c1.area(5)) --> code throws error because of this
print(c1.area(4,5))

# The above code throws error, because method overloading is not supported in python
# if done it always considers the last method which has the same name, here it expects 2 input

# such behaviour can be done in the following way - 

class Shape:
    def area(self, a, b=0):
        if b==0:
            return 3.14*a*a
        else: return a*b

c1 = Shape()
print(c1.area(5)) 
print(c1.area(4,5))





### OPERATOR OVERLOADING
# same operator behaves differntly with different input
# eg: + operator
# + on strings 'concatenates', + on integer 'adds', + on Lists 'merge'
# eg: __add__ (add magic methods)




######################## ABSTRACTION ####################

# abstract class has atleast one abstract method - method which donot have any code, and should inherit from ABC class
# abstract method - the method which does not have code , concrete method - which has code
# abc - abstract base classes module, ABC - abstract base class
# we cannot make an object of an abstract class
from abc import ABC, abstractmethod

class BankApp(ABC): #abstract class

    def database(self):
        print("Connected to DB")

    @abstractmethod
    def security(self):
        pass

class MobileApp(BankApp):
    # Those inheriting the BankApp, should mandatority have a method of security. Else it will throw an error
    def mobileLogin(self):
        print("Logged into mobile")

    def security(self):
        print("Security Implemented")

mob = MobileApp()
mob.mobileLogin()
mob.security()
mob.database()
