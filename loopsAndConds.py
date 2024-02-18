# conditional flow control
name = input("Your name: ")

# no paren needed around condition
if name == 'nathan' or name == 'Nathan':
    print("Hi", name + ',', "you are great")
elif name == 'Joe':
    print("Hi Joe")
else:
    print("I don't know you")