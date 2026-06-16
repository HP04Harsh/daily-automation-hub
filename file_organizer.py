import os
import shutil

# Path to your Downloads folder
source_folder = r"C:\Users\YourName\Downloads"

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Vicleaner.pycleaner.pydeos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()

        for folder, extensions in file_types.items():
            if extension in extensions:
                destination_folder = os.path.join(source_folder, folder)

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                shutil.move(file_path, os.path.join(destination_folder, filename))
                print(f"Moved: {filename} → {folder}")
                break

print("File organization completed!")