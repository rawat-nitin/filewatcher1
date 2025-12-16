### 📂 File Watcher Program (Python)

**This program:**

- ✅ Watches a directory (. = current folder)
- ✅ Detects file changes (create / modify / delete)
- ✅ Prints a message when something changes
- ✅ Keeps running until you press Ctrl + C
  It uses the watchdog library to listen for filesystem events.

### 📦 Import Section

```python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
```

### 🔍 Explanation

**time**

- Used to pause the program so it continues running instead of exiting immediately.
  **Observer**
- Monitors the filesystem and detects changes such as file creation, modification, or deletion.
  **FileSystemEventHandler**
- A base class used to define how the program should respond to filesystem events.
