import os
import time
import subprocess
import argparse

#example usage command:
#python3 monitor_clipboard.py output.txt --start_marker 0 --end_marker 10 --sleep_time 0.01

def get_clipboard_content():
    """Fetches the content of the Windows clipboard from WSL2."""
    try:
        result = subprocess.run(
            ["powershell.exe", "-Command", "Get-Clipboard"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error fetching clipboard content: {e}")
        return None

def write_to_file(file_path, content):
    """Appends content to the specified file."""
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(content + "\n")

def main(file_path, start_marker, end_marker, sleep_time):
    print(f"Monitoring clipboard for marker starting at {start_marker}...")
    if end_marker is not None:
        print(f"Stopping after processing marker {end_marker}...")
    else:
        print("Monitoring indefinitely...")

    last_marker = None
    last_content = None
    mismatch_log_path = "mismatch_log.txt"

    while True:
        clipboard_content = get_clipboard_content()
        if clipboard_content is None:
            time.sleep(sleep_time)
            continue
        
        # Parse marker and content
        try:
            lines = clipboard_content.split("\n")
            marker = int(lines[0])  # First line is the marker
            content = "\n".join(lines[1:])  # Remaining lines are the content
        except (IndexError, ValueError):
            # Ignore invalid clipboard content
            time.sleep(sleep_time)
            continue

        # Wait until the marker starts at the specified value
        if last_marker is None and marker != start_marker:
            time.sleep(sleep_time)
            continue

        # Stop processing if the marker exceeds the end marker
        if end_marker is not None and marker > end_marker:
            mismatch_message = f"Exceeded end marker: Expected <= {end_marker}, got {marker}. Exiting."
            print(mismatch_message)
            write_to_file(mismatch_log_path, mismatch_message)
            break

        # Only act if clipboard content has changed
        if clipboard_content != last_content:
            # Detect mismatched markers
            if last_marker is not None and marker != last_marker + 1:
                mismatch_message = f"Mismatch detected: Expected {last_marker + 1}, got {marker}"
                print(mismatch_message)
                write_to_file(mismatch_log_path, mismatch_message)

            # Print the current marker to the terminal
            print(f"Marker: {marker}")

            # Write the clipboard content (excluding marker line) to the file
            write_to_file(file_path, content)

            # Update the last_marker and last_content
            last_marker = marker
            last_content = clipboard_content

            # Stop if the end marker has been reached
            if end_marker is not None and marker == end_marker:
                print(f"Processed end marker: {marker}. Exiting.")
                break

        time.sleep(sleep_time)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor Windows clipboard for changes.")
    parser.add_argument("file_path", help="Path to the output file.")
    parser.add_argument("--start_marker", type=int, default=0, help="Marker value to start processing from.")
    parser.add_argument("--end_marker", type=int, help="Marker value to stop processing at (inclusive).")
    parser.add_argument("--sleep_time", type=float, default=0.1, help="Time (in seconds) to wait between checks.")
    args = parser.parse_args()
    main(args.file_path, args.start_marker, args.end_marker, args.sleep_time)
