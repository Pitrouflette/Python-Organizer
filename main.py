import tkinter as tk
from tkinter import filedialog
import os
import shutil

path = ""


def create_folders(directories, directory_path):
    for key in directories:
        if key not in os.listdir(directory_path):
            os.mkdir(os.path.join(directory_path, key))
    if "OTHER" not in os.listdir(directory_path):
        os.mkdir(os.path.join(directory_path, "OTHER"))


def organize_folders(directories, directory_path):
    for file in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, file)):
            src_path = os.path.join(directory_path, file)
            for key in directories:
                extension = directories[key]
                if file.endswith(extension):
                    dest_path = os.path.join(directory_path, key, file)
                    shutil.move(src_path, dest_path)
                    break


def organize_remaining_files(directory_path):
    for file in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, file)):
            src_path = os.path.join(directory_path, file)
            dest_path = os.path.join(directory_path, "OTHER", file)
            shutil.move(src_path, dest_path)


def organize_remaining_folders(directories, directory_path):
    list_dir = os.listdir(directory_path)
    organized_folders = []
    for folder in directories:
        organized_folders.append(folder)
    organized_folders = tuple(organized_folders)
    for folder in list_dir:
        if folder not in organized_folders:
            src_path = os.path.join(directory_path, folder)
            dest_path = os.path.join(directory_path, "FOLDERS", folder)
            try:
                shutil.move(src_path, dest_path)
            except shutil.Error:
                shutil.move(src_path, dest_path + " - copy")
                print("That folder already exists in the destination folder."
                      "\nThe folder is renamed to '{}'".format(folder + " - copy"))


def start(directory_path):
    directories = {
        "WEB": (".html5", ".html", ".htm", ".xhtml", '.css'),
        "IMAGES": (".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg",
                   "svg",
                   ".heif", ".psd"),
        "VIDEOS": (".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",
                   ".mng",
                   ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"),
        "DOCUMENTS": (".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf",
                      ".ods",
                      ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                      ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                      "pptx", ".odp"),
        "ARCHIVES": (".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                     ".dmg", ".rar", ".xar", ".zip"),
        "AUDIO": (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p",
                  ".mp3",
                  ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"),
        "PLAINTEXT": (".txt", ".in", ".out"),
        "PDF": ".pdf",
        "PYTHON": ".py",
        "JAVA": ".jar",
        "JS": (".js", ".json"),
        "EXE": ".exe",
        "OTHER": "",
        "FOLDERS": "",
        "MSI": ".msi",
        "NOT_CONFIRM": ".crdownload"
    }
    try:
        print(directory_path)
        create_folders(directories, directory_path)
        organize_folders(directories, directory_path)
        organize_remaining_files(directory_path)
        organize_remaining_folders(directories, directory_path)
    except shutil.Error:
        print("There was an error trying to move an item to its destination folder")


def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_path_label.config(text=f"Selected directory's path : {folder_path}")
        start(folder_path)
    else:
        folder_path_label.config(text="No directory selected")


window = tk.Tk()
window.title("Select a directory")

select_button = tk.Button(window, text="Select a directory", command=select_folder)
select_button.pack(pady=20)

folder_path_label = tk.Label(window, text="", wraplength=400)
folder_path_label.pack()

window.mainloop()
