from pathlib import Path
from time import ctime
import shutil

path = Path("ecommerce/__init__.py")
#path.exists()  
#path.rename("init.txt")
#path.unlink()  #deletes the file
print(path.stat())  #returns file info
print(ctime(path.stat().st_ctime))

print(path.read_bytes())   #returns file data as bytes object
print(path.read_text())  #returns file data as string

file = open("sales.py", "r")
file.close()

#use with statement no need to manually close the file

#with open("sales.py", "r") as file
# ...
path.write_text("...")
#path.write_bytes() #All these methods take care of opening and closing the file in python
source = Path("ecommerce/__init__.py")
target = Path() / "__init__.py"

target.write_text(source.read_text())  #tedious , use shutil
shutil.copy(source, target) #cleaner way

