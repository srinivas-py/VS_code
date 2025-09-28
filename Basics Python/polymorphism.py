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
class Bird:
    def fly(self):
        print("Some birds can fly.")

class Ostrich(Bird):
    def fly(self):  # Overridden
        print("Ostriches cannot fly.")

b = Bird()
o = Ostrich()
b.fly()  # Some birds can fly.
o.fly()  # Ostriches cannot fly.


#  What is Abstraction?
# Abstraction = Hiding complex details and showing only essential features.
# It lets you focus on "what" an object does, not "how" it does it.

# Step 1: Create a class that hides internal details
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # __ means "private" (hidden)

    # Public method to check balance
    def get_balance(self):
        return self.__balance

    # Public method to withdraw money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance = self.__balance - amount
            print("Withdrawal successful!")
        else:
            print("Insufficient funds!")


# Step 2: Use the class (user doesn't see the hidden details)
# Create an account with $100
my_account = BankAccount(100)

# Check balance
print("Current balance:", my_account.get_balance())

# Try to withdraw $30
my_account.withdraw(30)

# Check balance again
print("Current balance:", my_account.get_balance())