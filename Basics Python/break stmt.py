# break statement in python
# The break statement is used to exit a loop prematurely
# It can be used in both for and while loops
# Example of break in a for loop
l = [10, 20, 30, 40]
for x in l:
    if x == 30:
        break  # Exit the loop when x is 30
    print(x)  # This will print 10 and 20, but not 30

# Example of break in a while loop
a = 0
while a < 5:
    if a == 4:
        break
    print(a)
    a += 1  # This will print 0, 1, 2, and 3, but not 4

# continue statement in python
# The continue statement is used to skip the current iteration of a loop
# If cond'n statisfied do not print continue to next iteration

for x in l:
    if x == 30:
        continue  # Skip the rest of the loop when x is 30
    print(x)  # This will print 10, 20, and 40, but not 30  

# Example of continue in a while loop
b = 0
while b < 5:
    b += 1
    if b <= 3:
        continue  # Skip the rest of the loop when b is 3
    print(b)  # This will print 1, 2, 4, and 5, but not 3

