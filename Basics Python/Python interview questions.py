# Python 3 uses print() as a function, whereas Python 2 allows print as a statement.

#Python 3
#print("Hello")
# Python 2
# print "Hello"

a = [1, 2, 3]
b = a  # Reference count of [1, 2, 3] increases
del a  # Reference count decreases but object persists as b points to it

'''What is the significance of PEP 8 in Python?
PEP 8 is the Python Enhancement Proposal for style guidelines that improve the readability and consistency of Python code. Key points include:

Use 4 spaces for indentation.
Limit lines to 79 characters.
Use meaningful variable names.
Use blank lines to separate functions and classes.
Avoid unnecessary whitespace.'''

'''What are the different data types in Python?
Python’s core data types include:

Numeric Types: int, float, complex
Sequence Types: str, list, tuple
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview
None Type: NoneType'''

''' What is the difference between a list and a tuple?
List:                                                     Tuple:
A mutable sequence used to store a collection of items    An immutable sequence used to store a collection of items.
Mutable: Elements can be modified, added, or removed.	  Immutable: Once defined, elements cannot be changed.
Defined using square brackets: [ ]	                      Defined using parentheses: ( )
Suitable for collections that need to change during program execution.	 Suitable for fixed data or read-only collections to ensure immutability.
Takes more memory due to extra data structures for mutability.	Takes less memory due to simpler internal structure.
Supports methods like append(), remove(), pop(), extend().	Does not support these methods since it is immutable '''

# Interpreter = Cooking Step-by-Step with Help
# An interpreter is like a friend who reads the recipe one line at a time and tells you exactly what to do right then.
# Example: Python uses an interpreter.
#  Compiler = Read Entire Recipe First, Then Cook Fast
# A compiler is like reading the whole recipe first, understanding it completely, and turning it into your own super-efficient cooking plan before you even start.
# C or C++ use a compiler.
'''
Difference Between Mutable and Immutable Types in Python
Feature	    Mutable	                                        Immutable
Definition	Objects that can be changed after creation.	    Objects that cannot be changed after creation.
Data Types	list, dict, set, bytearray.	    int, float, str, tuple, frozenset.
Behavior	Changes to the object do not create a new object.	    Changes require creating a new object.
Memory Efficiency	Less memory-efficient as changes happen in place.	    More memory-efficient as objects are fixed.
Hashability	Not hashable, cannot be used as dictionary keys.	    Hashable if they contain only hashable elements.
Use Cases	Used for collections that need updates or changes.	    Used for fixed data to ensure consistency '''

'''
What are Python’s built-in data structures, and when should you use each?
List: Ordered, mutable collection ([1, 2, 3]). Use for sequential or changing data.
Tuple: Ordered, immutable collection ((1, 2, 3)). Use for fixed data.
Set: Unordered, unique collection ({1, 2, 3}). Use for eliminating duplicates.
Dictionary: Key-value pairs ({'key': 'value'}). Use for mappings or lookups.'''

'''
What is the difference between is and == in Python?
is: Checks object identity (same memory location).
==: Checks object values'''
a = [1, 2]
b = [1, 2]
print(a == b)  # True (same values)
print(a is b)  # False (different memory locations)

'''
How does Python handle type conversion?
Python provides:

Implicit Conversion: Automatically converts compatible types.
Example: a = 5 + 2.5 (int → float)
Explicit Conversion: Done using functions like int(), float(), str().
Example: b = int('10') '''

