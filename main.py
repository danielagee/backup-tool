#Day 18 Task 3 - Collect both directories

import glob

# Sets the search directory path to all subdirectories and file types within the root.
dir_path = r'..\**\*.*'

# Ask for top node folder, a.k.a. the root directory to search.
root_dir_active = input('What is the path to search?\n'
                   'Example format: c:\\MyFolder\\SearchHere\\ \n')
# Adds '**' to the user specified root directory so that Python will only search the root and subdirectories.
root_dir_active += '**'

# Ask for top node folder of backup folder
root_dir_backup = input('What is the path of your backup?\n')
root_dir_backup += '**'

file_list_active = glob.glob(dir_path, root_dir=root_dir_active, recursive=True)

file_list_backup = glob.glob(dir_path, root_dir=root_dir_backup, recursive=True)

print('These files are present in your active drive.')
for files_active in glob.glob(dir_path, root_dir=root_dir_active, recursive=True):
    print(files_active)

# Adds a blank line between the results so we can see where the list changes.
print('')

print('These files are present in the backup drive.')
for files_backup in glob.glob(dir_path, root_dir=root_dir_backup, recursive=True):
    print(files_backup)