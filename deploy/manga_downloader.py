import os
import subprocess
import zipfile

def download_manga(manga_link: str, series_name: str, volumes_chapter_list_amount: list, start_from_chapter = 1, start_from_volume = 1):
    try:
        # Use ebook-convert to change the author
        current_chapter = start_from_chapter - 1
        total_chapters = calculate_total_chapters(volumes_chapter_list_amount)
        subprocess.run(['python3.8', "./manga-py/manga.py", manga_link, "--name", series_name, "--global-progress", "--skip-volumes", str(current_chapter), "--max-volumes", str(total_chapters), "--destination", "./"])
        unzuip_all("./" + series_name, start_from_volume, volumes_chapter_list_amount)
    except subprocess.CalledProcessError as e:
        print(f'Error cdownload_manga: {e}')

def calculate_total_chapters(volumes_chapter_list_amount: list):
    total = 0
    for item in volumes_chapter_list_amount:
        total = total + item
    return total

def unzuip_all(folder_path:str, start_from_volume: int, volumes_chapter_list_amount: list):
    folder_items = os.listdir(folder_path)

    # Loop through the items in the folder
    volumes_chapter_list_amount_index = 0
    chapter_count = 0
    for item in folder_items:
        if chapter_count >= volumes_chapter_list_amount[volumes_chapter_list_amount_index]:
            chapter_count = 0
            volumes_chapter_list_amount_index = volumes_chapter_list_amount_index + 1
        
        if volumes_chapter_list_amount_index >= len(volumes_chapter_list_amount):
            break
        # Get the full path of the item by joining the folder path with the item name
        item_path = os.path.join(folder_path, item)
        
        # Check if the item is a file or a directory
        if os.path.isfile(item_path):
            unzip(item_path, volumes_chapter_list_amount_index + start_from_volume)
            print(f"Unzip File: {item_path}")
            chapter_count = chapter_count + 1
        elif os.path.isdir(item_path):
            print(f"Directory: {item_path}")
        else:
            print(f"Unknown item: {item_path}")
            
def unzip(zip_file_path: str, volumes_chapter_list_amount_index: int):
    # Directory where you want to extract the contents
    base_name = os.path.basename(zip_file_path).replace(".zip","")
    dir_name = os.path.dirname(zip_file_path)
    # Extract the contents of the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall("./input/" + os.path.basename(dir_name) + " Vol." + str(volumes_chapter_list_amount_index) + "/" + base_name)
    os.remove(zip_file_path)

# Example usage:
if __name__ == "__main__":
    mangaLink = "https://www.mangatown.com/manga/shingeki_no_kyojin/"
    series_name = "Attack On Titan"
    volumes_chapter_list_amount = [2, 2]
    start_from_chapter = 3
    start_from_volume = 2
    # download_manga(mangaLink, series_name, volumes_chapter_list_amount, start_from_chapter, start_from_volume)
    download_manga(mangaLink, series_name, volumes_chapter_list_amount,start_from_chapter, start_from_volume)

