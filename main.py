# Day 18 Task 3 - Collect both directories

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

# Extracts the active and backup file lists from the user specified folders.
file_list_active = glob.glob(dir_path, root_dir=root_dir_active, recursive=True)
file_list_backup = glob.glob(dir_path, root_dir=root_dir_backup, recursive=True)

#print('These files are present in your active drive.')
#for files_active in glob.glob(dir_path, root_dir=root_dir_active, recursive=True):
#    print(files_active)

# Adds a blank line between the results to show where the list changes.
#print('')

#print('These files are present in the backup drive.')
#for files_backup in glob.glob(dir_path, root_dir=root_dir_backup, recursive=True):
#    print(files_backup)

# Creates sets from the file lists for better comparison (order does not matter).
set_active = set(file_list_active)
#sorted_list_active = sorted(set_active)
set_backup = set(file_list_backup)
#sorted_list_backup = sorted(set_backup)

# Subtracts the backup set from the active set to show what's in active and not in backup.
set_missing = set_active - set_backup
print('These files are missing from the backup:')
#print(set_missing)
# Prints a parsed list of missing files line by line rather than in a single line.
for item in set_missing:
    print(item)
print('')

# Subtracts the active set from the backup set to show what's in backup and not in active.
print('These files are in backup but missing from the active directory:')
set_extra = set_backup - set_active
#print(set_extra)
# Prints a parsed list of extra files line by line rather than in a single line.
for item in set_extra:
    print(item)
