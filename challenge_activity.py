from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from datetime import datetime

log_file = "spy_log.txt"

with open(log_file, "a") as f:
    f.write(f"=== Folder Spy Log Started ===\n")
    f.write(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

class TheSpy(FileSystemEventHandler):
    
    def on_created(self, event):
        self.log_event("CREATED", event.src_path)
        print(f"Created: {event.src_path}")

    def on_deleted(self, event):
        self.log_event("DELETED", event.src_path)
        print(f"Deleted: {event.src_path}")
    
    def on_modified(self, event):
        self.log_event("MODIFIED", event.src_path)
        print(f"Modified: {event.src_path}")

    def on_moved(self, event):
        self.log_event("MOVED", event.src_path)
        print(f"Moved: {event.src_path} to {event.dest_path}")
    
    def on_any_event(self, event):
        print("Hey! Something happened!")

    def log_event(self, event_type, path):
        with open(log_file, "a") as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} EVENT : {event_type} | PATH: {path}\n")

spy = TheSpy() 

observer = Observer()

folder_to_watch = "C:/Users/LENOVO/Desktop/SpyFolder"

observer.schedule(spy, folder_to_watch, recursive=True)

observer.start()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()
    print("Spy stopped spying.")