'''
What is the difference between // and / in Python?
/: Performs true division, returning a float.
//: Performs floor division, returning the largest integer less than or equal to the result. '''
print(7 / 2)   # Output: 3.5
print(7 // 2)  # Output: 3

'''
. Explain operator precedence in Python with an example.
Operator precedence determines the order of evaluation in expressions.
Order (Highest to Lowest):

Parentheses ()
Exponentiation **
Multiplication/Division *, /, //, %
Addition/Subtraction +, -
Comparison Operators <, >, ==, etc.'''
result = 2 + 3 * 4  # Multiplication first, then addition
print(result)  # Output: 14

'''
Escape sequences are special characters used to represent certain actions within strings:

\n: Newline
\t: Tab
\\: Backslash
\': Single quote
\": Double quote'''

'''
None: Represents the absence of value.
False: Boolean value representing "not true."
0: Numeric value.'''

'''
Explain the difference between for and while loops in Python.
Feature	for Loop	while Loop
Purpose	Iterates over a sequence (e.g., list).	Executes based on a condition.
Termination	Stops after the end of the sequence.	Stops when the condition is false.
Usage	Best for iterating a known range.	Best for indefinite loops.'''

'''
How does Python’s range() function work in a for loop?
The range() function generates a sequence of numbers:

range(stop): Generates numbers from 0 to stop-1.
range(start, stop): Generates numbers from start to stop-1.
range(start, stop, step): Generates numbers with a step size.'''
for i in range(10, 50, 5):
    print(i)
'''
 What is the purpose of the break statement?
The break statement is used to exit a loop prematurely, even if the loop condition has not been satisfied. Example:'''
for i in range(5):
    if i == 3:
        break
    print(i)  # Outputs: 0, 1, 2
'''
Differentiate between break and continue statements in Python.
Feature	break	continue
Purpose	Exits the loop entirely.	Skips the current iteration and continues the loop.
Effect	Ends loop execution.	Proceeds to the next iteration.
Example	if x == 5: break stops the loop.	if x == 5: continue skips iteration.'''
for i in range(5):
    if i == 3:
        continue
    print(i)  # Outputs: 0, 1, 2

'''
 Can a for loop in Python iterate over non-sequential data types?
Yes, a for loop can iterate over any iterable object, including strings, sets, and dictionaries.'''
dict = {1:'a', 2:'b', 3:'c'}
for key in dict:
    print(key)

'''
What is a nested loop, and when is it used?
A nested loop is a loop inside another loop, used for multi-dimensional data processing.
Example:'''
for i in range(10):
    for j in range(5):
        print(i, j)  #output: 00 01 02 03..

# How do you iterate through a dictionary’s keys and values?
dict = {1:'a', 2:'b', 3:'c'}
for key, value in dict.items():
    print(f"key: {key}, Value: {value}")

# . How do you iterate over multiple sequences in parallel?
# Use the zip() function:
list1 = [1, 2, 3, 4]
list2 = ['q', 'r', 't', 'u']
for x, y in zip(list1, list2):
    print(x, y)
'''What are the different types of for loops in Python?
Iterating over a sequence: Iterating through lists, strings, or other iterable objects.
Range-based loops: Using range() to iterate over a fixed number of iterations.
Enumerate: Iterating over an iterable with an index.'''
for index, value in enumerate(['a', 'b', 'c', 'd']):
    print(index, value)

# Q20. What are Decorators?
# Decorators in Python are a powerful feature that allows you to modify or extend the behavior of functions or classes without permanently changing their code.
# How Decorators Work
# A decorator is essentially a function that takes another function as an argument and returns a modified version of that function.
#syntax
'''@decorator_name
def function_to_decorate():
    pass'''

# Q21. How do you debug a Python program?
# By using this command we can debug a Python program:
# $ python -m pdb python-script.py

# Swapcase function > The swapcase() method in Python is a built-in string method that converts all uppercase letters to lowercase and all lowercase letters to uppercase in a string.
# Non-alphabet characters (like numbers, spaces, or symbols) remain unchanged.
string = "Geeks for Geeks"
print(string.swapcase())   #---> "gEEKSFORgEEKS"
print(string[2:8])

#  What are some common string operations?
# Concatenation: Joining strings using + or join().
# Repetition: Repeating strings using *.
# Search: Using in, find(), or index().
# Case Conversion: Using upper(), lower(), capitalize().
# Trimming: Removing whitespace using strip().

# 18. What is the difference between concatenating multiple strings using + and using .join()?
# Using + for multiple concatenations creates a new string each time, which can be inefficient for large operations.
# Using .join() is more efficient as it creates the final string in a single operation.
words = ['python', 'is', 'easy']
sentence = " ".join(words)
print(sentence)

#  Explain the difference between @staticmethod, @classmethod, and instance methods.
# Instance Methods: Operate on an instance of the class (self) and can access and modify instance variables.
# Class Methods: Operate on the class itself (cls) and cannot modify instance-specific data.
# Static Methods: Do not operate on either instance or class. They are utility functions.

# Instance method → Painting your house.
# Class method → Updating the blueprint so all future houses use solar panels.
# Static method → A calculator that tells you how much paint you’ll need

# How is encapsulation implemented in Python, given that it lacks access modifiers like private or protected?
# Encapsulation in Python is achieved using naming conventions:
# Public Members: No prefix (e.g., self.value).
# Protected Members: Single underscore prefix (e.g., _value).
# Private Members: Double underscore prefix (e.g., __value), which invokes name mangling.

# What is the assert keyword and when should it be used?
# assert is used for debugging purposes, ensuring that a condition is true. If the condition evaluates to False, it raises an AssertionError. It is often used during development to catch bugs early.
assert 2 + 2 == 4  # Passes
assert 2 + 2 == 5  # Raises AssertionError


