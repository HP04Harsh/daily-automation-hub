import os

folder_path = "C:/Users/YourName/Documents/files"

for count, filename in enumerate(os.listdir(folder_path), start=1):
    extension = os.path.splitext(filename)[1]
    new_name = f"file_{count}{extension}"

    src = os.path.join(folder_path, filename)
    dst = os.path.join(folder_path, new_name)

    os.rename(src, dst)

print("Files renamed successfully!")