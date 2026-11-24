import os
from sync import sync_folders

base_path = os.path.dirname(os.path.abspath(__file__))

source = os.path.join(base_path, "Source")
destination = os.path.join(base_path, "Backup")

os.makedirs(source, exist_ok=True)
os.makedirs(destination, exist_ok=True)

sync_folders(source, destination)