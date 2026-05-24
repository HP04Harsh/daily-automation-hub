import os
import shutil

for root, dirs, files in os.walk("."):
    if "logs" in dirs:

        log_path = os.path.join(root, "logs")

        # calculate folder size
        size = 0
        for path, d, f in os.walk(log_path):
            for file in f:
                file_path = os.path.join(path, file)
                size += os.path.getsize(file_path)

        print("\nLogs Folder Found:", log_path)
        print("Size:", round(size / (1024 * 1024), 2), "MB")

        choice = input("Delete this folder? (yes/no): ")

        if choice.lower() == "yes":
            shutil.rmtree(log_path)
            print("Folder deleted.")
        else:
            print("Folder kept.")