# it is a small anonymous function
# lambda a,b: a+b
# lambda parameter: expression


# Characteristic / Diff between lamdba and normal function
# 1. No name
# 2. lambda doesn't return any value (infact, it returns entire function)
# 3. not reusable
# 4. lambda is written in 1 line

# it is used with higher order function - the functions which returns a function or the function that recieves a function as an input

# number to square
a = lambda a: a*a
print(a(9))
# for i in range(1,11):
#     print(a(i))


# sum of number
exp = lambda x,y: x+y
print(exp(1,2))


# check if string has 'a'
exp = lambda st: 'a' in st
print(exp('hello'))
print(exp('tejas'))


# odd or even
exp = lambda x: x%2==0
o_e = exp(5)
if(o_e == 1): print('even')
else: print('odd')

exp = lambda x: 'even' if x%2==0 else 'odd'
print(exp(4))
print(exp(5))



#### One line code in List Comprehension (to comapre with lambdas)
x1 = [i for i in range(40)]
x2 = [i for i in x1 if i%2==0]
x3 = ['even' for i in x1 if i%2==0]
x4 = [[i for i in range(0,4)] for j in range(0,4)]
x5 = [[[i for i in range(0,4)] for j in range(0,4)] for k in range(0.4)]
x6 = ['even' if i%2 ==0 else 'odd' for i in x1]

