# operations

# must have compatible types on each side of arithmetic op
# cant add number to str, can do any two number types
x = 5
y = 2
sum = x + y
diff = x - y
product = x * y
quotient = x / y    # division always returns float, result = 0.75
int_quotient = x // y   # integer division (floor)
exp = x ** y       # exponent, x^y
mod = x % y         # modulo

print(sum)
print(diff)
print(product)
print(quotient)
print(int_quotient)
print(exp)
print(mod)

# incrementing
# no ++ or -- unary operator
# can us +=, -=, etc.
i = 1
i += 1

# string methods
name = "nathan"
print(name.upper())
print(name.capitalize())
print(name.count('n'))

# can add strings together (concatenation) and multiply them
print(name + " moore")
name3 = name * 3
print(name3)

# conditional operators
print(x == y)
print(x > y)
print(x >= y)
print(name == 'nathan') # can check equality of strings
print('abc' < 'abd') # can use to check alphabetical order
print('a' > 'b')

# arithmetic ops come first
print(3 + 2 < 3 * 2)

# precedence = not > and > or
print(3 > 2 and 3 >= 4)
print(3 > 2 or 3 >= 4)
print(not 3 > 2)