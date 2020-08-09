try:
    with open("first.py") as file:
        print("File Opened.")

    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a vaild age")
# except ZeroDivisionError:
#    print("Age cannot be 0.")
else:
    print("No exceptions!!")

# with auto deletes external resources will close file , no need of finally
