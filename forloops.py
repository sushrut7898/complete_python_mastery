for number in range(3):
    print("Sushrut Patil", number, (number + 2) * ".")

successful = False

for number in range(1, 4):
    print("Sushrut Patil", number, (number + 2) * ".")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and Failed")

for number in range(1, 10, 3):
    print("Sushrut Patil", number, (number + 2) * ".")

# Nested Loop

for x in range(5):
    for y in range(3):
        print(f"({x} , {y})")


print(type(5))
print(type(range(5)))

# Iterable
for x in "Python":
    print(x)

for x in [1, 2, 3, 4, 5]:
    print(x)
