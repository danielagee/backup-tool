# Day 23

import glob

# Sets the search directory path to all subdirectories and file types within the root.
dir_path = r'..\**\*.*'

# Ask for top node folder, a.k.a. the root directory to search.
root_dir_active = input('What is the path to search?\n'
                        'Example format: c:\\MyFolder\\SearchHere\\ \n')

# Stores the name of the directory to write the final output files.
write_dir = root_dir_active

# Adds '**' to the user specified root directory so that Python will only search the root and subdirectories.
root_dir_active += '**'

# Ask for top node folder of backup folder
root_dir_backup = input('What is the path of your backup?\n')
root_dir_backup += '**'

# Extracts the active and backup file lists from the user specified folders.
print('Extracting files from ' + root_dir_active)
file_list_active = glob.glob(dir_path, root_dir=root_dir_active, recursive=True)
print('Extracting files from ' + root_dir_backup)
file_list_backup = glob.glob(dir_path, root_dir=root_dir_backup, recursive=True)

# Creates sets from the file lists for better comparison (order does not matter).
# print('Lists extracted. Creating Sets...')
set_active = set(file_list_active)
set_backup = set(file_list_backup)

# Subtracts the backup set from the active set to show what's in the active and not in the backup, then sorts the result.
print('Sets created. Sorting sets...')
set_missing = sorted(set_active - set_backup)

# Create a file to accept the missing backup list.
print('Sets sorted. Creating missing backup list...')
missing_backup = open(write_dir+'files_missing_in_backup.txt', 'w')

# For loop to write a parsed list of all missing backup files to the text document.
print('Missing backup list created. Writing missing backup file...')
for item in set_missing:
    missing_backup.write(str(item))
    missing_backup.write('\n')

# Closes the text file holding the missing backup files.
missing_backup.close()

# Same process as above, but subtracts the active set from the backup set to show what's in backup and not in active.
print('Missing backup list written. Creating extra files list...')
set_extra = sorted(set_backup - set_active)
missing_active = open(write_dir+'extra_files_in_backup.txt', 'w')
for item in set_extra:
    missing_active.write(str(item))
    missing_active.write('\n')
missing_active.close()