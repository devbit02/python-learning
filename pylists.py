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
#[print(x) for x in range(4) if print('checking') or True]

def title_case(title, minor_words):
    t = title.lower()
    m = minor_words.lower()
    result = map(lambda x, y: if x not in y: x.capitalize(), title, minor_words)
    return result

print("KINGS".capitalize())
print("a clash of KINGS".lower().split(" "))
title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings'