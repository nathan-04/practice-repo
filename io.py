# printing
# automatically adds newline
print("hello world")
print (4.5)     # can print literals
print(4.5, "four point five") # automatically adds a space b/w

# can put operations inside print
print("2 + 2 =", 2+2)

# choose how to end the print statement - default is end='\n'
print("hello", end='|')
print("world")

# user input (input returns as a string)
user_name = input("(prompt here) enter name: ")
user_age = input("your age: ") # not a number
print("hello", user_name, "your age is", user_age)

strNum = '10'
str = 'the number 10'
print(int(strNum))
# print(int(str)) this doesnt work