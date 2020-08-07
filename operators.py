temperature = 35
if temperature > 30:
    print("It's warm")
    print("Drink Water")
elif temperature > 20:
    print("It's Nice")
else:
    print("It's Cold")
print("Done")

age = 22
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# cleaner code

message = "Eligible" if age >= 20 else "Not Eligible"
print(message)

# logical operators
# and or not

high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")

if high_income or good_credit:
    print("Eligible")
else:
    print("Not Eligible")

student = True

if not student:
    print("Eligible")
else:
    print("Not Eligible")

# Logical Operators are Short Circuiting

#chaining comparison operators
age = 22
if age >= 18 and age < 65:
    print("Eligible")

# example of chaining comparison operators
if 18 <= age < 65:
    print("Eligible")

