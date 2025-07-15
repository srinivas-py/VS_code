#No need to specify data types before declaring in Python(as compared to java C++)
#All python files in .py format
#can declare diff data types for same variable in python

#swapping two variables 
#introducing extra variables 
x=100
y=200
temp = x
x=y
y=temp
print(x)
print(y)

#using comma assignment(using comma can use multiple values with multiple variables)
a=100
b=200
a, b = b, a   #using comma assignment
print(a)
print(b)

#is operator will give the Boolean value (a=1 & b=2) print(a is b) > True

#id() function:
#it gives id of the object
print(id(5))
s=10
print(id(s))
r=s
print(id(r))

#Type(): is a built in function and tells the data type of var
print(type(10)) 
print(type(10+5j)) 
print(type(True))
print(type("hello python"))
print(type([1, 2, 3]))


