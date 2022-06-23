import os
dir_path = os.getcwd()

if not os.path.exists(dir_path):
    print(f'The path: {dir_path} does not exist')
    exit(1)
if not os.path.isdir(dir_path):
    print(f'{dir_path} is not a directory')
    exit(1)

def count_lines(file_path):
    '''counts the number of non empty lines in one file'''
    lines = 0
        
    with open(file_path,'r') as python_file:
        for line in python_file:
            if line.strip(): 
                lines += 1
    return lines

def count_py_lines(path):
    '''goes through all the files in a directory and its sub directories. Detcts python files and uses "count lines" on them.'''
    directory_content = os.scandir(path)
    total_lines = 0
    for content in directory_content:
        try:
            if content.name.startswith('.'):
                continue
            elif content.is_dir():
                total_lines += count_py_lines(content.path)
            elif content.name.endswith('.py'):
                total_lines += count_lines(content.path)

        except FileNotFoundError as error:
            
            print(f'The file you are trying to read does not exist: {error.filename}')

        except PermissionError as error:
            print(f'You lack permission to read {error.filename}, no lines counted')

    return total_lines

print(f'Total number of python lines is: {count_py_lines(dir_path)}')
