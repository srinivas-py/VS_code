# slicing (list, tupple & string)
l = [10, 20, 30, 40, 50]
print(l[0 : 5 : 2]) # [start - stop - increment]

# OOP is a programming paradigm based on the concept of "objects", which can contain data (attributes) and code (methods).
# Instead of writing procedural code, we model real-world entities as classes and objects.
# Key Idea: Break complex problems into smaller, manageable pieces (objects) that interact with each other.
# Example: A simple class
class Car:
    def __init__(self, brand, model):
        self.brand = brand    # data attribute
        self.model = model

    def start(self):          # method
        print(f"{self.brand} {self.model} is starting.")

my_car = Car("Toyota", "welfire")  # Creating objects (instances)
my_car.start()  # Output: Toyota welfire is starting.

# Core OOP Concepts in Python
# Class: Blueprint or template for creating objects.
# Object: Instance of a class.

#Encapsulation:
# Encapsulation = Data + Methods bundled together + Controlled access
# It restricts direct access to some components (data hiding).
# Achieved using private and protected members.
# Data integrity, security, reduces complexity.

# Access Modifiers in Python (by convention):
# Public: name → accessible everywhere.
# Protected: _name → should not be accessed outside class (but possible).
# Private: __name → name-mangled to prevent accidental access.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # public
        self._balance = balance  # protected (by convention)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def get_balance(self):  # controlled access
        return self._balance


acc = BankAccount("John", 1000)
print(acc.owner)  # OK
print(acc.get_balance())  # Preferred way


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


# Class > Blueprint for objects > class MyClass:
# Object > Instance of a class > obj = MyClass()
# Encapsulation > Bundle data + methods; control access > _protected , __private, getters/setters
# Abstraction > Hide complexity; show essentials, ABC > @abstractmethod
# Inheritance > Reuse code from parent > class Child(Parent):
# Polymorphism > Same interface, different behavior > Method overriding

# Why Use OOP in Python?
# ✅ Modularity: Code organized into classes.
# ✅ Reusability: Inheritance avoids rewriting code.
# ✅ Maintainability: Changes in one class don’t break others.
# ✅ Scalability: Easy to extend with new features.
# ✅ Real-world modeling: Natural way to represent entities.



