import subprocess
import time
import argparse
import keyboard  # Import the keyboard module to detect key presses

#Interactive Mode with Specific Key: If you want to wait for the "Space" key, run the script with --wait_for_key space:
#python send_chunks_to_clipboard.py example.txt --interactive --chunk_size 3 --wait_for_key space
#Interactive Mode with Any Key: If you just want to wait for any key, use --interactive without --wait_for_key:
#python send_chunks_to_clipboard.py example.txt --interactive --chunk_size 3
#Non-Interactive Mode with Delay: To use the script with a delay and without interaction:
#python send_chunks_to_clipboard.py example.txt --delay 2 --chunk_size 3

def send_to_clipboard(text):
    """Send text to the clipboard using xclip."""
    try:
        process = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
        process.communicate(input=text.encode('utf-8'))  # Send the text to clipboard
    except Exception as e:
        print(f"Error sending text to clipboard: {e}")

def print_and_send_chunks_to_clipboard(file_path, delay, start_marker=0, chunk_size=3, interactive=False, wait_for_key=None):
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
                
                # Print the chunk with the marker (optional, for debugging)
                print(f"Marker: {marker}")
                print(chunk_with_marker)
                
                # Send the chunk to clipboard
                send_to_clipboard(chunk_with_marker)
                
                # Increment the marker for the next chunk
                marker += 1
                
                if interactive:
                    if wait_for_key:
                        print(f"Press '{wait_for_key}' to proceed to the next chunk...")
                        # Wait for the specified key press (e.g., Space, 'x', 'q', etc.)
                        keyboard.wait(wait_for_key)
                    else:
                        # Wait for any key press before proceeding
                        print("Press any key to proceed to the next chunk...")
                        keyboard.read_event()
                else:
                    # Wait for the specified delay
                    time.sleep(delay)
                
    except Exception as e:
        print(f"Error processing the file: {e}")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Send file content to clipboard in chunks with markers.")
    parser.add_argument("file_path", help="Path to the file to send to clipboard.")
    parser.add_argument("--delay", type=float, default=1, help="Delay (in seconds) between sending chunks.")
    parser.add_argument("--start_marker", type=int, default=0, help="The starting marker value.")
    parser.add_argument("--chunk_size", type=int, default=3, help="The number of lines to send per chunk.")
    parser.add_argument("--interactive", action="store_true", help="Run interactively, waiting for user input before each chunk.")
    parser.add_argument("--wait_for_key", type=str, help="Specify a key to wait for (e.g., 'space', 'q', 'x').")

    # Parse arguments
    args = parser.parse_args()
    
    # Call the function with the arguments
    print_and_send_chunks_to_clipboard(args.file_path, args.delay, args.start_marker, args.chunk_size, args.interactive, args.wait_for_key)
