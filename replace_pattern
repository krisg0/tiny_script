import os
import re

def replace_pattern_in_files(root_dir, old_text, new_text):
    # Compile regex pattern with case-insensitive flag
    regex = re.compile(re.escape(old_text), re.IGNORECASE)

    def replacement_function(match):
        """
        Create a replacement string where each character's case matches the corresponding character's case 
        in the original text.
        """
        original_text = match.group(0)
        replacement = new_text
        result = []
        for o, r in zip(original_text, replacement):
            # Preserve the case of each character from the original text
            if o.isupper():
                result.append(r.upper())
            elif o.islower():
                result.append(r.lower())
            else:
                result.append(r)
        return ''.join(result)
    
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
old_string = 'Old_Text'  # The text pattern to replace, with mixed case
new_string = 'new_text'  # The text to replace with
replace_pattern_in_files(root_directory, old_string, new_string)
