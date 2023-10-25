import re
import time
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from corpus_content.utils.formatter import update_content

DECISIONS_DIR = Path().home().joinpath("code/corpus-decisions")


class Watcher:
    def __init__(self, directory=".", handler=FileSystemEventHandler()):
        self.observer = Observer()
        self.handler = handler
        self.directory = directory

    def run(self):
        self.observer.schedule(self.handler, self.directory, recursive=True)
        self.observer.start()
        print("\nWatcher Running in {}/\n".format(self.directory))
        try:
            while True:
                time.sleep(1)
        except Exception:
            self.observer.stop()
        self.observer.join()
        print("\nWatcher Terminated\n")


class MyHandler(FileSystemEventHandler):
    file_cache: dict = {}

    def on_modified(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith("README.md"):
            print("Ignoring change to readme.md")
            return
        elif event.src_path.endswith("HEADINGS.md"):
            print("Ignoring change to headings.md")
            return
        elif event.src_path.endswith(".md"):
            seconds = int(time.time())
            key = (seconds, event.src_path)
            if key in self.file_cache:
                return
            self.file_cache[key] = True
            p = Path(event.src_path)
            print(f"\nUpdating: {p.name=}")
            to_check = update_content(file=p)
            for text in to_check:
                print(f"\nCheck {text=}\n")
            if not to_check:
                print(f"Cleared: {p.name=}\n\n")

    def on_any_event(self, event):
        print(event)  # Your code here


if __name__ == "__main__":
    w = Watcher(str(DECISIONS_DIR), MyHandler())
    w.run()
