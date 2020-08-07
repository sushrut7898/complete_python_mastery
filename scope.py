msg = "sushrut"  # Global Variables


def greet(name):
    message = "a"  # local variable in function


def send(name):  # local parameter
    message = "Sush"
    msg = "b"
    

send("a")
print(msg)

def s(name):  # local parameter
    message = "Sush"
    global msg
    msg = "b"
    

s("a")
print(msg)