#Day 16 of #100daysofcoding #python

import glob

dir_path = r'..\**\*.*'
root_dir = r'c:\Python\MyFolder\**'

for files in glob.glob(dir_path, root_dir=root_dir, recursive=True):
    print(files)