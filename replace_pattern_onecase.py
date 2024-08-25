import os
import re

def replace_pattern_in_files(root_dir, old_text, new_text):
    # Compile regex pattern with case-insensitive flag
    regex = re.compile(re.escape(old_text), re.IGNORECASE)

    def replacement_function(match):
        """
        Replace the entire match with the new text while preserving the case of the original text.
        """
        original_text = match.group(0)
        # Preserve the overall case of the original text
        if original_text.isupper():
            return new_text.upper()
        elif original_text.istitle():
            return new_text.capitalize()
        elif original_text.islower():
            return new_text.lower()
        else:
            return new_text  # In case it's already mixed-case or unchanged

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

# Example usage
root_directory = '/path/to/your/directory'  # Specify the root directory
old_string = 'Old_Text'  # The text pattern to replace
new_string = 'new_text'  # The text to replace with
replace_pattern_in_files(root_directory, old_string, new_string)
