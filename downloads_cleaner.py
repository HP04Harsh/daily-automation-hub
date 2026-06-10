import os
import shutil

# Set the path to the folder you want to clean
target_dir = os.path.expanduser("~/Downloads")

# Define folder mappings
EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Archives": [".zip", ".tar", ".gz"],
}

for filename in os.listdir(target_dir):
    file_path = os.path.join(target_dir, filename)
    
    # Skip directories
    if os.path.isdir(file_path):
        continue
        
    # Get file extension
    _, ext = os.path.splitext(filename)
    
    # Move file to corresponding folder
    for folder_name, ext_list in EXTENSIONS.items():
        if ext.lower() in ext_list:
            dest_folder = os.path.join(target_dir, folder_name)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_folder, filename))
            print(f"Moved: {filename} -> {folder_name}")