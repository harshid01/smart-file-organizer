
import os
import shutil
import logging
from tkinter import *
from tkinter import filedialog, messagebox, ttk

# ==========================
# FILE TYPE MAPPING
# ==========================

EXTENSION_MAP = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg'],
    "Videos": ['.mp4', '.mkv', '.mov', '.avi', '.wmv'],
    "Documents": ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx', '.csv'],
    "Music": ['.mp3', '.wav', '.flac', '.aac'],
    "Archives": ['.zip', '.rar', '.7z', '.iso'],
    "Scripts": ['.py', '.js', '.html', '.css', '.php', '.bat', '.ps1'],
    "Programs": ['.exe', '.apk', '.jar'],
    "Databases": ['.db', '.sqlite', '.sql'],
    "Config": ['.json', '.xml', '.yaml', '.yml', '.ini'],
}

selected_folder = ""


# ==========================
# FUNCTIONS
# ==========================

def browse_folder():
    global selected_folder

    folder = filedialog.askdirectory()

    if folder:
        selected_folder = folder
        folder_var.set(folder)


def get_category(extension):
    for category, extensions in EXTENSION_MAP.items():
        if extension.lower() in extensions:
            return category

    return "Others"


def get_unique_name(path):
    if not os.path.exists(path):
        return path

    name, ext = os.path.splitext(path)
    counter = 1

    while True:
        new_path = f"{name}_{counter}{ext}"

        if not os.path.exists(new_path):
            return new_path

        counter += 1


def organize_files():

    if not selected_folder:
        messagebox.showwarning(
            "Warning",
            "Please select a folder first."
        )
        return

    total_files = 0
    organized_files = 0

    log_file = os.path.join(
        selected_folder,
        "file_organization_log.txt"
    )

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(message)s"
    )

    files = [
        f for f in os.listdir(selected_folder)
        if os.path.isfile(os.path.join(selected_folder, f))
    ]

    progress["maximum"] = len(files)
    progress["value"] = 0

    for file in files:

        source = os.path.join(selected_folder, file)

        if file == "file_organization_log.txt":
            continue

        total_files += 1

        extension = os.path.splitext(file)[1]
        category = get_category(extension)

        target_folder = os.path.join(
            selected_folder,
            category
        )

        os.makedirs(target_folder, exist_ok=True)

        destination = os.path.join(
            target_folder,
            file
        )

        destination = get_unique_name(destination)

        try:
            shutil.move(source, destination)

            logging.info(
                f"Moved {file} -> {category}"
            )

            organized_files += 1

        except Exception as e:
            logging.error(str(e))

        progress["value"] += 1
        root.update_idletasks()

    result_label.config(
        text=f"""
Total Files : {total_files}
Organized   : {organized_files}
Location    : {selected_folder}
"""
    )

    messagebox.showinfo(
        "Completed",
        "Files Organized Successfully!"
    )


# ==========================
# GUI
# ==========================

root = Tk()
root.title("Smart File Organizer")
root.geometry("700x450")
root.resizable(False, False)

title = Label(
    root,
    text="Smart File Organizer",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)

folder_var = StringVar()

folder_entry = Entry(
    root,
    textvariable=folder_var,
    width=70
)
folder_entry.pack(pady=5)

browse_btn = Button(
    root,
    text="Browse Folder",
    command=browse_folder,
    width=20
)
browse_btn.pack(pady=10)

organize_btn = Button(
    root,
    text="Organize Files",
    command=organize_files,
    width=20,
    height=2
)
organize_btn.pack(pady=10)

progress = ttk.Progressbar(
    root,
    length=500,
    mode="determinate"
)
progress.pack(pady=20)

result_label = Label(
    root,
    text="Select a folder and click Organize",
    justify=LEFT,
    font=("Arial", 11)
)
result_label.pack(pady=20)

root.mainloop()
