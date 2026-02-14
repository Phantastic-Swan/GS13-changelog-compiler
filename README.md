# GS13 Changelog Compiler

A simple in line command tool written in Python for compiling changelogs for event/updates announcements.

# Requirements

This requires python 3.11.9, and the PyYAML package. You can install it using:

`pip install pyyaml`

# Usage

To run this program, you must have a valid changelog in the `.yml` format.

### Running from the command line

`python changelog_compiler.py [-h] [-d] [-n] [-o OUTPUT_FILE] input_file`

### Running with VSC

This repo comes with a `launch.json` file configured with 2 launch configurations. One allows the user to input the arguments manually, the other has a pre-defined lists of arguments, which can be changed by the user. These can be used from the "Run and Debug" panel of VSC.

### Options


| Option        | Function |
| ------------- | ------------- |
| -h, --help| Displays the help message|
| -d, --date| Optional, whether the changes should be sorted by date. Defaults to false.  |
| -n, --name| Optional, whether the changes should be sorted by author. Defaults to false. |
| -o OUTPUT_FILE, --output-file OUTPUT_FILE| Optional, the name of the output file. Can be a path to a folder too. Defaults to the current directory. |
| input_file| Required, the path to the original changelog file.  |