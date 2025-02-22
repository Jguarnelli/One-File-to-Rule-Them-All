import os
import json
from datetime import datetime
import argparse

def collect_python_code(base_path: str, verbose: bool) -> dict:
    """
    Recursively scans the 'base_path' directory for Python files (.py).
    For each file found, reads its content and stores it in a dictionary
    with the relative path as the key and the file's content as the value.

    :param base_path: The root directory to start scanning from.
    :param verbose: If True, prints the relative path of each file being processed.
    :return: A dictionary mapping file paths (relative to 'base_path') to their contents.
    """
    aggregated = {}
    # Walk through the directory tree starting from base_path
    for root, dirs, files in os.walk(base_path):
        # Exclude directories we don't want to process
        dirs[:] = [d for d in dirs if d not in ['.git', '.venv', 'venv', 'node_modules', '__pycache__']]
        
        # Iterate over all files in the current directory
        for f in files:
            # Only process Python files
            if f.endswith('.py'):
                file_path = os.path.join(root, f)               # Absolute path to the file
                rel_path = os.path.relpath(file_path, base_path)  # Relative path from base_path
                if verbose:
                    print(f"Reading: {rel_path}")
                try:
                    # Read the file's contents (UTF-8 encoded)
                    with open(file_path, 'r', encoding='utf-8') as source:
                        content = source.read()
                except Exception as e:
                    # If an error occurs while reading, store the error message
                    content = f"Error reading file: {e}"
                
                # Add the file content to our aggregated dictionary
                aggregated[rel_path] = content

    return aggregated

def main():
    """
    Main entry point of the script.
    Parses command-line arguments, collects Python files, and exports them as JSON.
    """
    # Set up argument parser and define optional arguments
    parser = argparse.ArgumentParser(description="Aggregate Python files.")
    parser.add_argument("--output", "-o", help="Output filename.")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging.")
    args = parser.parse_args()

    # Generate a timestamped default output filename if none is provided
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_json = args.output if args.output else f"aggregated_output_{timestamp}.json"

    # Use the current directory as the base path (modify if needed)
    base_path = os.path.abspath('.')

    # Collect code from all .py files under base_path
    python_files_content = collect_python_code(base_path, args.verbose)

    # Write the aggregated code data to a JSON file
    with open(output_json, 'w', encoding='utf-8') as outfile:
        json.dump(python_files_content, outfile, indent=2, ensure_ascii=False)

    # Print a confirmation message
    print(f"Aggregated Python code written to: {output_json}")

if __name__ == '__main__':
    main()
