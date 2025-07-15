# Type conversion in Python
# Type conversion is the process of converting one data type to another
# There are two types of type conversion:
# 1. Implicit Type Conversion: Automatically done by Python
# 2. Explicit Type Conversion: Done by the user using built-in functions

# Implicit Type Conversion
# Python automatically converts smaller data types to larger data types
# Example: int to float 
x = 10  # Integer
y = 5.5  # Float
z = x + y  # Implicit conversion from int to float
print(z)  # Output: 15.5

# Explicit Type Conversion
a = '100'   # String
b = 200    # Integer
c = int(a) + b  # Explicit conversion from string to int
print(c)  # Output: 300

a = 'abc'   # String
b = 'gfd'    # Integer
c = a + b  # Explicit conversion from string to int
print(c)  # Output: 300 

s = 'shree' # String
print(list(s))   # Converting string to list, Output: ['s', 'h', 'r', 'e', 'e']
print(tuple(s))  # Converting string to tuple, Output: ('s', 'h', 'r', 'e', 'e')
print(set(s))    # Converting string to set, Output: {'s', 'h', 'r', 'e'} (order may vary)

l = ['a', 10, 'c']  # List
print(str(l))

q = 10
r = 20
print(str(q) + str(r)) # Converting integers to strings and concatenating, Output: '1020'

t = 12.6
print(str(t))  # Converting float to string, Output: '12.6' 
print(tuple(l))  # Converting list to tuple, Output: ('a', 10, 'c')




