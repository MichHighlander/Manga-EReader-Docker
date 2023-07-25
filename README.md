## INSTALLATION
1. Install docker

## Sources
for KCC Options read:
https://github.com/ciromattia/kcc

## Optional:
Create a options json in this format (Optins with a boolean is without payload to the options and options with null have payload)
```
  {
      "baseOptions": {
          "addVolumePrefix": null //Add prefix to volumes
      },
      "kccOptions": {
          "--profile": null, #Example for a option with parameter (should null to the parameter)
          "--manga-style": false, #Example for option without paramter (should change to true if option needed)
      }
  }
```

### Steps:
```
1. docker build -t <container_name> . 
2. docker run -v <options_file_path>.json:/app/options.json -v <local_input_folder>:/app/input <kindle_dir>/documents/:/app/output <container_name>
```