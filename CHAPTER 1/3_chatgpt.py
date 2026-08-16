import os
from os import path

# Specify the directory path
directory_path = "C:/Users/tausi/OneDrive/Desktop/Python/CHAPTER 1" 

try:
    # Get the list of files and folders
    contents = os.listdir(directory_path)

    print("\nContents of the directory:")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("Directory not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print("Error:", e)