# Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats. For example:

# sfdsf.png --> 1.png
# vfsf.png --> 2.png
# this.png --> 3.png
# design.png --> 4.png
# name.png --> 5.png

import os 

folders = os.listdir("images")

def rename(formate):
  i=1
  for file in folders:
    file_name, file_extension = os.path.splitext(file)
    if file_extension == f".{formate}":
      os.rename(f"images/{file_name}.{formate}", f"images/{i}.{formate}")
    i += 1
    
rename("txt")