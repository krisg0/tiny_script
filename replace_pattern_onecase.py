#!/usr/bin/env python3
import os
import re
import argparse

def replace_pattern_in_files(root_dir, old_text, new_text):
    # Compile regex pattern with case-insensitive flag
    regex = re.compile(re.escape(old_text), re.IGNORECASE) #WARNING: re.escape will help you escape all special character in old_text; if this is not wanted, need to remove this call!

    def replacement_function(match):
        """
        Replace the matched text with the new text while preserving the case of the original text.
        """
        original_text = match.group(0)
        if original_text.isupper():
            return new_text.upper()
        elif original_text.istitle():
            return new_text.capitalize()
        elif original_text.islower():
            return new_text.lower()
        else:
            return new_text

    # Traverse directories and process files
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            temp_file_path = file_path + '.tmp'
            
            with open(file_path, 'r') as read_file, open(temp_file_path, 'w') as write_file:
                for line in read_file:
                    # Apply replacement line by line to handle large files efficiently
                    new_line = regex.sub(replacement_function, line)
                    write_file.write(new_line)
            
            # Replace the original file with the temporary file
            os.replace(temp_file_path, file_path)
            print(f'Processed file: {file_path}')

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Replace text pattern in files within a directory recursively.")
    
    # Define the arguments
    parser.add_argument('directory', type=str, help="The root directory where the replacement should be applied.")
    parser.add_argument('old_text', type=str, help="The text pattern to replace.")
    parser.add_argument('new_text', type=str, help="The new text that will replace the old text.")
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with the parsed arguments
    replace_pattern_in_files(args.directory, args.old_text, args.new_text)
