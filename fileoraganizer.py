import os
import shutil

target_directory = os.path.expanduser("~/Downloads")

if os.path.exists(target_directory):
    for filename in os.listdir(target_directory):
        file_path = os.path.join(target_directory, filename)
        
        if os.path.isfile(file_path):
            file_extension = filename.split(".")[-1].upper()
            
            if len(filename.split(".")) > 1:
                destination_folder = os.path.join(target_directory, file_extension)
                
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                
                shutil.move(file_path, os.path.join(destination_folder, filename))