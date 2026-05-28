import os
import shutil

usage = shutil.disk_usage("/").used / shutil.disk_usage("/").total * 100

if usage > 80:
    os.system("sudo apt clean -y")
    os.system("sudo journalctl --vacuum-time=7d")
    print("Disk cleaned")

for root, dirs, files in os.walk("/var/log"):
    for file in files:
        path = os.path.join(root, file)

        try:
            if os.path.getsize(path) > 50 * 1024 * 1024:
                os.system(f"sudo truncate -s 0 {path}")
                print(f"Cleaned: {path}")
        except:
            pass