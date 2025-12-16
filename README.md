This program:
✅ Watches a directory (. = current folder)
✅ Detects file changes (create/modify/delete)
✅ Prints a message when something changes
✅ Keeps running until you press Ctrl + C

It uses the watchdog library to listen to filesystem events.

**Import Section**
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

time ➡️️ used to pause the program so it does not exit.
observer ➡️️ watches the filesystem for changes
FileSystemEventHandler ➡️️ base class to handle file events
