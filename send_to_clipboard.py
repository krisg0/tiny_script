import subprocess
import time
import argparse
#Interactive mode: This will process the file in chunks, and after each chunk, it will wait for you to press Enter before proceeding.
#python3 send_to_clipboard.py example.txt --interactive --chunk_size 3
#Non-Interactive mode: This will process the file in chunks and wait for a specified delay between each chunk.
#python3 send_to_clipboard.py example.txt --delay 2 --chunk_size 3

def send_to_clipboard(text):
    """Send text to the clipboard using xclip."""
    try:
        process = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
        process.communicate(input=text.encode('utf-8'))  # Send the text to clipboard
    except Exception as e:
        print(f"Error sending text to clipboard: {e}")

def wait_for_enter():
    """Wait for the user to press Enter to continue."""
    input("Press Enter to continue to the next chunk...")

def print_and_send_chunks_to_clipboard(file_path, delay, start_marker=0, chunk_size=3, interactive=False):
    """Print and send a specified number of lines at a time from the file to the clipboard, prepending a marker."""
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()  # Read all lines from the file
            total_lines = len(lines)
            marker = start_marker

            # Process the lines in chunks
            for i in range(0, total_lines, chunk_size):
                # Get the next chunk of 'chunk_size' lines
                chunk = ''.join(lines[i:i+chunk_size])

                # Add marker as the first line
                chunk_with_marker = f"{marker}\n{chunk}"
                
                # Print the chunk with the marker
                print(f"Marker: {marker}")
                print(chunk_with_marker)
                
                # Send the chunk to clipboard (you can replace this with your own clipboard function)
                send_to_clipboard(chunk_with_marker)
                
                # Increment the marker for the next chunk
                marker += 1
                
                if interactive:
                    # Wait for the user to press Enter to continue to the next chunk
                    wait_for_enter()
                else:
                    # Wait for the specified delay
                    time.sleep(delay)

    except Exception as e:
        print(f"Error processing the file: {e}")

# Main function to run the code
if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Send file content to clipboard in chunks with markers.")
    parser.add_argument("file_path", help="Path to the file to send to clipboard.")
    parser.add_argument("--delay", type=float, default=1, help="Delay (in seconds) between sending chunks.")
    parser.add_argument("--start_marker", type=int, default=0, help="The starting marker value.")
    parser.add_argument("--chunk_size", type=int, default=3, help="The number of lines to send per chunk.")
    parser.add_argument("--interactive", action="store_true", help="Run interactively, waiting for Enter before each chunk.")

    # Parse arguments
    args = parser.parse_args()
    
    # Call the function with the arguments
    print_and_send_chunks_to_clipboard(args.file_path, args.delay, args.start_marker, args.chunk_size, args.interactive)
