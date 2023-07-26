## INSTALLATION
1. Install docker

## Sources
for KCC Options read:
https://github.com/ciromattia/kcc

for Manga Downloading Options - Manga Link:
https://manga-py.github.io/manga-py/#resources-list
Recommended sites:
- https://manganato.com/
- https://kissmanga.in/
- https://www.mangatown.com/
- https://mangakakalot.com/

## Tutorial - How to setup "mangaDownloadingOptions"
1. Find a manga from the site list above.
2. Search in google: <Manga_Name> volumes list
3. Fill "--volumes_chapter_list_amount" with the amount of chapter for each volume.

Example - Download volume 2 and 3 of "Shingeki no Kyojin":
1. Enter: https://www.mangatown.com/manga/shingeki_no_kyojin/
2. Enter: https://en.wikipedia.org/wiki/List_of_Attack_on_Titan_chapters
3. Write: 
    "mangaDownloadingOptions": {
        "--manga_link": https://www.mangatown.com/manga/shingeki_no_kyojin/
        "--series_name": Shingeki no Kyojin
        "--volumes_chapter_list_amount": [6,4] //In the volume wikipedia we see that volume 2 there are 5 chapters but in MangaTown we can see that there is a half chapter 9.5, so to also include it we need to add 1 to volume 2 chapter list.
        "--start_from_chapter": 6 //In the volume wikipedia it is written that volume 2 starts at chapter 5 but at MangaTown we can see that there is a "one shoot" at the start and i dont want it so i added 1.
        "--start_from_volume': 2
    },

## Config:
Create a options json in this format (Optins with a boolean is without payload to the options and options with null have payload)
```
  {
      "baseOptions": {
          "addVolumePrefix": null //Add prefix to volumes
      },
      "mangaDownloadingOptions": {
        "--manga_link": A link to the manga's url. [Required]
        "--series_name": The name of the series. [Required]
        "--volumes_chapter_list_amount": A list of integers that represent how much chapters are in each volume. [Required]
        "--start_from_chapter": A chapter to start from, included. (Example: 3 will download from chapter 3 and beyond). Default: 1', default=1.
        "--start_from_volume': The number of volume to start counting from. Default: 1', default=1.

      },
      "kccOptions": {
          "--profile": null, #Example for a option with parameter (should null to the parameter)
          "--manga-style": false, #Example for option without paramter (should change to true if option needed)
      }
  }
```

## How to build local input folder:
```
-local_input_folder---|
                      |
                      V
                    - Manga Vol.1 Folder----|
                                            |
                                            V
                                          - Chapter 1 Folder
                                          - Chapter 2 Folder

                    - Manga Vol.2 Folder----|
                                            |
                                            V
                                          - Chapter 3 Folder
                                          - Chapter 4 Folder
```
### Steps:
1.
```
docker build -t <container_name> . 
```

2.
*Disclamer*: if <local_input_folder> is given and is not empty, the code will ignore "mangaDownloadingOptions" and will not download new manga.
```
docker run -v <options_file_path>.json:/app/options.json -v <local_input_folder>:/app/input <kindle_dir>/documents/:/app/output <container_name>
```
