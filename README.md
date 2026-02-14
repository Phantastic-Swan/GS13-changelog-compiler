# GS13 Changelog Compiler

A simple in line command tool written in Python for compiling changelogs for event/updates announcements.

# Requirements

This requires python 3.11.9, and the PyYAML package. You can install it using:

`pip install pyyaml`

# Usage

To run this program, you must have a valid changelog in the `.yml` format.

`python changelog_compiler.py [-h] [-d] [-n] [-o OUTPUT_FILE] input_file`

### Options


| Option        | Function |
| ------------- | ------------- |
| -h, --help| Displays the help message|
| -d, --date| Optional, whether the changes should be sorted by date. Defaults to false.  |
| -n, --name| Optional, whether the changes should be sorted by author. Defaults to false. |
| -o OUTPUT_FILE, --output-file OUTPUT_FILE| Optional, the name of the output file. Can be a path to a folder too. Defaults to the current directory. |
| input_file| Required, the path to the original changelog file.  |