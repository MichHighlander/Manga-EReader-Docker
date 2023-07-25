import subprocess
import os
import zipfile

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

def zip_folder(folder_path):
    with zipfile.ZipFile(folder_path + ".zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))


def zip_folders(parent_folder_path: str):
    # Check if the parent folder exists
    if os.path.exists(parent_folder_path):
        # Get a list of all items (files and subfolders) in the parent folder
        if are_there_sub_folders(parent_folder_path) is True:
            items_in_parent_folder = os.listdir(parent_folder_path)
            
            # Loop through the items in the parent folder
            for item in items_in_parent_folder:
                item_path = os.path.join(parent_folder_path, item)
                if os.path.isdir(item_path):
                    zip_folder(item_path)
        else:
            zip_folder(parent_folder_path)
    else:
        raise Exception("No parent folder")

def run_second_script():
    # Replace 'python_script_to_run.py' with the name of the script you want to run
    script_to_run = 'second_text.py'

    try:
        subprocess.run(['python3.8', script_to_run,"-param","123"])
    except subprocess.CalledProcessError as e:
        print("Error occurred while running the script:", e)

def get_kcc_command_from_config(config: dict):
    command = ['python','./kcc/kcc-c2e.py']
    if 'kccOptions' in config:
       for key in config['kccOptions']:
        if config['kccOptions'][key] is not False and config['kccOptions'][key] is not None:
            command.append(key)
            if config['kccOptions'][key] is not True:
                command.append(config['kccOptions'][key])
    return command

# folder_prefix = "./"
# parent_folder = "folderparent"
# prefix = None
# does_have_subfolders = are_there_sub_folders(folder_prefix + parent_folder)

# if prefix is not None:
#     rename_folders(folder_prefix + parent_folder, prefix)
#     parent_folder =  prefix + parent_folder if does_have_subfolders is False else parent_folder
# zip_folders(folder_prefix + parent_folder)
# run_second_script()

options = {
    "baseOptions": {
        "addVolumePrefix": "Golden Kamui "
    },
    "kccOptions": {
        "--profile": "KPW5",
        "--manga-style": True,
        "--hq": True,
        "--two-panel": False,
        "--webtoon": False,
        "--targetsize": None,
        "--noprocessing": False,
        "--upscale": False,
        "--stretch": False,
        "--splitter": None,
        "--gamma": None,
        "--cropping": None,
        "--croppingpower": None,
        "--croppingminimum": None,
        "--blackborders": False,
        "--whiteborders": False,
        "--forcecolor": False,
        "--forcepng": False,
        "--mozjpeg": False,
        "--maximizestrips": False,
        "--delete": False,
        "--output": None,
        "--title": None,
        "--format": None,
        "--batchsplit": None
    }
}

command = get_kcc_command_from_config(options)
print(command)