# if, else and elif statements  
if 5 > 2:
    print("Five is greater than two!")  # This will print because the condition is True
else:
    print("Five is not greater than two!")  # This will not print because the condition is False

# WAP to take input from user and check if the number is even or odd
num=int(input("enter a number: "))
if num%2==0:
    print("The number is even")  # This will print if the number is even
else:
    print("The number is odd")  # This will print if the number is odd

# WAP to take input from user and check if the number is positive, negative or zero
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive")  # This will print if the number is positive
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")


# Nested if else statements
# WAP to take input from user and check if the number is positive even, positive odd, negative even or negative odd or zero

n = int(input("enter a number: "))
if n > 0:
    print("Positive ", end="")
    if n%2 == 0:
        print("even")
    else:
        print("odd")
elif n < 0:
    print("Negative", end="")
    if n%2 == 0:
        print("even")
    else:
        print("odd")
else:
    print("The number is zero")


# WAP to take input from user and if a is greater> print "a is greater", if b is greater print "b is greater", if both are equal print "both are equal"
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("a is greater")
elif b > a:
    print("b is greater")
else:
    print("Both are equal")
    