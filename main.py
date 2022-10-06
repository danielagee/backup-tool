#Day 14 Task 3
import glob

dir_path = r'c:\python\MyFolder\**\*.*'

for files in glob.glob(dir_path, recursive=True):
    print(files)