# PascalCase - start the first letter of all the word in Capital
class Atm:

    def __init__ (self):
        print(id(self))
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        Hi, How can I help you?
        1. press 1 to create pin
        2. press 2 to change pin
        3. press 3 to check balance
        4. press 4 to withdraw
        5. press anything else to exit     
        """)

        if user_input == '1':
            self.createPin()
        elif user_input == '2':
            self.changePin()
        elif user_input == '3':
            self.checkBalance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()

    def createPin(self):
        userPin = input("enter new pin: ")
        self.pin = userPin
        userBalance = int(input("enter your balance: "))
        self.balance = userBalance
        print("Pin created successfully")
        self.menu()

    def changePin(self):
        oldPin = input("enter your old pin: ")
        if oldPin == self.pin:
            newPin = input("Enter new pin: ")
            self.pin = newPin
            print("Pin changed succesfully")
        else:
            print("Old pin is wrong")
        self.menu()

    def checkBalance(self):
        yourPin = input("Enter your pin: ")
        if yourPin == self.pin:
            print("Your balance is", self.balance)
        else: print("Wrong Pin")
        self.menu()

    def withdraw(self):
        yourPin = input("Enter your pin: ")
        if yourPin == self.pin:
            withdrawAmount = int(input("How much you want to withdraw: "))
            if withdrawAmount > self.balance:
                print("Insufficient Balance")
            else:
                self.balance -= withdrawAmount
                print("Withdrawl Success")
            
            print("Your Current Balance is", self.balance)

        else:
            print("Wrong Pin")

        self.menu()

# obj = Atm()
# print(id(obj))





# Creating a new data type - fraction
class Fraction:
    """
    numerator, denominator
    """
    def __init__(self, x, y): # parameterised constructor i.e the constructor which needs input
        self.numerator = x
        self.denominator = y

    def __str__(self):
        # return "i am here"
        return "{}/{}".format(self.numerator, self.denominator)
    
    def __add__(self,other): # self = fr1, other = fr2
        # print("i am here")
        newNumerator = (self.numerator*other.denominator) + (other.numerator*self.denominator)
        newDenominator = self.denominator * other.denominator
        return "{}/{}".format(newNumerator, newDenominator)
    
    def __sub__(self,other): 
        newNumerator = (self.numerator*other.denominator) - (other.numerator*self.denominator)
        newDenominator = self.denominator * other.denominator
        return "{}/{}".format(newNumerator, newDenominator)
    
    def __mul__(self,other): 
        newNumerator = self.numerator * other.numerator
        newDenominator = self.denominator * other.denominator
        return "{}/{}".format(newNumerator, newDenominator)
    
    def __truediv__(self,other): 
        newNumerator = self.numerator * other.denominator
        newDenominator = self.denominator * other.numerator
        return "{}/{}".format(newNumerator, newDenominator)
    
    def convertToDecimal(self):
        return self.numerator/self.denominator

# fr1 = Fraction(3,4)
# fr2 = Fraction(1,2)
# print(fr1, fr2)

# a = fr1 + fr2
# b = fr1 - fr2
# c = fr1 * fr2
# d = fr1 / fr2
# print(a,b,c,d,sep="\n")

# e = fr1.convertToDecimal()
# print(e)








# Write OOP classes to handle the following scenarios:
# * A user can create and view 2D coordinates
# * A user can find out the distance between 2 coordinates
# * A user can find find the distance of a coordinate from origin
# * A user can check if a point lies on a given line
# * A user can find the distance between a given 2D point and a given line

class Point:

    def __init__(self,x=0,y=0):
        self.xCord = x
        self.yCord = y

    def __str__(self):
        return "<{}, {}>".format(self.xCord, self.yCord)
    
    def euclidianDistance(self, other):
        # self = x1, y1
        # other = x2, y2
        # dist = sqrt(((x2-x1)^2) + ((y2-y1)^2))
        return (((self.xCord - other.xCord)**2) + ((self.yCord - other.yCord)**2))**0.5
    
    def distanceFromOrigin(self):
        dummy = Point(0,0) # creating class object inside a class
        return self.euclidianDistance(dummy)
        # return self.euclidianDistance(self, Point(0,0)) #throws error due to 3 argument s

    def pointOnLine(point, line): #self = point, other = line
        if (line.a*point.xCord) + (line.b*point.yCord) + line.c == 0 :
            return "Lies on the line"
        else: return "Not on the line"

# * A user can check if a point lies on a given line -> put the value of point in the line object
class Line: # ax+by+c = 0

    def __init__(self,a=1,b=1,c=0):
        self.a, self.b, self.c = a, b, c

    def __str__(self):
        return "{}x + {}y + {} = 0".format(self.a, self.b, self.c)
    
    # def pointOnLine(self, other): 
    def pointOnLine(line, point):
        # line = self, other = point
        if (line.a*point.xCord) + (line.b*point.yCord) + line.c == 0 :
            return "Lies on the line"
        else: return "Not on the line"

    def shortestDist(line, point):
        return (abs(line.a*point.xCord + line.b*point.yCord + line.c))/((line.a**2 + line.b**2)**0.5)
    
    def intersectionOfLines(self, other):
        # determinant (D) = a1b2 - a2b1, if D = 0, then lines are parallel, else they intersect
        # self = a1x + b1y + c1 = 0
        # other = a2x + b2y + c2 = 0
        if ((self.a * other.b) - (other.a * self.b) == 0):
            return "The two lines don't intersect"
        else: return "The two lines intersect"


p1 = Point(1,1)
p2 = Point(10,1)
# print(p1, p2)
# print(p1.euclidianDistance(p2))
# print(p1.distanceFromOrigin())


l1 = Line(1,1,-2)
l2 = Line()
# print(l1,l2)
# print(l1.pointOnLine(p1)) # calls pointOnLine of the Line Class
# print(l1.pointOnLine(p2))
# print(Line().pointOnLine(Point()))

# print(p1.pointOnLine(l1)) # calls pointOnLine of the Point Class
# print(p2.pointOnLine(l1))

l3 = Line(3,3,1)
p3 = Point(2,1)
# print(l3.shortestDist(p3))
# print(Line(1,1,-2).shortestDist(Point(1,1)))

l4 = Line(2,-3,1)
l5 = Line(1,1,-7)
l6 = Line(2,-3,-9)
# print(l4.intersectionOfLines(l5))
# print(l4.intersectionOfLines(l6))














# How objects access attributes

class Person:

    def __init__(self, name, country):
        self.name, self.country = name, country

    def greet(self):
        if self.country.lower() == 'india':
            return "Namaste, {}".format(self.name.capitalize())
        else: return "Hello, {}".format(self.name)

p = Person('tejas','India')
print(p.country) # accessing the attributes
print(p.greet()) # accessing the methods
# p.hello  --> throws error because hello as an attribute is not present in Person Class
p.gender = 'male' # creating attributes from outside of the class
print(p.gender)



################### Reference Variable ####################

class Person:

    def __init__(self):
        self.name = 'Tejas'
        self.gender = 'Male'

p = Person() # creating an object of Person
print(Person()) # no variable
# p is the reference of the object. p is not the object. It contains the reference of the object that has been created

q = p # both point to the same object  # syntax of aliasing
# any editing on any object, changes the data within both object
print(id(p))
print(id(q))

print(p.name)
print(q.name)
q.name = 'hegde'
print(p.name)
print(q.name)




########################## Pass By Reference ########################

class Person:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

def greet(person): # this is a function (not a method)
    # Function recieving object as input to this function
    print('my name is', person.name, 'and i am a', person.gender)
    p1 = Person('tejaswini','female')
    return p1 
    # Function returning Object

p = Person('tejas','male')
x = greet(p)
print(x.name, x.gender)




####################
class Person:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

def greet(person):
    # person has same id as p which is outside the function.
    # that is, address is passed and not the object
    # therefore when i change the name of person within this class, it reflects the same even outside the class when p.name is printed
    print(id(person))
    person.name = 'hello'
    print('my name is', person.name, 'and i am a', person.gender)

p = Person('tejas','male')
print(id(p))
greet(p)
print(p.name) # p.name is changed because of greet function




####################### Mutability of object #####################
# User defined objects are mutable 

class Person:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

def greet(person):
    person.name = 'ankit'
    return person

p = Person('tejas','male')
print(id(p))
p1 = greet(p)
print(id(p1))
