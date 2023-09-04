def find_replace(file_path, search_text, replace_text):
    with open(file_path, 'r') as f:
        text = f.read()
        mod_text = text.replace(search_text, replace_text)

    with open(file_path, 'w') as f:
        f.write(mod_text)


find_replace(input("Insert Folder's Path Here: "))
