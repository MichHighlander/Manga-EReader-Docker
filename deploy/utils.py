import os
import zipfile

class Utils:
    @staticmethod
    def calculate_total_int_from_list(int_list: list)->int:
        total = 0
        for item in int_list:
            total = total + item
        return total

    @staticmethod
    def unzip(zip_file_path: str, unzip_destination: str, should_remove_zip_after_unzip: bool):
        # Directory where you want to extract the contents
        base_name = os.path.basename(zip_file_path).replace(".zip","")
        # Extract the contents of the zip file
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(unzip_destination + base_name)
        if should_remove_zip_after_unzip is True:
            os.remove(zip_file_path)