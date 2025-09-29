# File Management Automation

**Description:** Simple and easy-to-use Python file automation script

---

## Overview
This Python script automates basic file management tasks.  
It can:
- Create a text file with custom content
- Copy files to another folder
- Create target folders if they don't exist
- Handle common errors like file not found or permission denied

---

## How to Use
1. Download the repository or clone it.
2. Open the Python script (`main.py`).
3. Modify the file name, content, and target folder as needed.
4. Run the script:
```bash
python main.py
# Create a file
create_file("test.txt", "This is a test text file.")

# Copy file to a folder (creates the folder if it doesn't exist)
create_folder_and_copy("C:\\Users\\YourUser\\Desktop\\Python_Automation", "test.txt")

Features

Simple and easy to understand

Works on Windows

Includes error handling for common file operations

Modular functions for reuse in other projects
