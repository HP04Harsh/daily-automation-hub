import psutil
import time

PROCESS_NAME = "notepad.exe"  # Change to your process name

def is_process_running(process_name):
    for process in psutil.process_iter(['name']):
        try:
            if process.info['name'].lower() == process_name.lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return False

while True:
    if is_process_running(PROCESS_NAME):
        print(f"[ACTIVE] {PROCESS_NAME} is running")
    else:
        print(f"[INACTIVE] {PROCESS_NAME} is not running")

    time.sleep(5)  # Check every 5 seconds