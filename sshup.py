import subprocess
from os import path, listdir, getenv
from dotenv import load_dotenv

load_dotenv()

ssh_host = getenv('SSH_HOST')
ssh_port = getenv('SSH_PORT')
ssh_user = getenv('SSH_USER')
comfyui_folder_path = getenv('COMFYUI_FOLDER_PATH')

# ssh root@82.221.170.234 -p 31498 -i ~/.ssh/id_ed25519
# path: /workspace/runpod-slim/ComfyUI
# Securely copy file or folder (-r)

def get_command(item:str, is_folder: bool): 
    base_command = ['scp',f'-P {ssh_port}']
    if is_folder:
        base_command.append('-r')

    if bool(item):
        base_command.append(item)
    return base_command + [f'{ssh_user}@{ssh_host}:{comfyui_folder_path}/']

paths_exlude = [
    '.git',
    '.gitignore',
    '.venv',
    '.env.example',
    'mise.toml',
    'README.md',
    'sshup.py'
]



directory_files = listdir('.')
items_to_upload = list(filter(lambda item: item not in paths_exlude, directory_files))

for item_to_up in items_to_upload:
    item_path = path.join(item_to_up)

    if path.isdir(item_path):
        command = get_command(item_path,True)
    else:
        command = get_command(item_path,False)
    print(command)
    subprocess.run(command)