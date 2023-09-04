import os as o


def rename_files(folder_path, old_name, new_name):
    for file in o.listdir(folder_path):
        if old_name in file:
            new_file = file.replace(old_name, new_name)
            o.rename(o.path.join(folder_path, file), o.path.join(folder_path, new_file))

rename_files(input("Please Insert folder path here: "))