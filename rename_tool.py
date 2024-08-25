#!/usr/bin/env python3
import os
import argparse

def rename_files_first(root_dir, old_text, new_text):
    """
    Rename files first in a directory and its subdirectories,
    then rename directories to avoid issues with path changes.
    """
    # Step 1: Rename files first
    for dirpath, _, filenames in os.walk(root_dir, topdown=False):
        for filename in filenames:
            old_file_path = os.path.join(dirpath, filename)
            new_filename = filename.replace(old_text, new_text)
            new_file_path = os.path.join(dirpath, new_filename)
            if old_file_path != new_file_path:
                os.rename(old_file_path, new_file_path)
                print(f'Renamed file: {old_file_path} -> {new_file_path}')
    
    # Step 2: Rename directories
    for dirpath, dirnames, _ in os.walk(root_dir, topdown=False):
        for dirname in dirnames:
            old_dir_path = os.path.join(dirpath, dirname)
            new_dirname = dirname.replace(old_text, new_text)
            new_dir_path = os.path.join(dirpath, new_dirname)
            if old_dir_path != new_dir_path:
                os.rename(old_dir_path, new_dir_path)
                print(f'Renamed directory: {old_dir_path} -> {new_dir_path}')

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Rename files and directories recursively.")
    
    # Define the arguments
    parser.add_argument('directory', type=str, help="The root directory where renaming should be applied.")
    parser.add_argument('old_text', type=str, help="The text to be replaced.")
    parser.add_argument('new_text', type=str, help="The new text to replace with.")
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with the parsed arguments
    rename_files_first(args.directory, args.old_text, args.new_text)
