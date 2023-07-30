import os
import zipfile


class ZipUtils:
    @staticmethod
    def zip_folder(folder_path):
        with zipfile.ZipFile(folder_path + ".zip", 'w', zipfile.ZIP_STORED) as zipf:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, folder_path))
        print("Finished zipping ", folder_path + ".zip")

    @staticmethod
    def unzip(zip_file_path: str, unzip_destination: str, should_remove_zip_after_unzip: bool):
        # Directory where you want to extract the contents
        base_name = os.path.basename(zip_file_path).replace(".zip","")
        # Extract the contents of the zip file
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(unzip_destination + base_name)
        if should_remove_zip_after_unzip is True:
            os.remove(zip_file_path)

    @staticmethod
    def is_zip_file(file_path):
        return file_path.endswith('.zip')