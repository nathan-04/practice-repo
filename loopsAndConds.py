# conditional flow control
#name = input("Your name: ")
name = 'nathan'

# no paren needed around condition
if name == 'nathan' or name == 'Nathan':
    print("Hi", name + ',', "you are great")
elif name == 'Joe':
    print("Hi Joe")
else:
    print("I don't know you")

# for loops
# range fn: range(stop), range(start, stop), range(start, stop, step)
for i in range(3):
    print(i)

# for i in range(10, 13):
#     print(i)

# for i in range(1, 6, 2): # prints 1,3,5
#     print(i)

# for loop using list
list_x = [100, 200, 300]
# for i in list_x:
#     print(i)

# for loop using enumerate
for count, element in enumerate(list_x):
    print(count, element)

# while loops
i = 0
while i < 5:
    print(2 * i)
    i += 1