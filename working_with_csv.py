import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction", "product_id", "price"])
    writer.writerow([1000, 7, 1])
    writer.writerow([2, 9, 8])

with open("data.csv") as file:
    reader = csv.reader(file)
    #print(list(reader))    #reader cannot be iterated twice
    for row in reader:
        print(row)