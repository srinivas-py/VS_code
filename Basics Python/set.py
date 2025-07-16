# set contains only unique elements
# Sets are unordered collections 
# Sets are defined using curly braces {} or the set() constructor
# No indexing, slicing in sets
# Sets are mutable, but the elements must be immutable (e.g., numbers, strings, tuples)
s1 = {10, 20, 30, 40, 50}  # Set with unique elements
print(s1)   # Display the set s1
print(type(s1))  # Display the type of s1, which should be <class 'set'>
s2 = {30, 40, 50, 60, 70, 40}  # Another set with some overlapping elements
print(s2)  # Display the set s2 
s3 = {}  # This is an empty dictionary, not a set
print(type(s3))  # Display the type of s3, which should be <class 'dict'>
s4 = set()  # This is an empty set
print(type(s4))  # Display the type of s4, which should be <class 'set'>    

s5 = {10, 20, 30, 40, 50}  # Another set with unique elements
s5.add(60)  # Adding 60 to the set s5
print(s5)  # Display the updated set s5
s5.remove(20)  # Removing 20 from the set s5
print(s5)  # Display the updated set s5 after removal

# In operations works fastly in sets compared to lists
print(30 in s5)  # Checking if 30 is in the set s5  # Should return True
print(100 in s5)  # Checking if 100 is in the set s5 # Should return False

s5.update([66, 77, 77])  # Adding multiple elements to the set s5 using list format
print(s5)  # Display the updated set s5 after adding multiple elements

#removal options in set
s5.discard(10)  # Discarding 10 from the set s5
print(s5)  # Display the updated set s5 after discarding 10

s5.remove(30)  # Removing 30 from the set s5
print(s5)  # Display the updated set s5 after removal

s5.remove(40)  # Removing 40 from the set s5
print(s5)  # Display the updated set s5 after removal   

s5.clear()  # Clearing all elements from the set s5
print(s5)  # Display the empty set s5 after clearing

# Set operations
s6 = {10, 20, 30, 40, 50}   # Another set for operations
s7 = {30, 40, 50, 60, 70}   # Another set for operations
print(s6.union(s7))  # Union of s6 and s7, combining unique elements from both sets
print(s6.intersection(s7))  # Intersection of s6 and s7, common elements in both sets
print(s6.difference(s7))  # Difference of s6 and s7, elements in s6 but not in s7
print(s7.difference(s6))  # Difference of s7 and s6, elements in s7 but not in s6
print(s6.symmetric_difference(s7))  # Symmetric difference, elements in either s6 or s7 but not both
print(s6.issubset(s7))  # Checking if s6 is a subset of s7, should return False
print(s7.issubset(s6))  # Checking if s7 is a subset of s6, should return False
print(s6.issuperset(s7))  # Checking if s6 is a superset of s7, should return False
print(s7.issuperset(s6))  # Checking if s7 is a superset of s6, should return False
print(s6.isdisjoint(s7))  # This checks: Do s6 and s7 have NO elements in common elements but it has common elements > return False
print(s6.isdisjoint({100, 200}))  # Checking if s6 is disjoint with another set, should return True

s8 = {22, 33, 55}
s9 = {44, 66, 77}
print(s8.isdisjoint(s9))  # Checking if s8 and s9 are disjoint, should return True

