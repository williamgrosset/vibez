<p align="center">
  <img src="https://github.com/user-attachments/assets/c4f6e72f-10ff-4ff9-a8e9-a5ead8fdb413" alt="Demo" />
</p>

## Overview

`yaink` is a simple command-line tool that extracts file contents for use with LLMs.

## Motivation

The developer AI workflow is messy. There are _many_ tools that integrate across the different stages of development and layers of the stack. Some are more powerful, but heavyweight and expensive. For most prompts, these tools only need a limited amount of [context](https://en.wikipedia.org/wiki/Large_language_model#Prompt_engineering,_attention_mechanism,_and_context_window). `yaink` is a pragmatic solution to this problem. Simply copy the file contents you need and use whatever AI tool you prefer.

## Installation

Install with `pip`:

```sh
pip install yaink
```

Or install from source:

```sh
git clone https://github.com/williamgrosset/yaink.git
cd yaink
pip install .
```

## Usage

```sh
yaink [OPTIONS] <file|file:range|directory> [...]
```

### Options

- `[-r | --recursive]`: Recursively process directories.
- `[-i | --ignore] "item1,item2,..."`: Ignore files or directories.
- `[-o | --output] <output.md>`: Save output to a file.
- `[-s | --summary] "Your summary"`: Add a summary.

### Examples

#### Extract a single file to clipboard

```sh
yaink file.py
```

#### Extract specific lines from a file

```sh
yaink file.py:5-15
```

#### Extract multiple files and directories

```sh
yaink notes.md file.py src/
```

#### Recursively extract from a directory

```sh
yaink -r src/
```

#### Ignore files or directories

```sh
yaink -r src/ -i ".git,.gitignore"
```

#### Save output to a file

```sh
yaink -o output.md file.py
```

#### Add a summary

```sh
yaink -s "Add login functionality" auth.py
```

### Output Format

````md
<summary>

<file-1> (line range):

```
<content>
```

<file-2> (line range):

```
<content>
```

...

<file-n> (line range):

```
<content>
```
````

## License

MIT
