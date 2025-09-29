# range() in python
# range() is a built-in function that generates a sequence of numbers
# It is commonly used in for loops to iterate over a sequence of numbers
# range(start, stop, step) generates numbers starting from 'start' to 'stop - 1

r = range(0, 5)  # Generates numbers from 0 to 4
print(r)  # Display the range object
print(type(r))  # Display the type of r, which should be <class 'range'>

l = list(r)
print(l)  # Convert the range object to a list and display it
t = tuple(r)
print(t)  # Convert the range object to a tuple and display it
s = set(r)
print(s)  # Convert the range object to a set and display it

r1 = range(11)
print(r1)

r2 = range(10, 20, 3) # Generates numbers from 10 to 19 with a step of 3
l1 = list(r2)
print(l1)

# range() can also be used in for loops
for i in range(5):
    print(i)  # This will print numbers from 0 to 4 
# Using range() with a step value
for i in range(1, 10, 2):   
    print(i)  # This will print odd numbers from 1 to 9
    