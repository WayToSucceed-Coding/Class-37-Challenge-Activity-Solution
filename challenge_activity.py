from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from datetime import datetime

log_file = "spy_log.txt"

f= open(log_file, "a")
f.write(f"=== Folder Spy Log Started ===\n")
f.write(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
f.close()

class SpyHandler(FileSystemEventHandler):
    
    def on_created(self, event):
        self.log_event("Created", event.src_path)
        print(f"Created: {event.src_path}")

    def on_deleted(self, event):
        self.log_event("Deleted", event.src_path)
        print(f"Deleted: {event.src_path}")
    
    def on_modified(self, event):
        self.log_event("Modified", event.src_path)
        print(f"Modified: {event.src_path}")

    def on_moved(self, event):
        self.log_event("Moved", event.src_path)
        print(f"Moved: {event.src_path} to {event.dest_path}")
    
    def on_any_event(self, event):
        print("Hey! Something happened!")

    def log_event(self, event_type, path):
        f= open(log_file, "a")
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} EVENT : {event_type} | PATH: {path}\n")
        f.close()

spy_handler = SpyHandler() 

spy = Observer()

folder_to_watch = "C:/Users/LENOVO/Desktop/SpyFolder"

spy.schedule(spy_handler, folder_to_watch, recursive=True)

spy.start()

print(f"Spy started spying on {folder_to_watch}...")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    spy.stop()
    print("Spy stopped spying.")






