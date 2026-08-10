# While and For

num = int(input("Enter the number for which you need table: "))
i=1
while i<=10:
    print(i*num)
    i+=1


# While loop with else
# The else block executes only if the loop finishes normally (i.e., the condition x < num becomes false).
#If the loop is forcefully interrupted, the else block is skipped.
num=int(input("Enter the number: "))
x=0
while x<num:
    print(x+1)
    x+=1
else:
    print("Limit crossed")



#### FOR LOOPS

for i in range(1,11):
    print(i)

print()
for i in [1,2,True,"Hello",9.7]:
    print(i)

print()
for i in range(1,11,2):
    print(i)

print()
for i in range(10,0,-1):
    print(i)

print()
for i in "Delhi":
    print(i)



## NESTED LOOOOOOOOOOOOPS

# Unique Pairs
n,m = int(input("enter num1: ")), int(input("enter num2: "))
for i in range(1,n+1):
    for j in range(1,m+1):
        print(i,j)

n,m = int(input("enter num1: ")), int(input("enter num2: "))
for i in range(1,n+1):
    for j in range(1,m+1):
        if j>=i:
            print("(", i,", ", j, ")")

# Print Pattern
n = int(input("enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end="")
    print()


# Print Pattern
n = int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end="")
    for k in range(i-1, 0, -1):
        print(k, end="")

    print()



### Loop control statement - break, continue, pass
for i in range(1,11):
    print(i)

for i in range(1,11):
    if i == 5:
        break
    print(i)

for i in range(1,11):
    if i == 5:
        continue
    print(i)

for i in range(1,11):
    pass


