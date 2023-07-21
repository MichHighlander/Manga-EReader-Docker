Install docker

Steps:
1. docker build -t <container_name> . 
2. docker run -v <options_file_path>.json:/app/options.json -v <local_input_folder>:/app/input my_container