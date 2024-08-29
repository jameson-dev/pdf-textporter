import multiprocessing
import os.path
from multiprocessing import Process
from loguru import logger
from config import create_config
from config import read_config

from sqlite import monitor_db

from file_watchdog import Watcher

# Constants - Hardcoded until they can't be
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(ROOT_DIR, "fonts")
DEFAULT_FONT = "Consolas"


def main():
    try:

        logger.info("\n--------------------\n"
                    "Starting Tasking Sheets application..."
                    "\n--------------------"
                    "\n"
                    )

        logger.info("Loading configuration file...")
        if not os.path.isfile('config.ini'):
            logger.warning("Config file not found. Creating one now...")
            create_config()

        config_values = read_config()

        logger.info("Starting SQLite database monitoring...")
        monitor_db(config_values['db_table'])
    except Exception as e:
        logger.error(f"An error occurred: {e}")


def watchdog():
    w = Watcher()
    w.run()


if __name__ == "__main__":
    # Pyinstaller fix for multiprocessing
    multiprocessing.freeze_support()
    try:
        process1 = Process(target=main)
        process1.start()
        process2 = Process(target=watchdog)
        process2.start()
    except Exception as e:
        logger.error(f"Error starting process: {e}.")

    # Keep console window open on error
    input()
