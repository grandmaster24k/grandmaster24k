'''Write a python program to print the contents of a directory using the os module.
 Search online for the function which does that'''

#  by using chatgpt

import os

def list_directory_contents(path='D:\python learning'):
    try:
        # Get the list of all files and directories in the specified path
        
        contents = os.listdir(path)
        print(f"Contents of the directory '{path}':")
        
        for item in contents:
            print(item)
    
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_directory_path' with the directory path you want to check
directory_path = input("Enter the directory path (leave empty for current directory): ")
if directory_path.strip() == "":
    directory_path = '.'

list_directory_contents(directory_path)
