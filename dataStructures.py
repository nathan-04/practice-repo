# collections / data structures

# lists (ordered, mutable, reference type)
# **REFERENCE VARIABLE: LIST NAMES ARE POINTERS, WATCH FOR ALIASING
# define with square brackets (can be empty)
# can have different data types, can have e.g. list of lists of tuples
# index the normal way
list_x = [4, 5, 'hi']
# print(list_x[1])
# print("length:", len(list_x))

# copy without aliasing, iterate through old list elements
new_list = list_x[:]
new_list.append("update")
# print("x:", list_x)
# print("new list:", new_list)


# to add or remove elements
list_y = [1, 2]

# add an element
list_y.append(3)
# print("initial values of list x and list y")
# print("x:", list_x)
# print("y:", list_y)

# append any iterable to a list
list_y.extend(list_x)
# print("values of list x and list y after y.extend(x)")
# print("x:", list_x)
# print("y:", list_y)

# remove last element or specified element with pop()
last_elt = list_y.pop()
# print("removed last element:", last_elt)
# print("y:", list_y)
first_elt = list_y.pop(0)
# print("removed first element:", first_elt)
# print("y:", list_y)

# tuples (ordered, immutable)
# cannot change elements, cannot append or pop
# define with parens (can be empty)
# index the normal way
tuple_x = (1, 2, 3)
print("x:", tuple_x)
print("x[1]:", tuple_x[1])
print("length:", len(tuple_x))


# enumarate() method
# enum objects not subscriptable but are iterable
list_e = ['a', 'b', 'c']
enum1 = enumerate(list_e)
print(list(enum1))