# Dictionary is a collection of key value pairs
# items are unordered 
# keys are unique (values can be duplicate) 
# values can be of any data type
# Dictionary is defined using curly braces {}

d = {101: 'abc', 102: 'xyz', 103: 'abc'}  # Dictionary with integer keys and string values
print(d)  # Display the dictionary d
print(type(d))  # Display the type of d, which should be <class 'dict'>
print(d[101])  # Accessing the value associated with key 101

#Adding a new key-value pair to the empty dictionary 
d1 ={}
d1['xyz'] = 99
d1['prs'] = 88
print(d1)
print(d1['xyz'])  # Accessing the value associated with key 'xyz'

print(d1.get('prs'))  # Using get method to access value associated with key 'prs'
print(d1.get('abc'))  # if key 'abc' is not found in d2 it shows None instead of raising an error
print(d1.get('abc', 'NA'))  # if abc is not present in dictionary, it will return 'NA'

print(len(d1))  # Getting the number of key-value pairs in d1, which should be 2
d1['xyz'] = 100  # Updating the value associated with key 'xyz'
print(d1)  # Display the updated dictionary d1
print(d1.pop('xyz'))  # Removing the key 'xyz' and its associated value from d1
print(d1)  # Display the dictionary d1 after removing 'xyz'
del d1['prs']  # Deleting the key 'prs' from d1
print(d1)  # Display the dictionary d1 after deleting 'prs'
print(d.popitem())  # Removing last inserted key-value pair
print(d1)  # Display the dictionary d1 after popping the last item
d1.clear()  # Clearing all key-value pairs from d1       