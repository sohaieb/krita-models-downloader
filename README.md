# Krita Models Downloader

_Krita Models Downloader_ is a simple python script to easily download models for Krita AI diffusion in their right paths.

## Usage

### Display CLI help

```bash
python downloader.py --help
```

---

### Download required models & setup nodes

```bash
python downloader.py --required --nodes
```

---

### Download optional models

```bash
python downloader.py --optional
```

---

### Download custom Krita available models

#### Setup Flux

1. Install required flux models

```bash
python downloader.py --custom downloader_core/flux_shared.json5
```

2. Then install klein specific models

```bash
python downloader.py --custom downloader_core/flux.json5
```

#### Setup Flux 2 Klein

1. Install required flux models

```bash
python downloader.py --custom downloader_core/flux_shared.json5
```

2. Then install klein specific models

```bash
python downloader.py --custom downloader_core/flux-klein.json5
```

---

#### Setup All Krita Core models (required, optional and others) and custom ComfyUi nodes

- Setup all

```bash
python downloader.py --core
```

- Setup all except few ones (exclusion), example: exclude z-image and flux models

- Setup all

```bash
python downloader.py --core --exclude z-image.json5 flux.json5
```

---

#### Setup Z-Image

```bash
python downloader.py --custom downloader_core/z-image.json5
```

---

### Download custom models (like from [Civitai.com](https://civitai.com/))

```bash
python downloader.py --custom my-folder/myfile.json5 another-folder/my-other-file.json5 ..
```

**Note:** if you struggle about how to define your own custom models in json5 format, please take a look at one of the \_.json5 files in `downloader_core/*`

---

## SSH Upload your downloader & all configs

It can be done via `sshup.py` script with the configuration of `.env` file. You have to setup `COMFYUI_FOLDER_PATH`, `SSH_HOST`, `SSH_PORT` and `SSH_USER` variables.

```bash
python sshup.py
```

## Author

Sohaieb Azaiez
