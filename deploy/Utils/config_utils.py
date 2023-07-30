import json

class ConfigUtils:
    @staticmethod
    def get_config_as_dict(conifg_path)-> dict:
        try:
            # Step 1: Opening the JSON file in read mode
            with open(conifg_path, 'r') as file:
                
                # Step 2: Loading the JSON content into a Python dictionary
                json_object = json.load(file)
                
                # Step 3: Printing the JSON object (Python dictionary)
                print(json_object)
                return json_object
        except FileNotFoundError:
            print(f"The file '{conifg_path}' was not found.")
        except json.JSONDecodeError:
            print(f"Error occurred while parsing the JSON data in file '{conifg_path}'.")
        except IOError:
            print(f"Error occurred while reading the file '{conifg_path}'.")

    @staticmethod
    def get_manga_downloader_command_from_config(mangaDownloadingOptions: dict)-> list:
        command = ['python','./manga_downloader.py']
        for key in mangaDownloadingOptions:
            if mangaDownloadingOptions[key] is not False and mangaDownloadingOptions[key] is not None:
                command.append(key)
                if mangaDownloadingOptions[key] is not True:
                    command.append(str(mangaDownloadingOptions[key]))
        return command
    
    @staticmethod
    def get_kcc_command_from_config(config: dict)-> list:
        command = ['python','./kcc/kcc-c2e.py']
        if 'kccOptions' in config:
            for key in config['kccOptions']:
                if config['kccOptions'][key] is not False and config['kccOptions'][key] is not None:
                    command.append(key)
                    if config['kccOptions'][key] is not True:
                        command.append(config['kccOptions'][key])
        return command