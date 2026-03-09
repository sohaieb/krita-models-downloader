from yeeti.zero_spinner import spinner
from robust_downloader import download
import pyjson5 as json
from os import path, getenv
import argparse
import sys
import requests
from dotenv import load_dotenv
from git import Repo, RemoteProgress
import subprocess
from rich import print


load_dotenv()

civitai_secret = getenv("CIVITAI_TOKEN")
huggingface_secret = getenv("HUGGINGFACE_TOKEN")

parser = argparse.ArgumentParser(
                    prog='krita-downloader',
                    description='Download Krita AI-diffusion models')


parser.add_argument("--optional", action="store_true", help="Install Optional checkpoints & controlnet for SD1.5, NoobAi, Illustrious, etc.")
parser.add_argument("--required", action="store_true", help="Install Required nodes and models so Krita can work correctly.")
parser.add_argument("--custom", action="store", type=str, help="Install custom models via a custom path, exp. inputs/mycustom.json5")
args = parser.parse_args(sys.argv[1:])


if (hasattr(args, "help") and args.help == True) or len(vars(args)) == 0 :
    parser.print_help()
    exit()


spin = spinner('Init...').start()

required_models_path = path.join("downloader_core","required.json5")
required_nodes_file = path.join("required_nodes.json5")
optional_models_path = path.join("downloader_core", "optional.json5")


# Set the list of models basing on args
all_models = []


if hasattr(args, "required") and bool(args.required) == True:
    with open(required_nodes_file, "r") as f:
        required_nodes = json.load(fp=f)
        for node in required_nodes:
            spin.start()
            print(f"[blue]Start installing {node['name']}..")
            node_path = path.join("custom_nodes",node['name'])
            Repo.clone_from(url=node['url'], to_path=node_path,progress=RemoteProgress())
            result = subprocess.run(['pip', 'install', '-r', 'requirements.txt'], shell=True,cwd=node_path)
            print(result.stdout)
            spin.succeed(f"Node: {node['name']} is installed")
        spin.succeed(f"All required nodes are installed!")
    spin.start()    
    with open(required_models_path, "r") as f:
        all_models = all_models + json.load(fp=f)

if hasattr(args, "optional") and args.optional == True:
    with open(optional_models_path, "r") as f:
        all_models = all_models + json.load(fp=f)

if hasattr(args, "custom") and bool(args.custom) == True:
    custom_models_path = path.join(args.custom)
    with open(custom_models_path) as f:
        all_models = all_models + json.load(fp=f)


spin.succeed("Models list is set")

for model in all_models:
    url = model['url']
    with requests.Session() as s:
        if 'civitai.com' in url:
            url = f"{url}&token={civitai_secret}"
        elif 'huggingface.co' in url:
            s.headers['Authorization'] = f'Bearer {huggingface_secret}'
        with spinner('Processing'):
            download(f"{url}", folder=model['path'], filename=model['filename'], session=s)


spin.succeed("All models are downaloded successfully!")