import os
import shutil
from_dir = "C:/Users/vishal/Desktop/New folder"
to = "C:/Users/vishal/Desktop/python"
list= os.listdir(from_dir)
for flie in list:
    name,ext=os.path.splitext(file)
    print(name)