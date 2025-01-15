import shutil
import os

def create(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Folder '{path}' created successfully.")
    else:
        print(f"Folder '{path}' already exists.")

def move_files(folder_origin, folder_dest):

    if not os.path.exists(folder_dest):
        os.makedirs(folder_dest)

    files = os.listdir(folder_origin)

    for file in files:
        full_path = os.path.join(folder_origin, file)
        if os.path.isfile(full_path):
            shutil.move(full_path, folder_dest)
