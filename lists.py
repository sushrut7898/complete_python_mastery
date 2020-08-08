letters = ["a", "b", "c"]
list_of_list = [[0, 1], [1, 2]]
zeros = [0] * 10
print(zeros)

combined = zeros + letters
print(combined)

# can combine list of any datatype

numbers = list(range(20))
print(numbers)

char = list("Hello World")
print(char)

print(len(char))

letters = ["a", "b", "c", ]
letters[0] = "A"
print(letters[-1])
print(letters)
print(letters[:])
print(letters[0:])
print(letters[:2])
print(letters[1:2])
print(letters[::2])  # returns alternate element in list
print(letters[::-1])  # reverse the list

# lIST uNPACKING
num = [1, 2, 3]
first, second, third = num
num = [1, 2, 3, 3, 4, 5, 5, 6, 7]
first, second, *other = num
print(other)
first, *other, last = num
print(first, last)

#Looping over list using for loops, can also use enumerate which returns a tuple

letters = ['a', 'b', 'c']
for letter in letters:
    print(letter)

for letter in enumerate(letters):   #enumerate returns a Tuple
    print(letter)
    print(letter[0], letter[1])

for index, letter in enumerate(letters):
    print(index, letter)

#add
letters = ['a', 'b', 'c']
#add at end of list
letters.append("d")
print(letters)

letters.insert(0, 's')
print(letters)

#removing objects

#from end

letters.pop()
print(letters)

#any index pop
letters.pop(1)
print(letters)

#remove specific letter
letters.remove('s')
print(letters)

#remove range
del letters[1:3]
print(letters)

#remove all items
letters.clear()
print(letters)

#Finding Items
letters = ['a', 'b', 'c']
if 'a' in letters:
    print(letters.index('a'))
print(letters.count('d'))

#sorting numbers in a list
numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(numbers)

items = [
    ("Pro1", 10),
    ("Pro2", 8),
    ("Pro3", 5)
]

def sort_item(item):
    return item[1]

items.sort(key = sort_item)
print(items)

#Lambda Function

items = [
    ("Pro1", 10),
    ("Pro2", 8),
    ("Pro3", 5)
]

items.sort(key = lambda item:item[1])
print(items)

#lambda function syntax  lambda parameters : expression



