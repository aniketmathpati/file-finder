import os, shutil
# you may add other extensions also
dict_extensions = {
    'audio_extensions' : ('mp3'),
    'video_extensions' : ('mp4', 'mkv'),
    'doc_extensions'   : ('pdf', 'docx', 'txt'),
    'image_extensions' : ('jpg', 'png'),
    'ppt_extensions'   : ('pptx')
}


def file_finder(current_path, file_extensions):
    files = []
    for file in os.listdir(current_path):
        for extension in file_extensions:
            if file.endswith(extension):
                files.append(file)
    return files

current_path = input("Enter folder path : ")

for file_type, file_extension in dict_extensions.items():
    files = file_finder(current_path, file_extension)
    if len(files) > 0:
        new_folder = file_type.split('_')[0] + 'Files'
        new_folder_path = os.path.join(current_path, new_folder)
        try:
            os.mkdir(new_folder_path)
        except FileExistsError:
            print(f"{new_folder} folder already exists")
        for item in files:
            item_path = os.path.join(current_path, item)
            new_item_path = os.path.join(new_folder_path, item)
            shutil.move(item_path, new_item_path)
    else:
        print(f"No {file_type.split('_')[0]} files")
