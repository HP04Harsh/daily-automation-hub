import os

folder = "files"

for count, filename in enumerate(os.listdir(folder), start=1):
    old_path = os.path.join(folder, filename)

    extension = os.path.splitext(filename)[1]
    new_name = f"file_{count}{extension}"

    new_path = os.path.join(folder, new_name)
    os.rename(old_path, new_path)

print("Files renamed successfully!")