try:
    file = open("first.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a vaild age")
# except ZeroDivisionError:
#    print("Age cannot be 0.")
else:
    print("No exceptions!!")
finally:
    file.close()
