#use only when dealing with large number of items
from array import array

numbers = array("i", [1, 2, 3])
print(numbers)
numbers.append(4)
print(numbers)
numbers.pop(1)
print(numbers)