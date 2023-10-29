import os
import py_compile

def compile_directory(path, exclude_dirs=None):
    """
    Recursively compiles Python files in a directory while excluding specified directories.

    :param path: The root directory to start searching for Python files.
    :param exclude_dirs: A list of directory names to exclude from compilation.
    """
    if exclude_dirs is None:
        exclude_dirs = []

    for dirpath, dirnames, filenames in os.walk(path, topdown=True):
        # Check if the current directory is in the excluded directories
        if any(exclude_dir in dirpath for exclude_dir in exclude_dirs):
            continue  # Skip excluded directories

        for filename in filenames:
            if filename.endswith('.py'):
                file_path = os.path.join(dirpath, filename)
                compiled_path = file_path + 'c'

                try:
                    # Compile the Python file
                    py_compile.compile(file_path, cfile=compiled_path)
                    os.remove(file_path)  # Delete the original .py file after successful compilation
                    print(f"Compiled: {file_path}")
                except Exception as e:
                    print(f"Error compiling {file_path}: {e}")
