# Day 17 of #100daysofcoding #python.
# Task 3 - Ask for user input on search location

import glob

dir_path = r'..\**\*.*'
# Ask for top node folder
root_dir = input('What is the path to search?\n'
                   'Example format: c:\\MyFolder\\SearchHere\\ \n')
root_dir += '**'

for files in glob.glob(dir_path, root_dir=root_dir, recursive=True):
    print(files)