class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eat")

# Animal: Parent, Base
# Mammal: Child, Sub


class Mammal(Animal):
    def walk(self):
        print("Walk")


class Fish(Animal):
    def swim(self):
        print("swim")

# every class in Python is derived from object


m = Mammal()
m.eat()
print(m.age)
print(isinstance(m, Mammal))
print(isinstance(m, object))

o = object()
print(issubclass(Mammal, Animal))

print(issubclass(Mammal, object))
