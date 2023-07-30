import json
import os
import shutil
import subprocess

from Utils.utils import Utils
from Utils.folder_utils import FolderUtils

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
    
def zip_all_sub_folders(parent_folder_path: str):
    # Check if the parent folder exists
    if os.path.exists(parent_folder_path):
        # Get a list of all items (files and subfolders) in the parent folder
        items_in_parent_folder = os.listdir(parent_folder_path)
        
        # Loop through the items in the parent folder
        for item in items_in_parent_folder:
            item_path = os.path.join(parent_folder_path, item)
            if os.path.isdir(item_path):
                Utils.zip_folder(item_path)
    else:
        raise Exception("No parent folder")

def run_kcc_script_on_input(parent_folder, config: dict):
    if os.path.exists(parent_folder):
        # Get a list of all items (files and subfolders) in the parent folder
        items_in_parent_folder = os.listdir(parent_folder)
        
        command = get_kcc_command_from_config(config)
        # Loop through the items in the parent folder
        for item in items_in_parent_folder:
            if Utils.is_zip_file(item):
                print("item",item)
                run_kcc_script(item, command)
    else:
        raise Exception("No parent folder")
      
def run_kcc_script(item: str, command: list):
    command_and_item = command.copy()
    command_and_item.append("./input/" + item)
    try:
        subprocess.run(command_and_item)
        #Moving mobi file to output folder (Kindle)
        mobi_file = item.replace(".zip",".mobi")
        destination = "./output/" + mobi_file
        FolderUtils.move_file("./input/" + mobi_file, destination)
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

def rename_all_sub_folders(parent_folder_path: str, prefix: str):
    # Check if the parent folder exists
    if os.path.exists(parent_folder_path):
        # Get a list of all items (files and subfolders) in the parent folder
        if FolderUtils.are_there_sub_folders(parent_folder_path) is True:
            items_in_parent_folder = os.listdir(parent_folder_path)
            
            # Loop through the items in the parent folder
            for item in items_in_parent_folder:
                item_path = os.path.join(parent_folder_path, item)
                FolderUtils.add_prefix_to_folder(item_path, prefix)
    else:
        raise Exception("No parent folder")

def get_manga_downloader_command_from_config(mangaDownloadingOptions: dict):
    command = ['python','./manga_downloader.py']
    for key in mangaDownloadingOptions:
        if mangaDownloadingOptions[key] is not False and mangaDownloadingOptions[key] is not None:
            command.append(key)
            if mangaDownloadingOptions[key] is not True:
                command.append(str(mangaDownloadingOptions[key]))
    return command

def run_manga_downloader(mangaDownloadingOptions):
    try:
        command = get_manga_downloader_command_from_config(mangaDownloadingOptions)
        subprocess.run(command)
    except Exception as e:
        print(f'run_manga_downloader Error {e}')

options = get_options()
folder_prefix = "./"
parent_folder = "input"
does_have_subfolders = FolderUtils.are_there_sub_folders(folder_prefix + parent_folder)

prefix = None
try:
    prefix = options["baseOptions"]["addVolumePrefix"]
except:
    pass

if prefix is not None:
    rename_all_sub_folders(folder_prefix + parent_folder, prefix)
    parent_folder =  prefix + parent_folder if does_have_subfolders is False else parent_folder

if does_have_subfolders is False and "mangaDownloadingOptions" in options:
    run_manga_downloader(options["mangaDownloadingOptions"])
print("after manga downloader")
zip_all_sub_folders(folder_prefix + parent_folder)
run_kcc_script_on_input(folder_prefix + parent_folder, options)


