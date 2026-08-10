######### Collection of Objects ##########

class Person:

    def __init__(self, name, gender):
        self.name, self.gender = name, gender

    # def __str__(self):
    #     return "i am {} and i am {}".format(self.name, self.gender)

p1 = Person('A','m')
p2 = Person('B','f')
p3 = Person('C','f')

l = [p1,p2,p3]
print(l)

for i in l:
    print(i)
    print(i.gender)

d = {
    'p1':p1,
    'p2':p2,
    'p3':p3
}

for i in d:
    print(i, d[i], d[i].name, d[i].gender, sep='        ')
    
for k,v in d.items():
    print(k,v)




############## STATIC Variables and STATIC METHOD ##############
# assign an id for each customer
class Atm:

    __counter = 1

    def __init__ (self):
        print(id(self))
        self.pin = ''
        self.balance = 0
        # self.menu()
        # self.cid = 0  # these two lines of code actually dont give any unique id
        # self.cid += 1  # all users will have the id 1, because these code runs all the time when an object is created
        # therefore instance variable cannot be used. 
        # Instance variable - object variable
        # we need static variable i.e class variable
        # static variable value will be same for all object
        # instance variable value will be different for all objects
        # Static attributes are object independent. We can access them without creating instance (object) of the class in which they are defined

        self.cid = Atm.__counter
        Atm.__counter += 1

        # className.variableName is STATIC variable
        # self.vairableName is INSTANCE variable

    @staticmethod
    def getCounter(): 
        # this is not using self inside the code and hence not given as parameter
        # they donot require object to call them
        # this method is called using class name and not with the object
        # eg. Atm.getCounter()
        # such methods are called as static methods
        # hence a decorator @staticmethod is added
        return Atm.__counter

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

c1 = Atm()
c2 = Atm()
c3 = Atm()
print(c1.cid, c2.cid, c3.cid)
print(Atm.getCounter())

# Atm.counter = 'hello'
# c1 = Atm()  --> creates error because counter is now a string. therefore make it private
print(Atm.getCounter())







########################## CLASS RELATIONSHIPS ########################
## AGGREGATION and INHERITANCE

# Aggregation means has a relationship
# here one class owns the other class
# eg - customer has a address, here customer class owns address class
# private variable can't be accessed while performing aggregation (can be printed with a get)

class Customer:

    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address

    def print_address(self):
        print(self.address.getCity(), self.address.pin, self.address.state) # self.address.__city -> throws error

    def editProfile(self, newName, newCity, newPin, newState):
        self.name = newName
        self.address.editAddress(newCity, newPin, newState)

class Address:

    def __init__(self, city, pin, state):
        self.__city = city
        self.pin = pin
        self.state = state

    def getCity(self):
        return self.__city
    
    def editAddress(self, newCity, newPin, newState):
        self.__city = newCity
        self.pin = newPin
        self.state = newState

add1 = Address('shimoga',577205,'karnataka')
cust1 = Customer('tejas','male',add1)
cust1.print_address()

cust1.editProfile('tejaswini','chennai',123456,'tamilnadu')
cust1.print_address()


### Inheritence - oop4.py
