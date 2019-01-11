# Strings

#strings are immutable

name = "tom"
mychar = 'a'

name1 = str() # creates an empyt string
name2 = str("newstring")


print(name,name[0])

s = "tom and " + "jerry"
print(s)

s = "this is bad spam " * 3
print(s)

# slicing string
# syntax: s[start:end]

s = "Welcome"
print(s[1:3])
print(s[:-1])


# in and not in
s = "Welcome"
print("come" in s) # True
print("come" not in s) # False

# string comparison > < <= >= == !=
print("one != two", "one" != "two")

m = "aabcdddef"
for i in m:
    print(i, end="")

print("")