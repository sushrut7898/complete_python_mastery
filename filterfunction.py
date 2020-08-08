items = [('Pro1', 10), ('Pro2', 7), ('Pro3', 12)]

x = list(filter(lambda item: item[1] >= 10, items))
print(x)

