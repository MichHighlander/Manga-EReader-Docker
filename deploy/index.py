import os
import subprocess

from Utils.folder_utils import FolderUtils
from Utils.config_utils import ConfigUtils
from Utils.zip_utils import ZipUtils
    
def zip_all_sub_folders(parent_folder_path: str):
    # Check if the parent folder exists
    if os.path.exists(parent_folder_path):
        # Get a list of all items (files and subfolders) in the parent folder
        items_in_parent_folder = os.listdir(parent_folder_path)
        
        # Loop through the items in the parent folder
        for item in items_in_parent_folder:
            item_path = os.path.join(parent_folder_path, item)
            if os.path.isdir(item_path):
                ZipUtils.zip_folder(item_path)
    else:
        raise Exception("No parent folder")

def run_kcc_script_on_input(parent_folder, config: dict):
    if os.path.exists(parent_folder):
        # Get a list of all items (files and subfolders) in the parent folder
        items_in_parent_folder = os.listdir(parent_folder)
        
        command = ConfigUtils.get_kcc_command_from_config(config)
        # Loop through the items in the parent folder
        for item in items_in_parent_folder:
            if ZipUtils.is_zip_file(item):
                print("item",item)
                run_kcc_script(item, command, config)
    else:
        raise Exception("No parent folder")
      
def run_kcc_script(item: str, command: list, config: dict):
    command_and_item = command.copy()
    command_and_item.append("./input/" + item)
    try:
        subprocess.run(command_and_item)
        #Moving mobi file to output folder (Kindle)
        mobi_file = ConfigUtils.find_new_file_created_by_kcc(item, config)
        destination = "./output/" + mobi_file
        FolderUtils.move_file("./input/" + mobi_file, destination)
    except subprocess.CalledProcessError as e:
        print("Error occurred while running the script:", e)

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

def run_manga_downloader(mangaDownloadingOptions):
    try:
        command = ConfigUtils.get_manga_downloader_command_from_config(mangaDownloadingOptions)
        subprocess.run(command)
    except Exception as e:
        print(f'run_manga_downloader Error {e}')

#Script start
config = ConfigUtils.get_config_as_dict('/app/options.json')
folder_prefix = "./"
parent_folder = "input"
does_have_subfolders = FolderUtils.are_there_sub_folders(folder_prefix + parent_folder)

prefix = None
try:
    prefix = config["baseOptions"]["addVolumePrefix"]
except:
    pass

if prefix is not None:
    rename_all_sub_folders(folder_prefix + parent_folder, prefix)
    parent_folder =  prefix + parent_folder if does_have_subfolders is False else parent_folder

if does_have_subfolders is False and "mangaDownloadingOptions" in config:
    run_manga_downloader(config["mangaDownloadingOptions"])
print("after manga downloader")
zip_all_sub_folders(folder_prefix + parent_folder)
run_kcc_script_on_input(folder_prefix + parent_folder, config)


