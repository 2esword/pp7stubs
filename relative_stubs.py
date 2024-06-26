#
#   This Python script fixes module imports
#   imports in generated stubs from .proto 
#   to use relative relative imports.
#
#   Here's how it works: it searches for a 
#   directory names "stubs", read all .py and
#   .pyi files, and rewrites them with import
#   changes to another directory named "pp7stubs"
#

import os
import re



def find_files(directory: str) -> list:
    file_paths = []
    try:
        for file in os.listdir(directory):
            if (file.endswith('.py') or file.endswith('.pyi')) and (not '__init__' in file):
                file_paths.append(os.path.join(directory, file))
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{directory}'.")
    return file_paths

def file_name_from_path(file_path: str) -> str:
    base_name = os.path.basename(file_path)

    if '.' in base_name: return base_name.split('.')[0]
    else: return base_name

def list_file_names(paths :list) -> set:
    names = set()
    for file_path in paths:
        name = file_name_from_path(file_path)
        names.add(name)
    return names

def create_dir(dir_path):
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        return
    except Exception as e:
        print(e)
    else:
        return

def open_read_file(file_path) -> list:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines =  file.readlines()
        return lines
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def change_pattern(file_names: set, line: str, extension: str):
    """
    Modify the import statement in the given line based on the specified extension.

    Args:
        file_names (set): List of file names to check against.
        line (str): The line of code to be modified.
        extension (str): The file extension ('py' or 'pyi').

    Returns:
        str: The modified line or the original line if no changes are made.
    """
    prefix = "from . "
    patterns = {
        '.py': r'import (\w+)_pb2 as \1__pb2',
        '.pyi': r'(?<!\s)import (\w+)_pb2 as _\1_pb2'
    }

    if extension not in patterns: return None

    match = re.search(patterns[extension], line)
    if match:
        name = match.group(1)
        if (name + '_pb2') in file_names:
            new_pattern = f"import {name}_pb2 as "
            if extension == '.py':
                new_line = re.sub(f"{new_pattern}{name}__pb2", f"{prefix}{new_pattern}{name}__pb2", line)
            else:
                new_line = re.sub(f"{new_pattern}_{name}_pb2", f"{prefix}{new_pattern}_{name}_pb2", line)
            return new_line
        else:
            return line
    else:
        return line


def main():
    main_dir = os.path.dirname(os.path.abspath("__file__"))
    stubs_dir = os.path.join(main_dir, 'stubs')

    file_paths : list = find_files(stubs_dir)
    file_names : set = list_file_names(file_paths)

    pp7_dir = os.path.join(main_dir, 'pp7stubs')
    create_dir(pp7_dir)

    for file in file_paths:
        name = os.path.basename(file)
        new_file = os.path.join(pp7_dir, name)
        extension = os.path.splitext(file)[1]

        text = open_read_file(file)

        with open (new_file, 'w', encoding='utf-8') as nf:
            for line in text:
                nf.write(change_pattern(file_names, line, extension))

if __name__ == "__main__":
    main()