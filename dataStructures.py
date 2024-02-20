# collections / data structures

# LISTS (ordered, mutable, reference type)
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

# TUPLES (ordered, immutable)
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

# slice operator (works for string, list, tuple)
# slicedIterable = [start:stop:step] (from start to stop-1 as usual)
listA = [1,2,3,4,5,6]
oddsA = listA[0:len(listA):2]
firstFour = listA[:4]
lastFour = listA[len(listA) - 4:]
revSlice = listA[4:1:-1]
reverseList = listA[::-1] # nifty way to reverse a list
print(oddsA)
print(firstFour)
print(lastFour)
print(revSlice)
print(reverseList)
# get even entries of a tuple
print((0,1,2,3,4,5,6,7,8)[::2])

# SETS (unique entries, order doesn't matter)
setX = set()    # empty set constructor, dont use empty {}
setY = {1,2,3}  # set literal creation, dont use empty {}
setY.add(5)
setY.remove(3)
flag = 5 in setY    # check if set contains 5
setX.union(setY)
setX.intersection(setY)
setX.difference(setY)

# DICTIONARIES - (key, value) pair (like a map or hash table)
# value can be any data type or data structure, keys maybe anything but certainly number or string
dict_x = {'key1': 5, 'key2': 8}
print(dict_x['key2'])
dict_x['key3'] = 12     # insert new key, value pair
flag2 = 'key3' in dict_x
dict_x.values()     # get all values
dict_x.keys()       # get all keys
list_of_dict_vals = list[dict_x.values()]
del dict_x['key3']       # remove key3 and value from dict

# comprehensions
# a one-line way to construct an iterable
# var_name = [ elt_expr for elt in range() ]
comp_list = [(3 * x) for x in range(1, 5)]   # print multiples of 3
print(comp_list)
many_lists = [[x for x in range(5)] for x in range(3)]      # make list of 3 lists of [0,1,2,3,4]
print(many_lists)
# conditional construction
multiples_of_17 = [x for x in range(100) if x % 7 == 0]
print(multiples_of_17)
# works for dict and tuple too
dict_seventeens = {x:2*x for x in range(100) if x % 7 == 0}       # vals initialized to 2*key
tuple_seventeens = tuple(x for x in range(100) if x % 7 == 0)    # need tuple keyword
print(dict_seventeens)
print(tuple_seventeens)