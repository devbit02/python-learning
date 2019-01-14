# resources
# https://docs.python.org/3.7/contents.html
# https://docs.python.org/3.7/tutorial/datastructures.html

line = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
list_names = [{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]

print("# get one item from the list")
print(list_names[2]["name"])

def namelist(names):
    s = "{} & {}".format(", ".join(name["name"] for name in names[:-1]),names[-1]["name"])
    return s

a = namelist(list_names)
print(a)

print(line)

a = 0
for x in range(4):
    a += x**3

print(a)


