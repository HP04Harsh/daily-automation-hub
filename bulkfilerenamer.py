import os

# Define the folder path and the naming changes
folder_path = "C:/Users/YourUsername/Desktop/MyFolder"
old_phrase = "draft"
new_phrase = "final"

# Loop through every file in the directory
for filename in os.listdir(folder_path):
    if old_phrase in filename:
        # Create the new filename
        new_filename = filename.replace(old_phrase, new_phrase)
        
        # Get full absolute paths
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed: {filename} -> {new_filename}")
