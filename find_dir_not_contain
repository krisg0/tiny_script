#!/usr/bin/env python3
import os

def find_folders_without_files(base_path, excluded_files):
    """
    Find folders that do not contain any of the specified files.

    Args:
        base_path (str): The base directory to start the search.
        excluded_files (list): List of filenames to check against.

    Returns:
        list: Folders that do not contain any of the specified files.
    """
    matching_roots = set()  # Use a set to avoid duplicates

    for root, dirs, files in os.walk(base_path):
        #any is higher-order functions working on iterables
        if not any(file in files for file in excluded_files):  # If a match is found
            matching_roots.add(root)  # Add to the set

    return list(matching_roots)  # Convert to list if needed

# Example Usage
base_path = "/some/path"
excluded_files = ["file1.txt", "file2.log"]
folders_without_excluded_files = find_folders_without_files(base_path, excluded_files)

print("Folders that do not contain the excluded files:")
for folder in folders_without_excluded_files:
    print(folder)
