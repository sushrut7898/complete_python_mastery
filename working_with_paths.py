from pathlib import Path

# r Raw Path - use single backslash, double backslash not required
Path(r"C:\Program Files\Microsoft")

# Path()
path = Path("ecommerce/__init__.py")
# Path() / Path("ecommerce")  # Combining Path Obhects using /
#Path() / "ecommerce" / "__init__.py"
# getting current directory
# Path.home()

path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)    #returns filename without extension
print(path.suffix)  #returns extension
print(path.parent)  #returns parent
pat = path.with_name("file.txt")    # create path object based on this path
print(pat)
print(pat.absolute())  #Absolute value of the path
pa = path.with_suffix(".txt")  #used to change file extension

print(pa)
