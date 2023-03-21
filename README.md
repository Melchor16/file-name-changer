# File Name Changer

This script is made to change the name of multiple files inside a folder so you don't need to do it one by one.

## Table of contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Instructions](#instructions)
- [Built with](#built-with)
- [Author](#author)


## Overview

This is a script that that chages the name of multiple files inside a folder. 
With this script you can: 
- Change part of the name.
- Add a suffix and/or a prefix.
- Completely rename the file with a consecutive number.
- Order the files by creation date and rename with a consecutive number.


## Requirements

To use this script you need to install:

- [Python](https://www.python.org/downloads/)

## Instructions

1. Run the script.
2. Write the path of the folder you'te going to work with.
3. Select an option and write the number.
4. follow the instructions.
5. select the extension of the files you want to rename.

### Replace part of the name
This feature replaces part of the name of all the files.
Example:

File names:

> FileName-P01.txt
> FileName-P02.txt
> FileName-P03.txt

    Text to replace: FileName
    Replace with: FN
    Extension of files to rename (empty for all):

New file names:

> FN-P01.txt
> FN-P02.txt
> FN-P03.txt

### Add a prefix and/or suffix

This feature adds a prefix and suffix to the names, if you want to add just a prefix or just a suffix, leave blank the other one.
Example:

File names:

> FileName01.pdf
> FileName02.pdf
> FileName03.pdf

    Write a suffix (Enter to skip): -new
    Write a prefix (Enter to skip): NM_
    Extension of files to rename (empty for all): pdf

New file names:

> NM_FileName01-new.pdf
> NM_FileName02-new.pdf
> NM_FileName03-new.pdf

### Rename all with a consecutive number

This feature completely rename all the files with a constant and a consecutive, you're going to write the constant and the number of digits of the consecutive.
Example:

File names:

> FileName01.png
> FileName02.png
> FileName03.png
> FileName04.jpg

    Write a constant: FN-
    Number of digits of the consecutive (max 5): 2
    Extension of files to rename (empty for all): png

New file names:

> FN-01.png
> FN-02.png
> FN-03.png
> FileName04.jpg

(Note: FileName04.jpg keep the original name because we selected only png files.)

### Order files by creation date and rename

This feature works exactly as the pevious one, but in this case before renaming it orders the files by creation date.

## Built with

- Python

## Author

- Website - [Erick Melchor](https://github.com/Melchor16)

