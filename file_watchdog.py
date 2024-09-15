import os.path
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from loguru import logger

from config import read_config
from generate_pdf import create_temp_pdf

config_value = read_config()


class Watcher:
    def __init__(self):
        self.observer = Observer()

    def run(self):
        config_values = read_config()
        watchdog_dir = config_values['msgs_path']
        logger.info(f"Watchdog is now monitoring '{watchdog_dir}'")
        if not os.path.isdir(watchdog_dir):
            logger.warning(f"{watchdog_dir} directory does not exist. Creating it now...")
            os.mkdir(watchdog_dir)
        try:
            event_handler = Handler()
            self.observer.schedule(event_handler, watchdog_dir, recursive=False)
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

            # Must be a delay to ensure log file is written to fully before being read
            time.sleep(config_value['file_read_delay'])
            with open(event.src_path, "r") as f:
                string = f.read().replace("\n", "")
                logger.debug(f"Captured string: {string}")
                create_temp_pdf(string)
