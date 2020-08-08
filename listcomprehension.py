items = [('Pro1', 10), ('Pro2', 7), ('Pro3', 12)]
prices = [item[1] for item in items]
print(prices)

items = [('Pro1', 10), ('Pro2', 7), ('Pro3', 12)]
filtered = [item for item in items if item[1] >= 10]
print(filtered)
