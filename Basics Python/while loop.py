# loops in python
# doing something repeatedly
# traversing through a sequence (like a list, tuple, dictionary, set, or string) is called iteration
# running series of statements multiple times is called looping

# while loop
# while loop is used when the number of iterations is not known beforehand
# it continues until a certain condition is met
# WAP to print "Nielsen" for 5 times
a = 0
while a < 5:
    print("Nielsen")
    a = a+1

# WAP to print numbers from 1 to 10
b = 1
while b <= 10:
    print(b)
    b+= 1

# infinite loop
while True:
    print("This will run forever unless stopped manually")
    # Uncomment the next line to break the loop after 5 iterations
    # if a > 5: break
    a += 1
    if a > 5: break  # This will prevent an infinite loop for demonstration purposes

