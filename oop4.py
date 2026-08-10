####################### Inheritance ########################


# Parent class and Child class
# helps is code reusability
# helps in DONT REPEAT YOURSELF

# * student - login, registration, enroll, review
# * instructor - login, registration, create, reply

# instead of the above framework, we can use this - 
# * user (parent) - login, registration
# * student (child 1) - enroll, review
# * instructor (child 2) - create, reply

# What gets inherited?
# 1. constructor
# 2. non private attribute
# 3. non private method

# - A class can inherit from another class.
# - Inheritance improves code reuse
# - Constructor, attributes, methods get inherited to the child class
# - The parent has no access to the child class
# - Private properties of parent are not accessible directly in child class
# - Child class can override the attributes or methods. This is called method overriding
# - super() is an inbuilt function which is used to invoke the parent class methods and constructor



############################## Inheritance ##############################

# 1. single : parent <- child
# 2. multilevel : grand parent <- parent <- child <- grand child
# 3. hirarchical : one parent with multiple children
# 4. multiple : multiple parent for a child class
# 5. hybrid : mixture of above 4




class User: 

    def __init__(self):
        self.name = 'tejas'
        self.gender = 'm'

    def login(self):
        return ('login')

class Student(User): 
    # Student is the child class
    # User is the parent class
    # Student object can access the User class

    # def __init__(self):
    #     self.rn = 111

    def enroll(self):
        return ("enroll into the class")

u = User()
s = Student()

"""
 when s object is created, it first checks the constructor within it's class i.e Student class. If there is a constructor, then it executes the constructor and donot look for parents constructor

 suppose if there was no constructor within the Student class, then it looks for the constructor within the Parent Class and executes it.

 def __init__(self):
      self.rn = 111

when the above 2 lines of code is written within Student class, then this will be executed. Constructor of the parent (setting name and gender) donot get executed.

Therefore, printing s.name would throw error
"""

# print(s.name)
# print(s.enroll())
# print(s.login())







class Phone:
    def __init__(self, price, brand,camera):
        print("inside phone constructor")
        self.price, self.brand, self.camera = price, brand, camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    pass

s = SmartPhone(10000, 'hello',' 40') 
# SmartPhone donot have its own constructor
# Parent constructor is execued
s.buy()



class Phone:
    def __init__(self, price, brand,camera):
        print("inside phone constructor")
        self.price, self.brand, self.camera = price, brand, camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    def __init__(self, os, ram):
        print("Inside SmartPhone constructor")
        self.os, self.ram = os, ram

s = SmartPhone('and','12GB')
# now SmartPhone has its own constructor and hence it gets executed
# s.price, s.brand, s.camera --> This throws error, because price is not initialized
s.buy()





# Child cannot access private members of the parent class
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    # getter
    def show(self):
        return (self.__price)

class SmartPhone(Phone): #this calls the parent constructor
    def check(self):
        print(self.__price)

s = SmartPhone(20000, 'world', 40)
# s.check() # --> this throws error, because, it is accessing the private member of the parent class __price
print(s.brand) # this gets executed because brand is not a private member
print(s.show()) # this also gets executed because show is not private






################## METHOD OVERRIDING ################

class Person:
    def __init__(self):
        self.name, self.age = 'okay', 'google'

    def data(self):
        print("I am a Person")

class Man(Person):
        
    def data(self):
        print("I am a Parent")

par = Man()
par.data()

"""
Here par object of the class Man, when it calls data method, this overrides the data method of Person(which is a parent of Man Class). Since, data method is present in both child and parent, par.data() calls the data method of the Man Class overridding the data method of Person Class

The same when it happens for constructor, it is called as Constructor Overridding.
"""





####################### SUPER KEYWORD #######################
print("\n\nSuper Keyword Demo\n")
# helps to call Parent Method
# super keyword(function) is used always inside the child class and cannot be called from outside
# super can be used for attributes, it is only used for methods like __init__, data etc

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")
        # syntax to call parent ka buy method
        super().buy()

s=SmartPhone(20000, "Apple", 13)
s.buy()



class Person:
    def __init__(self,name,age):
        print("Inside Parent")
        self.name, self.age = name, age

    def data(self):
        print("I am a Person")

class Man(Person):
    
    def __init__(self, name, age, gender='male'):
        self.gender = gender
        print("Inside Child 1")
        super().__init__(name, age) # calls the __init__ (constructor) of the parent class Person
        print("Inside Child 2")
    
    def data(self):
        print("I am a Parent")


m1 = Man('tejas',21,'m')
print(m1.name) 






##################### TYPES of INHERITENCE #####################

# 1. single : parent <- child (shown as discussed above), child inherits from parent
# 2. multilevel : grand parent <- parent <- child <- grand child
# 3. hierarchical : one parent with multiple children
# 4. multiple (Diamond problem) : multiple parent for a child class
# 5. hybrid : mixture of above 4

#### Single Inheritance
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    pass

SmartPhone(1000, "Apple","13px").buy()


##### Multilevel Inheritance #####
# multilevel : grand parent <- parent <- child <- grand child
class Product:
    def review(self):
        return("Product Customer Review")

class Phone(Product):
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        return ("Buying a phone")
    
    def printPvtPrice(self):
        print(self.__price)
    
    def getPrice(self):
        return self.__price

class SmartPhone(Phone):
    def data(self):
        return "I am from {}, having {} MP camera, with {}Rs Price".format(self.brand, self.camera, self.getPrice())

s = SmartPhone(20000,'mi',40)
print(s.data())
print(s.buy())
print(s.review()) # grandparent method
s.printPvtPrice()





##### Hierarchical #####
# hirarchical : one parent with multiple children
class Person:
    def __init__(self,name,age):
        self.__name, self.age = name, age

    def print_data(self):
        return "I am {} years, {}, name is {}".format(self.age, self.gender, self.__name)
    
class Man(Person):
    def __init__(self, name, age, gender = 'male'):
        super().__init__(name,age)
        self.gender = gender

class Woman(Person):
    def __init__(self, name, age, gender = 'female'):
        super().__init__(name,age)
        self.gender = gender

m1 = Man('tejas',21,'m')
w1 = Woman('tejaswini','18','f')
print(m1.print_data(), w1.print_data(),sep="\n")



##### Multiple #####
# multiple : multiple parent for a child class

class Mom:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class Dad:
    def review(self):
        print ("Customer review")

class Children(Dad, Mom):
    pass

c = Children(1,2,3)
c.buy()
c.review()
# I can call the method of both the parent, since it inherits from both Mom and Dad class


# Diamond Problem in Multiple inheritance
class Mom:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone within Mom Class")

class Dad:

    def buy(self):
        print("Buying a phone within Dad Class")

    def review(self):
        print ("Customer review")

# class Children(Dad, Mom):
class Children(Mom, Dad):
    pass

c = Children(1,2,3)
c.buy() # since, buy method is present in both mom and dad class, which buy method will be called here??
# class Children(Dad, Mom) -> whichever class from which the children is inheriting is written first (here Dad), the buy function of that class will be called. Output - Buying a phone within Dad Class
# class Children(Mom, Dad) -> whichever class from which the children is inheriting is written first (here Mom), the buy function of that class will be called. Output - Buying a phone within Mom Class


#####
class A:
    def m1(self):
        return 20

class B(A):
    def m1(self):
        val = super().m1+30
        return val

class c(B):
    def m1(self):
        val = self.m1()+20  # Error due to infinite loop
        return val

obj = C()
print(obj.m1())
        
