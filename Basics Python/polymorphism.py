# polymorphism - one name having different forms
# method overriding comes under polymorphism
# method overriding - child class has same name and same parameter method as parent class

class Employee:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
    def display(self):
        print(self.ID, self.name)

class Salesman(Employee):
    def __init__(self, ID, name,salary ):
        super().__init__(ID, name)
        self.salary = salary
    def display(self):
        super().display()
        print(self.salary)
el  = [Employee(101, 'shree'), Salesman(102, "gowda", 100000)] #list of employee
for e in el:
    e.display()

# operator overloading - example of ploymorphism
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __add__(self, other):
        return self.price + other.price
p1 = Product("A", 100)
p2 = Product("B", 200)
print(p1 + p2)