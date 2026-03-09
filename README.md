# Krita Models Downloader

*Krita Models Downloader* is a simple python script to easily download models for Krita AI diffusion in their right paths.

## Usage

```bash
python downloader.py --help
```

## Download required models

```bash
python downloader.py --required
```

## Download optional models

```bash
python downloader.py --optional
```


## Download custom models (like from [Civitai.com](https://civitai.com/))

```bash
python downloader.py --custom myfolder/myfile.json5
```

*Note:* if you struggle about how to define models, please look at one of the *.json5 files in `downloader_core/*` 