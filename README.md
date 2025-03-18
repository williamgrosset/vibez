## Overview

`yaink` is a simple command-line tool for extracting file contents to be used as input to LLMs.

## Motivation

The developer AI workflow is messy. There are _many_ different tools that integrate across the stages of development. Some tools are more powerful, but heavyweight and expensive than others. `yaink` is a pragmatic solution to this problem.

## Installation

Install with `pip`:

```sh
pip install yaink
```

Alternatively, install from source:

```sh
git clone https://github.com/williamgrosset/yaink.git
cd yaink
pip install .
```

## Usage

```sh
yaink [-r] [--md <OUTPUT.md>] [--summary "your summary"] [--ignore "file_or_directory1,file_or_directory2"] <file or directory or file:range> [...]
```

### Options

- `[-r | --recursive]`: Recursively process directories.
- `[-md | --markdown] <OUTPUT.md>`: Save content to the specified markdown file.
- `[-s | --summary] "your summary"`: Add a summary at the beginning of the output.
- `[-i | --ignore] "file_or_directory1,file_or_directory2"`: Ignore specific files or directories.

### Examples

#### Extract from a single file
```sh
yaink myfile.py
```

#### Extract a line range from a file
```sh
yaink myfile.py:5-15
```

#### Extract from multiple files and directories
```sh
yaink src/ myfile.py otherfile.py
```

#### Extract recursively from a directory
```sh
yaink -r src/
```

#### Save output to a markdown file
```sh
yaink -md snippets.md myfile.py
```

#### Provide a summary
```sh
yaink -s "Important snippets" src/
```

## License

MIT