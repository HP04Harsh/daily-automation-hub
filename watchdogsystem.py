# pip install watchdog

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 1. Define the folder you want to watch in real-time
WATCH_FOLDER = r"C:\Users\YourUsername\Downloads"

# 2. Define what happens when a file is created
class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Ignore folder creation, look for files only
        if not event.is_directory:
            print(f"🔥 ALERT: New file detected -> {event.src_path}")

# 3. Set up the folder watcher
if __name__ == "__main__":
    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_FOLDER, recursive=False)
    
    print(f"👀 Monitoring folder: {WATCH_FOLDER}\nPress Ctrl+C to stop.")
    observer.start()

    try:
        while True:
            time.sleep(1)  # Keeps the script running in the background
    except KeyboardInterrupt:
        observer.stop()
        print("\nStopping monitor...")
    
    observer.join()