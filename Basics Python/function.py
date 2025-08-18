# Functions in python
def func():
    print("Hello")
func()
print("my name is python")


# By passing the parameters to the function
def fun2(d, m, y):
    print(d, m, y, sep=',')

print("My b'day is on")
fun2('16', '09', '1998')


def fun3(d, m, y):
    return d+"-"+m+"-"+y
e = fun3('16', '09', '1998')
print(e)

# passing parameters
def fun4(l):
    l.append(5)
    return l
l = [10, 20, 30, 40]
fun4(l)
print(l)

# function returning multiple values
def fun5(a, b):
    sum = a + b
    sub = a - b
    mul = a * b
    return sum, sub, mul

s, sub, mul = fun5(12, 8)
print(s)
print(sub)
print(mul)



