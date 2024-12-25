import time
import subprocess

def get_clipboard_content():
    """Retrieve the current Windows clipboard content."""
    result = subprocess.run(
        ["powershell.exe", "-Command", "Get-Clipboard"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip().replace('\r', '')

# Measure execution time
start_time = time.time()
get_clipboard_content()
elapsed_time = time.time() - start_time
print(f"Clipboard fetch time: {elapsed_time:.5f} seconds")
