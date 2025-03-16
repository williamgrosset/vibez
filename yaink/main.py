#!/usr/bin/env python3
import sys
import os

try:
    import pyperclip
    PYPERCLIP_AVAILABLE = True
except ImportError:
    PYPERCLIP_AVAILABLE = False

def main():
    """
    Usage:
      yaink [-r] [--md <OUTPUT.md>] [--summary "your summary"] <file or directory or file:range> [<file or directory or file:range> ...]
    
    Examples:
      1) Copy to clipboard (default):
         yaink file1.js file2.go:1-50 file3.rs:10-20

      2) Write to a markdown file (--md):
         yaink --md output.md file1.js file2.go:1-50

      3) Recursively process all files in a directory:
         yaink -r directory

      4) Add a summary:
         yaink --summary "This is a summary" file1.js file2.go
    """

    if len(sys.argv) < 2:
        print("Usage: yaink [-r] [--md <OUTPUT.md>] [--summary \"your summary\"] <file or directory or file:range> ...")
        sys.exit(1)

    args = sys.argv[1:]
    output_file = None
    recursive = False
    summary = None
    file_specs = []

    # Recursive flag
    if '-r' in args:
        recursive = True
        args.remove('-r')

    # Output file flag
    if '--md' in args:
        md_index = args.index('--md')
        if md_index + 1 >= len(args):
            print("Error: You used '--md' but did not specify an output file.")
            sys.exit(1)
        output_file = args[md_index + 1]
        del args[md_index:md_index + 2]

    # Summary flag
    if '--summary' in args:
        summary_index = args.index('--summary')
        if summary_index + 1 >= len(args):
            print("Error: You used '--summary' but did not provide a summary.")
            sys.exit(1)
        summary = args[summary_index + 1]
        del args[summary_index:summary_index + 2]

    # File specs
    file_specs = args

    if not file_specs:
        print("Error: No files or directories specified.")
        sys.exit(1)

    if output_file is None and not PYPERCLIP_AVAILABLE:
        print("Error: pyperclip is not installed for clipboard copying. Install via 'pip install pyperclip',")
        print("or use the '--md <OUTPUT.md>' option to write to a file instead.")
        sys.exit(1)

    content = []

    def add_snippet_block(header, code):
        content.append(f"{header}:\n```\n{code}\n```\n")

    def process_file(filepath, line_range=None):
        if not os.path.isfile(filepath):
            print(f"Skipping: file '{filepath}' not found.")
            return

        with open(filepath, 'r', encoding='utf-8') as f_in:
            content_lines = f_in.readlines()

        if line_range:
            start_line, end_line = line_range
            file_length = len(content_lines)
            start_line = max(1, start_line)
            end_line = min(file_length, end_line)
            excerpt = content_lines[start_line - 1:end_line]
            excerpt_str = "".join(excerpt)
            add_snippet_block(f"{filepath} (lines {start_line}-{end_line})", excerpt_str)
        else:
            file_content = "".join(content_lines)
            add_snippet_block(filepath, file_content)

    def process_directory(directory):
        for root, _, files in os.walk(directory):
            for file in files:
                process_file(os.path.join(root, file))
            if not recursive:
                break

    for spec in file_specs:
        if ':' in spec:
            parts = spec.split(':', 1)
            filename = parts[0]
            line_range = parts[1]

            if '-' not in line_range:
                print(f"Skipping invalid line range format: {line_range}")
                continue

            try:
                start_line, end_line = map(int, line_range.split('-'))
            except ValueError:
                print(f"Skipping invalid numeric range: {line_range}")
                continue

            process_file(filename, (start_line, end_line))
        elif os.path.isdir(spec):
            process_directory(spec)
        else:
            process_file(spec)

    concatenated_content = "".join(content)

    if summary:
        concatenated_content = f"Summary:\n{summary}\n\n{concatenated_content}"

    if output_file is None:
        pyperclip.copy(concatenated_content)
        print("Code has been copied to the clipboard.")
    else:
        with open(output_file, 'w', encoding='utf-8') as f_out:
            f_out.write(concatenated_content)
            print(f"Created {output_file}.")

if __name__ == '__main__':
    main()