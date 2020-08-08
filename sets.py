numbers = [1, 1, 2, 3, 4, 5]
uniques = set(numbers)
print(uniques)
first ={1,23,3454,46,5,765,7}
second = {1, 4, 65, 43}

#sets are unordered, sets dont support indexing

print(second | first)  #UNION
print(second & first)  #Intersection
print(second - first)  #difference
print(second ^ first)  #symmetric difference - first or second but not both



