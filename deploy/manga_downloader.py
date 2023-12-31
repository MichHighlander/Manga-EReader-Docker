import argparse
import ast
import os
import subprocess

from Utils.utils import Utils
from Utils.zip_utils import ZipUtils

class ParseListAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        try:
            # Convert the string representation of the list to an actual list
            parsed_list = ast.literal_eval(values)
            setattr(namespace, self.dest, parsed_list)
        except (ValueError, SyntaxError) as e:
            raise argparse.ArgumentTypeError(f"Invalid list format for {self.dest}: {values}")
        
def download_manga(manga_link: str, series_name: str, volumes_chapter_list_amount: list, start_from_chapter = 1, start_from_volume = 1):
    try:
        # Use ebook-convert to change the author
        current_chapter = start_from_chapter - 1
        total_chapters = Utils.calculate_total_int_from_list(volumes_chapter_list_amount)
        subprocess.run(['python3.8', "./manga-py/manga.py", manga_link, "--name", series_name, "--global-progress", "--skip-volumes", str(current_chapter), "--max-volumes", str(total_chapters), "--destination", "./"])
        unzuip_all("./" + series_name, start_from_volume, volumes_chapter_list_amount)
    except subprocess.CalledProcessError as e:
        print(f'Error cdownload_manga: {e}')

def unzuip_all(folder_path:str, start_from_volume: int, volumes_chapter_list_amount: list):
    folder_items = sorted(os.listdir(folder_path))

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
            dir_name = os.path.dirname(item_path)
            unzip_destination: str = "./input/" + os.path.basename(dir_name) + " Vol." + str(volumes_chapter_list_amount_index + start_from_volume) + "/"
            ZipUtils.unzip(item_path, unzip_destination, True)
            print(f"Unzip File: {item_path}")
            chapter_count = chapter_count + 1
        elif os.path.isdir(item_path):
            print(f"Directory: {item_path}")
        else:
            print(f"Unknown item: {item_path}")

if __name__ == "__main__":
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='A script with command-line arguments.')

    parser.add_argument('--manga_link', type=str, required=True, help="A link to the manga's url")
    parser.add_argument('--series_name', type=str, required=True, help='The name of the series')
    parser.add_argument('--volumes_chapter_list_amount', type=str, required=True, action=ParseListAction, help='A list of integers that represent how much chapters are in each volume')
    parser.add_argument('--start_from_chapter', type=int, help='A chapter to start from, included. (Example: 3 will download from chapter 3 and beyond). Default: 1', default=1)
    parser.add_argument('--start_from_volume', type=int,help='The number of volume to start counting from. Default: 1', default=1)

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the values of the arguments
    manga_link = args.manga_link
    series_name = args.series_name
    volumes_chapter_list_amount = args.volumes_chapter_list_amount
    start_from_chapter = args.start_from_chapter
    start_from_volume = args.start_from_volume

    if len(volumes_chapter_list_amount) == 0:
        raise Exception("--volumes_chapter_list_amount is Empty!")

    download_manga(manga_link, series_name, volumes_chapter_list_amount,start_from_chapter, start_from_volume)

