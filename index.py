import json
import os
import subprocess
import zipfile

def get_options():
    # Replace 'your_file.json' with the actual path to your JSON file
    file_path = '/app/options.json'

    try:
        # Step 1: Opening the JSON file in read mode
        with open(file_path, 'r') as file:
            
            # Step 2: Loading the JSON content into a Python dictionary
            json_object = json.load(file)
            
            # Step 3: Printing the JSON object (Python dictionary)
            print(json_object)
            return json_object
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error occurred while parsing the JSON data in file '{file_path}'.")
    except IOError:
        print(f"Error occurred while reading the file '{file_path}'.")

def zip_folder(folder_path):
    with zipfile.ZipFile(folder_path + ".zip", 'w', zipfile.ZIP_STORED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))

def are_there_sub_folders(parent_folder_path: str):
    # Check if the parent folder exists
    if os.path.exists(parent_folder_path):
        # Get a list of all files and subfolders in the parent folder
        items_in_parent_folder = os.listdir(parent_folder_path)
        
        # Variable to keep track if any subfolders are found
        subfolders_found = False
        
        # Iterate through the items in the parent folder
        for item in items_in_parent_folder:
            item_path = os.path.join(parent_folder_path, item)
            
            # Check if the item is a directory (subfolder)
            if os.path.isdir(item_path):
                subfolders_found = True
                print(f"Subfolder found: {item}")
        
        # Check if any subfolders were found
    
        print("There are subfolders inside the parent folder: ", subfolders_found)
        return subfolders_found
    else:
        raise Exception("No parent folder")

def are_there_sub_folders(parent_folder_path: str):
    # Check if the parent folder exists
    if os.path.exists(parent_folder_path):
        # Get a list of all files and subfolders in the parent folder
        items_in_parent_folder = os.listdir(parent_folder_path)
        
        # Variable to keep track if any subfolders are found
        subfolders_found = False
        
        # Iterate through the items in the parent folder
        for item in items_in_parent_folder:
            item_path = os.path.join(parent_folder_path, item)
            
            # Check if the item is a directory (subfolder)
            if os.path.isdir(item_path):
                subfolders_found = True
                print(f"Subfolder found: {item}")
        
        # Check if any subfolders were found
    
        print("There are subfolders inside the parent folder: ", subfolders_found)
        return subfolders_found
    else:
        raise Exception("No parent folder")
def zip_folders(parent_folder_path: str):
    # Check if the parent folder exists
    if os.path.exists(parent_folder_path):
        # Get a list of all items (files and subfolders) in the parent folder
        items_in_parent_folder = os.listdir(parent_folder_path)
        
        # Loop through the items in the parent folder
        for item in items_in_parent_folder:
            item_path = os.path.join(parent_folder_path, item)
            if os.path.isdir(item_path):
                zip_folder(item_path)
    else:
        raise Exception("No parent folder")

def run_kcc_script_on_input(parent_folder):
    if os.path.exists(parent_folder):
        # Get a list of all items (files and subfolders) in the parent folder
        items_in_parent_folder = os.listdir(parent_folder)
        
        # Loop through the items in the parent folder
        for item in items_in_parent_folder:
            if is_zip_file(item):
                print("item",item)
                run_kcc_script(item)
    else:
        raise Exception("No parent folder")
      
def run_kcc_script(item):
    # Replace 'python_script_to_run.py' with the name of the script you want to run
    script_to_run = './kcc/kcc-c2e.py'
    try:
        subprocess.run(['python',script_to_run,"-p","K1","./input/" + item])
    except subprocess.CalledProcessError as e:
        print("Error occurred while running the script:", e)

def is_zip_file(file_path):
    return file_path.endswith('.zip')

options = get_options()
folder_prefix = "./"
parent_folder = "input"
prefix = None
# does_have_subfolders = are_there_sub_folders(folder_prefix + parent_folder)

# if prefix is not None:
#     rename_folders(folder_prefix + parent_folder, prefix)
#     parent_folder =  prefix + parent_folder if does_have_subfolders is False else parent_folder
zip_folders(folder_prefix + parent_folder)
run_kcc_script_on_input(folder_prefix + parent_folder)


