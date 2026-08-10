################################### ENCAPSULATION ####################################

# Instance variable 
# we can store different values on the same variable using different objects
class Person:
    def __init__(self,name_input,country_input):
        self.name = name_input
        self.country = country_input

p1 = Person('tejas','india')
p2 = Person('tony','US')
print(p1.name, p2.name)


class Atm:

    def __init__ (self):
        print(id(self))
        self.pin = ''
        self.balance = 0
        # self.menu()

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
        # self.menu()

    def changePin(self):
        oldPin = input("enter your old pin: ")
        if oldPin == self.pin:
            newPin = input("Enter new pin: ")
            self.pin = newPin
            print("Pin changed succesfully")
        else:
            print("Old pin is wrong")
        # self.menu()

    def checkBalance(self):
        yourPin = input("Enter your pin: ")
        if yourPin == self.pin:
            print("Your balance is", self.balance)
        else: print("Wrong Pin")
        # self.menu()

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

        # self.menu()



obj = Atm()

# obj.createPin()
# obj.balance = 'hehehe'
# obj.withdraw() # This throws error --> because balance now has a string, but withdraw function demands integer/float
# this happens because the attribute of the object can be accessed from outside the program (balance = 'hehehe')
# therefore this is made private



# variable is made PRIVATE by using __ (double underscore before the variable name) eg. __balance
class Atm:

    def __init__ (self):
        print(id(self))
        self.pin = ''
        self.__balance = 0
        # self.menu()

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
        self.__balance = userBalance
        print("Pin created successfully")
        # self.menu()

    def changePin(self):
        oldPin = input("enter your old pin: ")
        if oldPin == self.pin:
            newPin = input("Enter new pin: ")
            self.pin = newPin
            print("Pin changed succesfully")
        else:
            print("Old pin is wrong")
        # self.menu()

    def checkBalance(self):
        yourPin = input("Enter your pin: ")
        if yourPin == self.pin:
            print("Your balance is", self.__balance)
        else: print("Wrong Pin")
        # self.menu()

    def withdraw(self):
        yourPin = input("Enter your pin: ")
        if yourPin == self.pin:
            withdrawAmount = int(input("How much you want to withdraw: "))
            if withdrawAmount > self.__balance:
                print("Insufficient Balance")
            else:
                self.__balance -= withdrawAmount
                print("Withdrawl Success")
            
            print("Your Current Balance is", self.__balance)

        else:
            print("Wrong Pin")

        # self.menu()

#obj = Atm()
#obj.createPin()
# obj. # when . in clicked, it doesn't show the variable name balance (because it is made private)
#obj.__balance = 'hehehe' # this code doesn't throw error, it works perfectly. Therefore purpose failed :(
#obj.withdraw() # this also works perfectly without any error

# This happens because, when a variable is made private by inserting a __ before the variable name, the python internally converts it into _ClassName__VariableName (here: _Atm__balance). Therefore when i do this (obj.__balance = 'hehehe'), i am not working on the balance variable. Since, we can create an attribute from outside the class in this way, __balance becomes the new attribute for the object. Therefore, withdraw function works perfectly on the data given earlier through createPin() method.
# But one can access the private balance variable as well in the following way : 

#obj._Atm__balance = 'hehehe'
# obj.withdraw() # this code crashes, because balance is now is string and withdraw function requires int/float

### Therefore nothing in python is TRUELY PRIVATE





## Using Getter and Setter logic to access the private variable from within the class
class Atm:

    def __init__ (self):
        print(id(self))
        self.pin = ''
        self.__balance = 0
        # self.menu()

    def getBalance(self):
        return self.__balance
    
    def setBalance(self, newValue):
        if type(newValue) == int:
            self.__balance = newValue
            print("Balance set successfully")
        else: print("Unknown datatype to set balance")

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
        self.__balance = userBalance
        print("Pin created successfully")
        # self.menu()

    def changePin(self):
        oldPin = input("enter your old pin: ")
        if oldPin == self.pin:
            newPin = input("Enter new pin: ")
            self.pin = newPin
            print("Pin changed succesfully")
        else:
            print("Old pin is wrong")
        # self.menu()

    def checkBalance(self):
        yourPin = input("Enter your pin: ")
        if yourPin == self.pin:
            print("Your balance is", self.__balance)
        else: print("Wrong Pin")
        # self.menu()

    def withdraw(self):
        yourPin = input("Enter your pin: ")
        if yourPin == self.pin:
            withdrawAmount = int(input("How much you want to withdraw: "))
            if withdrawAmount > self.__balance:
                print("Insufficient Balance")
            else:
                self.__balance -= withdrawAmount
                print("Withdrawl Success")
            
            print("Your Current Balance is", self.__balance)

        else:
            print("Wrong Pin")


obj = Atm()
print(obj.getBalance())
obj.setBalance('hehehe')
obj.setBalance(10000)
print(obj.getBalance())
# print(obj.__balance)  --> throws error because obj has no attribute __balance
print(obj._Atm__balance) # a way to access private variable/attributes








