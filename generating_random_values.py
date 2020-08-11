import random
import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 54, 654, 67564, 67546, ]))
print(random.choices([1, 2, 3, 4, 5, 6], k=2))

# Generating Random Password

print("".join(random.choices("skdbaskjdhksajdhjsa", k=4)))
print(string.ascii_letters)
print("".join(random.choices(string.ascii_letters + string.digits, k=4)))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(numbers)
print(numbers)