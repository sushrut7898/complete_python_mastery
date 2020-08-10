class Animal:
    def eat(self):
        print("Eat")

class Bird(Animal):
    def fly(self):
        print("Fly")

class Chicken(Bird):
    pass  #Disadvantage of using Inheritance chicken being a bird dosent fly , inheritance also increases complexity
