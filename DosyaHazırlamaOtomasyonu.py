# File Management Automation
import os
import shutil

# Create a file
def create_file(file_name, content):
    # Creates a file with the given content
    with open(file_name, "w") as file:
        file.write(content)
    print(f"{file_name} has been created.")

create_file("test.txt", "This is a test text file.")

# Copy file to another folder
def copy_file(file_name, target_folder):
    # Copies a file to the specified folder
    shutil.copy(file_name, target_folder)
    print(f"{file_name} has been copied to {target_folder}.")

copy_file(
    "test.txt",
    "C:\\Users\\ruzga\\OneDrive\\Desktop\\Python_Automation"
)

# Error handling
try:
    copy_file(
        "test.txt",
        "C:\\Users\\ruzga\\OneDrive\\Desktop\\Python_Automation"
    )
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Operation attempted (completed or failed).")

# Create folder if it doesn't exist and copy file
def create_folder_and_copy(target_folder, file_name):
    # Creates the folder if it doesn't exist and copies the file into it
    os.makedirs(target_folder, exist_ok=True)
    shutil.copy(file_name, target_folder)
    print(f"{file_name} has been copied to {target_folder}.")

# Example usage
create_folder_and_copy(
    "C:\\Users\\ruzga\\OneDrive\\Desktop\\Python_Automation",
    "test.txt"
)
