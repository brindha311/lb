from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Todo Need to change in a way it should trigger main funtion if files enter sources
class CSVHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        # Check if the created file is a CSV file
        if event.src_path.lower().endswith('.csv'):
            print(f"New CSV file detected: {event.src_path}")


def watch_directory(directory_path):
    event_handler = CSVHandler()
    observer = Observer()
    observer.schedule(event_handler, path=directory_path, recursive=False)
    observer.start()

    try:
        print(f"Watching directory: {directory_path}")
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

