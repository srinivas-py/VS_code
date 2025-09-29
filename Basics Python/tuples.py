# Tuples are immutable sequences in Python, similar to lists but cannot be changed after creation
# Tuples are faster then lists and can be used to store a collection of items
# Tuples are defined using parentheses () and can contain mixed data types
t = (10, 20, 'abc', 35.5, True)  # Tuple with mixed data types
print(t)
print(type(t))  # Display the type of t, which should be <class 'tuple'>
print(t[2])  # Accessing the third element of the tuple 

t2 = 50, 60   # Another tuple   brackets are optional

print(t + t2)  # Concatenating two tuples

print(t * 2)   # Repeating the tuple twice

print(sum(t2))  # Summing the elements of t2, which should be 110

print(len(t))  # Getting the length of the tuple, which should be 5     

#t2.sort()  # This will raise an error because tuples do not have a sort method
print(20 in t)  # Checking if 20 is in the tuple, should return True

print(t.count(10))  # Counting occurrences of 10 in the tuple, should return 1

print(t.index('abc'))  # Finding the index of 'abc' in the tuple, should return 2

print(t[1:3])  # Slicing the tuple from index 1 to 2 (3 is not included)