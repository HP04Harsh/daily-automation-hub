import os
import shutil

# Define the directory you want to clean up (e.g., your messy Downloads folder)
# Replace this path with your own folder path
TARGET_DIR = os.path.expanduser("~/Downloads")

# Map file extensions to their corresponding destination folders
TRACKED_EXTENSIONS = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
}


def organize_folder():
    # Loop through every item in the target directory
    for item in os.listdir(TARGET_DIR):
        item_path = os.path.join(TARGET_DIR, item)

        # Skip directories; we only want to move files
        if os.path.isdir(item_path):
            continue

        # Extract the file extension and convert to lowercase
        _, extension = os.path.splitext(item)
        extension = extension.lower()

        # Find the correct category folder for the extension
        for folder_name, extensions_list in TRACKED_EXTENSIONS.items():
            if extension in extensions_list:
                # Construct the path to the sub-folder
                destination_folder = os.path.join(TARGET_DIR, folder_name)

                # Create the category folder if it doesn't exist yet
                os.makedirs(destination_folder, exist_ok=True)

                # Move the file into its new folder
                shutil.move(item_path, destination_folder)
                print(f"Moved: {item} -> {folder_name}/")
                break


if __name__ == "__main__":
    print(f"Scanning and cleaning up: {TARGET_DIR}...")
    organize_folder()
    print("Cleanup complete!")
