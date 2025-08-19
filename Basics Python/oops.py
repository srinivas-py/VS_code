# slicing (list, tupple & string)
l = [10, 20, 30, 40, 50]
print(l[0 : 5 : 2]) # [start - stop - increment]

# Introduction to object oriented programming
# oops > we break the code onto a set of entities ans these entities are talk to each other and it contains data & methods

# encapsulation - refers to data hiding
# It helps in consistency & reduce redudency
# Bundling of data member and method
from abc import ABC, abstractmethod  # (11 & 12 - abstart class)
class Polygon(ABC):
    def __init__(self, color):
        self.color = color
    @abstractmethod
    def printsides(self):            # (15, 16 & 17 - abstart method)
        pass

class triangle(Polygon):
    def __init__(self, color):
        super().__init__(color)
    def printsides(self):
        print("there are 3 sides")

# decoraters in python
# functions are first class objects
# function can have innner functions
# decorater is a func that takes another func as an argument and enhances the behaviour of the passed functions

def decfun(f):
    def innerfun():
        print("inside decfun")
        f()
    return innerfun

@decfun
def fun():
    print("inside func1")
fun()

# ASCII codes
# [0 - 9] = [48 - 57]
# [A - Z] = [65 - 90]
# [a - z] = [97 - 122]
# ord will use to get the ascii value
print('A')
print(ord('A'))
print(ord('a'))

# exception handling > try catch method
try:
    q = 10
    print(q/0)
except:
    print('error')
# pass case
try:
    e = 33
    print(e)
except:
    print('error occured')
# using double exception
try:
    f = 90
    print(90-0)
except ZeroDivisionError:
    print('zero in the division')
except:
    print('unknown error')
finally:
    print('finally will end the code either by terminating / completing')

