import math

print(math.pi)

# https://thepythonguru.com/python-numbers/

# int 45
# float 2.3
# complex 3+2j

#x = 12
#xtype = type(x)
#print(xtype)
#print(type(x))

#xt = input("Number:") # inputs are read in as strings
#print(type(xt))

# Python Operators

print("addition: 2 + 2 = ", 2 + 2)
print("subtraction: 21.1 - 4 = ", 21.1 - 4)
print("multiplication: 300 * 30 = ", 30 * 30)
print("float division: 1 / 2 = ", 1 / 2)
print("integer division: 1 // 2 =", 1 // 2)
print("exponentiation: 2 ** 4 = ", 2 ** 4)
print("remainder: 20 % 3 = ", 20 % 3)

def namelist(names):
    s = "{} & {}".format(", ".join(name["name"] for name in names[:-1]),names[-1]["name"])
    return s

a = namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])
print(a)
