# Get 2 int/float input from user and add them

print()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
add = num1 + num2
print(add)

# ORR
print(int(input("Enter First Num: ")) + int(input("Enter Second Num: ")))




# Get 3 digit input from user, and add the digits

number = int(input("Enter a 3 digit number: "))
a = number%10
number //= 10
b = number%10
number //= 10
c = number
print("Sum is ", a+b+c)




# find the minimim of 3 numbers

num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))
num3 = int(input('Enter number 3: '))

if (num1<num2) and (num1<num3):
    print('smallest is',num1)
elif num2<num3:
    print('smallest is',num2)
else:
    print('smallest is',num3)
    
                 
#ORR
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
minimum = min(num1,num2)
num3 = int(input("Enter number 3: "))
minimum = min(minimum, num3)
print(minimum)

# ORR
num1, num2, num3 = int(input("Enter number 1: ")), int(input("Enter number 2: ")), int(input("Enter number 3: "))
print(min (num1, num2, num3))




# Menu driven calculator

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
op = input("Enter the operator: ")

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
else:
    print(num1/num2)





# Guessing Game

import random as r
num = r.randint(1,100)
guess = int(input("Enter the number: "))
count = 1

while guess != num:
    if guess < num: 
        print("Wrong, guess higher")
    else:
        print("Wrong, guess lower")

    guess = int(input("Enter the number: "))
    count += 1

print("Correct Guess")
print("Turns = ",count)





# population of town is 10k, it is increasing at 10 percent per year. What is the population at the end of each year of the last 10 year.

pop = 10000

for i in range(10,0,-1):
    print(i,pop)
    pop = pop/1.1


#ORR
pop = 10000

for i in range(0,10):
    pop = 1.1 * pop
    pop = pop//1
    print("Population at the end of", i+1, "year is", pop)




# Sum of sequence till nth term
# 1/1! + 2/2! + 3/3! + ....

n = int(input('enter n'))
sum = 0
fact = 1

for i in range(1,n+1):
    fact = fact * i
    sum = sum + i/fact
print(sum)


#ORR
import math as m
n = int(input("enter n: "))
sum = 0

for i in range(1,n+1):
    factor = (i/m.factorial(i))
    # print(factor)
    sum = sum + factor

print(sum)




# Sum of sequence till nth term
# 1/1! + 2/2! + 3/3! + ....

n = int(input("enter n: "))
sum = 0
factorial = 1

for i in range(1,n+1):
    factorial *= i
    sum += i/factorial

print(sum)




# Print Pattern

n = int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end="")
    for k in range(i-1, 0, -1):
        print(k, end="")

    print()





# Print prime number between a range

lowerNum = int(input("Enter the lower number: "))
upperNum = int(input("Enter the upper number: "))

for i in range(lowerNum, upperNum+1):
    prime = True
    for j in range(2,i):
        if i%j == 0:
            prime = False
            break

    if prime == True:
        print(i)





# Find length of a str without using len()

s = input("Enter the string: ")
count = 0
for i in s:
    count += 1
print(count)




# Extract username from email, (the part before @)

email = "tejashegde@gmail.com"
pos = email.find('@')
print(email[:pos])




# Count the frequency of a particluae character in a provided string

s = input("Enter the string: ")
search = input("What would you like to search: ")
count = 0
for i in s:
    if i == search:
        count += 1
print("Frequency: ", count)




# Write a prog to remove a perticular char from a string

s = input("Enter the string: ")
c = input("Enter the char to remove from the string: ")
r = ""
for i in s:
    if i != c:
        r = r+i
print(r)
    



# Check palindrome string

s = input("Please enter the string: ")
sr = s[::-1]
if s == sr:
    print("palindrome")
else:
    print("Not Palindrome")


#ORR
s = input("Please enter the string: ")
flag = True
for i in range(0,len(s)//2):
    if s[i] != s[len(s) - i - 1]:
        flag = False
        print("Not a palindrome")
if flag:
    print("Palindrome")




# Write a program to count the number of words in a string without using split()

s = input("Please enter the string: ")
L = []
temp = ''
count = 1
for i in s:
    if i != ' ':
        temp = temp + i
    else:
        L.append(temp)
        temp = ''
        count += 1
        
L.append(temp)
print(L)
print(count)


#ORR
s = input("Please enter the string: ").strip()
if not s:
    print(0)
else:
    count = 0
    for i in range(0,len(s)-1):
        if s[i] == " " and s[i+1].isalnum():
            count += 1

    print(count+1)




# Write a program to conver a string to title case without using the title()

s = input("Please enter the string: ")
L = []
for i in s.split():
    L.append(i[0].upper() + i[1:].lower())
    
print(" ".join(L))  




# Write a program that can convert an integer to string

number = int(input("Enter a number: "))
digits = '0123456789'
result = ''
while number != 0:
    result = digits[number % 10] + result
    number = number//10

print(result)
print(type(result))
