import os

def rename_files_and_directories(root_dir, old_text, new_text):
    # Walk through the directory tree from the deepest level first
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        
        # Rename files that contain the old_text
        for filename in filenames:
            if old_text in filename:
                old_file = os.path.join(dirpath, filename)
                new_file = os.path.join(dirpath, filename.replace(old_text, new_text))
                os.rename(old_file, new_file)
                print(f'Renamed file: {old_file} -> {new_file}')
        
        # Rename directories that contain the old_text
        for dirname in dirnames:
            if old_text in dirname:
                old_dir = os.path.join(dirpath, dirname)
                new_dir = os.path.join(dirpath, dirname.replace(old_text, new_text))
                os.rename(old_dir, new_dir)
                print(f'Renamed directory: {old_dir} -> {new_dir}')

# Example usage
root_directory = '/path/to/your/directory'  # Specify the root directory for renaming
old_string = 'old_text'  # Text to replace
new_string = 'new_text'  # New text to use
rename_files_and_directories(root_directory, old_string, new_string)
