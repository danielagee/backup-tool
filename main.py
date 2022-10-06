# Day 18 of #100daysofcoding #python.
# Task 3 - Collect data from multiple user input folders.

import glob

dir_path = r'..\**\*.*'
# Ask for top node folder of primary drive
root_dir_active = input('What is the path to search?\n'
                   'Example format: c:\\MyFolder\\SearchHere\\ \n')
root_dir_active += '**'

# Ask for top node folder of backup drive
root_dir_backup = input('What is the path of your backup?\n')
root_dir_backup += '**'

for files_active in glob.glob(dir_path, root_dir=root_dir_active, recursive=True):
    print(files_active)
print('')
for files_backup in glob.glob(dir_path, root_dir=root_dir_backup, recursive=True):
    print(files_backup)