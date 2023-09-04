import os


def remove_empty_folders(folder_path):
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)

            if not os.listdir(folder_path):
                os.rmdir(folder_path)
