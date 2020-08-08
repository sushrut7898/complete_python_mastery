# key value pair

point = {"x": 1, "y": 2}

point = dict(x=1, y=2)
print(point["x"])
point["x"] = 10
point["z"] = 20
print(point)

print(point.get("f"))
print(point.get("f",0)) #0 is default value if not found
del point["x"]
print(point)
    
for key, value in point.items():
    print(key, value)