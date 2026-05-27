import os
import shutil
import tempfile

temp_dir = tempfile.gettempdir()

for item in os.listdir(temp_dir):
    path = os.path.join(temp_dir, item)

    try:
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
        elif os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)
    except:
        pass

print("Temp files cleaned successfully.")~