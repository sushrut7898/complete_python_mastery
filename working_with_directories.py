from pathlib import Path

path = Path("ecommerce")

#path.exists()   #returns boolean
#path.mkdir()  #creates new directory
#path.rmdir()  #Removes direcotry, but have to make directory empty first
#path.rename("String")

for p in path.iterdir():
    print(p)

#you can use list comprehension
print([p for p in path.iterdir()])
print([p for p in path.iterdir() if p.is_dir()])
# for patterns and use recursively use glob ||| iterdir cannot be used
print([p for p in path.glob("*.py")])   #gets files in that particular directory
print([p for p in path.glob("**/*.py")])    #recursive glob using glob
print([p for p in path.rglob("*.py")])  #recursive implementatin , that directory + all sub directories