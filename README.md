## INSTALLATION
1. Install docker

## Optional:
Create a options json in this format
{
    "baseOptions": {
        "addVolumePrefix": null //Add prefix to volumes
    },
    "kccOptions": {
        "--profile": null,
        "--manga-style": false,
        "--hq": false,
        "--two-panel": false,
        "--webtoon": false,
        "--targetsize": null,
        "--noprocessing": false,
        "--upscale": false,
        "--stretch": false,
        "--splitter": null,
        "--gamma": null,
        "--cropping": null,
        "--croppingpower": null,
        "--croppingminimum": null,
        "--blackborders": false,
        "--whiteborders": false,
        "--forcecolor": false,
        "--forcepng": false,
        "--mozjpeg": false,
        "--maximizestrips": false,
        "--delete": false,
        "--output": null,
        "--title": null,
        "--format": null,
        "--batchsplit": null
    }
}

### KCC options:
```
        'K1': ("Kindle 1", (600, 670), Palette4, 1.8),
        'K11': ("Kindle 11", (1072, 1448), Palette16, 1.8),
        'K2': ("Kindle 2", (600, 670), Palette15, 1.8),
        'K34': ("Kindle Keyboard/Touch", (600, 800), Palette16, 1.8),
        'K578': ("Kindle", (600, 800), Palette16, 1.8),
        'KDX': ("Kindle DX/DXG", (824, 1000), Palette16, 1.8),
        'KPW': ("Kindle Paperwhite 1/2", (758, 1024), Palette16, 1.8),
        'KV': ("Kindle Paperwhite 3/4/Voyage/Oasis", (1072, 1448), Palette16, 1.8),
        'KPW5': ("Kindle Paperwhite 5/Signature Edition", (1236, 1648), Palette16, 1.8),
        'KO': ("Kindle Oasis 2/3", (1264, 1680), Palette16, 1.8),
        'KS': ("Kindle Scribe", (1860, 2480), Palette16, 1.8),
        'KoMT': ("Kobo Mini/Touch", (600, 800), Palette16, 1.8),
        'KoG': ("Kobo Glo", (768, 1024), Palette16, 1.8),
        'KoGHD': ("Kobo Glo HD", (1072, 1448), Palette16, 1.8),
        'KoA': ("Kobo Aura", (758, 1024), Palette16, 1.8),
        'KoAHD': ("Kobo Aura HD", (1080, 1440), Palette16, 1.8),
        'KoAH2O': ("Kobo Aura H2O", (1080, 1430), Palette16, 1.8),
        'KoAO': ("Kobo Aura ONE", (1404, 1872), Palette16, 1.8),
        'KoN': ("Kobo Nia", (758, 1024), Palette16, 1.8),
        'KoC': ("Kobo Clara HD/Kobo Clara 2E", (1072, 1448), Palette16, 1.8),
        'KoL': ("Kobo Libra H2O/Kobo Libra 2", (1264, 1680), Palette16, 1.8),
        'KoF': ("Kobo Forma", (1440, 1920), Palette16, 1.8),
        'KoS': ("Kobo Sage", (1440, 1920), Palette16, 1.8),
        'KoE': ("Kobo Elipsa", (1404, 1872), Palette16, 1.8),
        'OTHER': ("Other", (0, 0), Palette16, 1.8),
```

### Steps:
1. docker build -t <container_name> . 
2. docker run -v <options_file_path>.json:/app/options.json -v <local_input_folder>:/app/input <container_name>