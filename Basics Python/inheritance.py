# inheritance in python
class Person:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name

# this program is example for single inheritance
class Employee(Person):
    def __init__(self, ID, name, salary):
        Person.__init__(self, ID, name)
        self.salary = salary
    def display(self):
        print(self.ID, self.name, self.salary)
e = Employee(109, "shree", 100000)
e.display()

# Object class - if you create a sub class without any parent class and it happens from python 3.xx
# Types of inheritance in python
# Single - one parent one child class
# Multilevel - parent > child > grandson
# Herirarchal - one parent class with different child class
# multiple - one child > multiple parent class  - normally we avoid using multiple inheritance
# hybrid - mix of 2 or more inheritance


