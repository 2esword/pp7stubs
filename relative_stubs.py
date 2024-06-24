#
#   The purpose of this python script is to 
#   fix pp7stubs module importation
#
#   This script search for a directory named
#   stubs, read all .py and .pyi files and  
#   rewrite them with the changes in import
#   to another directory named mod_stubs
#

import os
import re

def find_py_files(directory):
    file_paths = []
    for arquivo in os.listdir(directory):
        if (arquivo.endswith('.py') or arquivo.endswith('.pyi')) and (not '__init__' in arquivo):
            file_paths.append(os.path.join(directory, arquivo))
    return file_paths

def find_name_from_path(file_path_list):
    file_name_list = []
    for file_path in file_path_list:
        if file_path.endswith('.py'):
            file_name_list.append(file_path.split('\\')[-1].rstrip('.py'))
    return file_name_list

def create_dir(dir_path):
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        return
    except Exception as e:
        print(e)
    else:
        return

def open_read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def change_pattern(file_names, line, extension):
    """
    Modify the import statement in the given line based on the specified extension.

    Args:
        file_names (list): List of file names to check against.
        line (str): The line of code to be modified.
        extension (str): The file extension ('py' or 'pyi').

    Returns:
        str: The modified line or the original line if no changes are made.
    """
    prefix = "from . "
    patterns = {
        'py': r'import (\w+)_pb2 as \1__pb2',
        'pyi': r'(?<!\s)import (\w+)_pb2 as _\1_pb2'
    }

    if extension not in patterns: return None

    match = re.search(patterns[extension], line)
    if match:
        name = match.group(1)
        if (name + '_pb2') in file_names:
            new_pattern = f"import {name}_pb2 as "
            if extension == 'py':
                new_line = re.sub(f"{new_pattern}{name}__pb2", f"{prefix}{new_pattern}{name}__pb2", line)
            else:
                new_line = re.sub(f"{new_pattern}_{name}_pb2", f"{prefix}{new_pattern}_{name}_pb2", line)
            return new_line
        else:
            return line
    else:
        return line

diretorio = os.path.dirname(os.path.abspath(__file__))
diretorio_stubs = os.path.join(diretorio, 'stubs')

file_paths = find_py_files(diretorio_stubs)
file_names = find_name_from_path(file_paths)

novo_dir = os.path.join(diretorio, 'mod_stubs')
create_dir(novo_dir)

for file in file_paths:
    file_name = file.split('\\')[-1]
    new_file = os.path.join(novo_dir, file_name)
    extension = file_name.split('.')[1]

    text = open_read_file(file)
    
    with open(new_file, 'w', encoding='utf-8') as nf:
        print(new_file)
        for line in text:
            nf.write(change_pattern(file_names, line, extension))