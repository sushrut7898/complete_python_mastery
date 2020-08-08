items = [('Pro1', 10), ('Pro2', 7), ('Pro3', 12)]

prices = []
for item in items:
    prices.append(item[1])

x = list(map(lambda item: item[1], items))

print(prices)
print(x)
