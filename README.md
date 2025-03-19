## Overview

`yaink` is a simple command-line tool for extracting file contents to be used with LLMs.

## Motivation

The developer AI workflow is messy. There are _many_ tools that integrate across the different stages of development and at different parts of the stack. Some tools are more powerful, but heavyweight and expensive. For most prompts, these tools don't actually need that much [context](https://en.wikipedia.org/wiki/Large_language_model#Prompt_engineering,_attention_mechanism,_and_context_window). `yaink` is designed to be a pragmatic solution to this problem. Simply copy the file contents you need and use whatever AI tool you want.

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
yaink [-r] [-md <OUTPUT.md>] [-s "your summary"] [-i "file_or_directory1,file_or_directory2"] <file or directory or file:range> [...]
```

### Options

- `[-r | --recursive]`: Recursively process directories.
- `[-md | --markdown] <OUTPUT.md>`: Save content to a markdown file.
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

#### Ignore files

```sh
yaink -r src/ -i ".git,.gitignore"
```

#### Save output to a markdown file

```sh
yaink -md snippets.md myfile.py
```

#### Provide a summary

```sh
yaink -s "Add a login button" src/
```

## License

MIT
