# super() function used to get access to base class

class Animal:
    def __init__(self):
        self.age = 1
        print("Animal Constructor")

    def eat(self):
        print("Eat")

# Animal: Parent, Base
# Mammal: Child, Sub


class Mammal(Animal):
    def __init__(self):
        self.weight = 1
        super().__init__()
        print("Mammal Constructor")

    def walk(self):
        print("Walk")


m = Mammal()
print(m.weight)
# print(m.age)   no attribute age for mammal - method overriding