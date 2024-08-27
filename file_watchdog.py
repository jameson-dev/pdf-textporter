import os.path
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from loguru import logger
from config import read_config

config_values = read_config()


class Watcher:
    WATCHDOG_DIR = config_values['msgs_path']

    def __init__(self):
        self.observer = Observer()

    def run(self):
        if not os.path.isdir(self.WATCHDOG_DIR):
            logger.warning(f"{self.WATCHDOG_DIR} directory does not exist. Creating it now...")
            os.mkdir(self.WATCHDOG_DIR)
        try:
            event_handler = Handler()
            self.observer.schedule(event_handler, self.WATCHDOG_DIR, recursive=False)
            self.observer.start()
        except FileNotFoundError as e:
            logger.error(f"An error occurred: {e}")

        try:
            while True:
                time.sleep(5)
        except Exception as e:
            self.observer.stop()
            logger.error(f"Error starting watchdog: {e}")

        self.observer.join()


class Handler(FileSystemEventHandler):
    def on_any_event(self, event) -> None:
        if event.is_directory:
            return None
        elif event.event_type == 'created' and event.src_path.endswith(".log"):
            logger.debug("File created - %s." % event.src_path)
            # TODO - Work the magic here!
