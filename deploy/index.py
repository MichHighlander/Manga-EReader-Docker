import json
import os
import shutil
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
    print("Finished zipping ", folder_path + ".zip")

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

def run_kcc_script_on_input(parent_folder, config: dict):
    if os.path.exists(parent_folder):
        # Get a list of all items (files and subfolders) in the parent folder
        items_in_parent_folder = os.listdir(parent_folder)
        
        command = get_kcc_command_from_config(config)
        # Loop through the items in the parent folder
        for item in items_in_parent_folder:
            if is_zip_file(item):
                print("item",item)
                run_kcc_script(item, command)
    else:
        raise Exception("No parent folder")
      
def run_kcc_script(item: str, command: list):
    # Replace 'python_script_to_run.py' with the name of the script you want to run
    # script_to_run = './kcc/kcc-c2e.py'
    command_and_item = command.copy()
    command_and_item.append("./input/" + item)
    try:
        subprocess.run(command_and_item)
        send_file_to_kindle("./input/" + item.replace(".zip",".mobi"))
    except subprocess.CalledProcessError as e:
        print("Error occurred while running the script:", e)

def is_zip_file(file_path):
    return file_path.endswith('.zip')

def get_kcc_command_from_config(config: dict):
    command = ['python','./kcc/kcc-c2e.py']
    if 'kccOptions' in config:
       for key in config['kccOptions']:
        if config['kccOptions'][key] is not False and config['kccOptions'][key] is not None:
            command.append(key)
            if config['kccOptions'][key] is not True:
                command.append(config['kccOptions'][key])
    return command

def rename_folders(parent_folder_path: str, prefix: str):
    # Check if the parent folder exists
    if os.path.exists(parent_folder_path):
        # Get a list of all items (files and subfolders) in the parent folder
        if are_there_sub_folders(parent_folder_path) is True:
            items_in_parent_folder = os.listdir(parent_folder_path)
            
            # Loop through the items in the parent folder
            for item in items_in_parent_folder:
                item_path = os.path.join(parent_folder_path, item)
                if os.path.isdir(item_path):
                    # Replace 'prefix_' with the prefix you want to add to each subfolder
                    new_folder_name = prefix + item
                    new_item_path = os.path.join(parent_folder_path, new_folder_name)
                    
                    try:
                        # Rename the subfolder
                        os.rename(item_path, new_item_path)
                        print(f"Subfolder '{item}' renamed to '{new_folder_name}' successfully.")
                    except FileExistsError:
                        print(f"A folder with the name '{new_folder_name}' already exists.")
                    except OSError as e:
                        print(f"Error occurred while renaming the subfolder '{item}': {e}")
        else:
            rename_folder(parent_folder_path, prefix)
    else:
        raise Exception("No parent folder")

def rename_folder(folder_path: str, prefix: str):
    # Replace 'folder_path' with the appropriate path to the folder you want to rename

    # Replace 'prefix_' with the prefix you want to add
    new_folder_name = prefix + os.path.basename(folder_path)

    try:
        # Rename the folder by adding the prefix
        os.rename(folder_path, new_folder_name)
        print(f"Folder renamed to '{new_folder_name}' successfully.")
    except FileNotFoundError:
        print(f"The folder '{folder_path}' was not found.")
    except FileExistsError:
        print(f"A folder with the name '{new_folder_name}' already exists.")
    except OSError as e:
        print(f"Error occurred while renaming the folder: {e}")

def send_file_to_kindle(file_path: str):
    try:
        print("send_file_to_kindle: ", file_path)
        
        # Convert the .mobi file to Kindle format (AZW3)\
        shutil.move(file_path, "./output/" + os.path.basename(file_path))
        # subprocess.run(['ebook-convert', file_path, "./output/" + os.path.basename(file_path)])
        print(f'Successfully sent {file_path} to Kindle!')
    except subprocess.CalledProcessError as e:
        print(f'Error sending {file_path} to Kindle:', e)

def run_manga_downloader():
    try:
        subprocess.run(["python", "./manga_downloader.py"])
    except Exception as e:
        print(f'run_manga_downloader Error {e}')
    
options = get_options()
folder_prefix = "./"
parent_folder = "input"
does_have_subfolders = are_there_sub_folders(folder_prefix + parent_folder)

prefix = None
try:
    prefix = options["baseOptions"]["addVolumePrefix"]
except:
    pass
if prefix is not None:
    rename_folders(folder_prefix + parent_folder, prefix)
    parent_folder =  prefix + parent_folder if does_have_subfolders is False else parent_folder

if does_have_subfolders is False:
    run_manga_downloader()
print("after manga downloader")
zip_folders(folder_prefix + parent_folder)
run_kcc_script_on_input(folder_prefix + parent_folder, options)


