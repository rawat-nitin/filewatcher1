import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
    DIRECTORY_TO_WATCH = "."

    def __init__(self):
        self.event_handler = Handler()
        self.observer = Observer()

    def run(self):
        self.observer.schedule(self.event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        print(f"🔥 Watching for changes in: {self.DIRECTORY_TO_WATCH}")

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("🛑 Stopping watcher...")
            self.observer.stop()

        self.observer.join()


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"🔄 File modified: {event.src_path}")

    def on_created(self, event):
        print(f"➕ New file created: {event.src_path}")

    def on_deleted(self, event):
        print(f"❌ File deleted: {event.src_path}")


if __name__ == "__main__":
    w = Watcher()
    w.run()
