#Tuple is Read Only i.e. Immutable, cannot change value once value is assigned

point = 1, 2
print(type(point))

point = ()
print(type(point))

point = (1, 2)
print(type(point))

point = (1, 2) *3
print(point)

point = (1, 2) + (2, 3)
print(point)

point = tuple([1,2])
print(point)
print(point[0:2])