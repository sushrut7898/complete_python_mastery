class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):
    pass


m = Manager()
m.greet()  # returns employee greet as its first in inheritance

# its bad to use multiple inheritance when classes have common methods

# Good example of Multiple Inheritance


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass
