# Literals is the value assigned to the variable

a = 0b1010 # Binary literal - 0b identifies binary
print(a)
b = 100 # Decimal literal
c = 0o310 # Octal literal - 0o means octal
print(c)
d = 0x12c # Hexadecimal
print(d)


# Floating Literal
float1 = 10.5
float2 = 1.5e5 # 1.5 * 10^5
float3 = 1.5e-5 # 1.5 * 10^-5
print()
print(float1, float2, float3, sep="\n")


# Complex Literals
print()
a = 3+5j
print(a.real, a.imag , sep = "\n")

# String Literals
print()
string1 = "hello"
string2 = 'world'
string3 = """ ** Hello                         
World"""
print(string1, string2,string3, sep="\t")

raw_str = r"raw \n string" # Raw String - start using r" " - considers everything within " "
print(raw_str)

uni = u"\U0001F600\U0001F600\U0001F600\U0001F600" # unicode string - start using u" "
print(uni)


# Boolean Literals
a = True + 4 # True = 1
b = False - 10 # False = 0
print()
print(a, b, sep="\n")


#special literal
a = None
print(a)
