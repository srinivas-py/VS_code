# end & sep in print statements
# end parameter are used to specify what to print at the end of the output
# sep parameter is used to specify what to print between the output

print("Hello", "World", end="!")  # Output: Hello World!
print("Hello", "World", sep=", ")  # Output: Hello, World
print("Hello", "World", sep=" ", end="!")  # Output: Hello World!

print("welcome", end=" ")  # Output: welcome
print("to FNF")

print("python", "is", "fun", sep="-")  # Output: python-is-fun

# inpput() function
name = input("Enter your name : ")
age = input("enter your age is : ")
print(name + age)  # Prompts user for input

# take 2 num & print their sum
num1 = input("enter num1 :")
num2 = input("enter num 2 :")
res = int(num1) + int(num2)  
print(res)
