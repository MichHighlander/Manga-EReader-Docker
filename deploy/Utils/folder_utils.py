import os
import shutil
import subprocess


class FolderUtils:
    @staticmethod
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
        
    @staticmethod
    def add_prefix_to_folder(folder_path: str, prefix: str):
        if os.path.isdir(folder_path):
            # Replace 'prefix_' with the prefix you want to add to each subfolder
            new_folder_name = prefix + os.path.basename(folder_path)
            new_item_path = os.path.join(os.path.dirname(folder_path), new_folder_name)
            
            try:
                # Rename the subfolder
                os.rename(folder_path, new_item_path)
                print(f"Subfolder '{folder_path}' renamed to '{new_folder_name}' successfully.")
            except FileExistsError:
                print(f"A folder with the name '{new_folder_name}' already exists.")
            except OSError as e:
                print(f"Error occurred while renaming the subfolder '{folder_path}': {e}")

    @staticmethod
    def move_file(file_path: str, destination_as_file:str):
        try:
            print("move_file: ", file_path)
            # Convert the .mobi file to Kindle format (AZW3)\
            shutil.move(file_path, destination_as_file)
            # subprocess.run(['ebook-convert', file_path, "./output/" + os.path.basename(file_path)])
            print(f'Successfully sent {file_path} to Kindle!')
        except subprocess.CalledProcessError as e:
            print(f'Error sending {file_path} to Kindle:', e)