import os
import time

TARGET_DIR = "./downloads"
DAYS_LIMIT = 30
NOW = time.time()
SECONDS_IN_DAY = 86400

for file_name in os.listdir(TARGET_DIR):
    file_path = os.path.join(TARGET_DIR, file_name)
    if os.path.isfile(file_path):
        file_age = NOW - os.path.getmtime(file_path)
        if file_age > (DAYS_LIMIT * SECONDS_IN_DAY):
            os.remove(file_path)
