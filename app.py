#!/venv/bin/python

import multiprocessing
import os.path
from multiprocessing import Process
from loguru import logger
from config import create_config
from config import read_config

from sqlite import monitor_db

from file_watchdog import Watcher

# Constants
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(ROOT_DIR, "fonts")
DEFAULT_FONT = "Consolas"  # Intentionally the only font allowed.


def check_config():
    logger.info("Loading configuration file...")
    if not os.path.isfile('config.ini'):
        logger.warning("Config file not found. Creating one now...")
        create_config()


def main():
    try:

        logger.info("\n--------------------\n"
                    "Starting Tasking Sheets application..."
                    "\n--------------------"
                    "\n"
                    )
    except Exception as e:
        logger.error(f"An error occurred: {e}")


def watchdog():
    w = Watcher()
    w.run()


def start_monit():
    config_values = read_config()

    logger.info("Starting SQLite database monitoring...")
    monitor_db(config_values['db_table'])


if __name__ == "__main__":
    # Pyinstaller fix for multiprocessing
    multiprocessing.freeze_support()

    try:
        process1 = Process(target=check_config)
        process1.start()
        process1.join()
        process2 = Process(target=watchdog)
        process2.start()
        process3 = Process(target=start_monit)
        process3.start()
    except Exception as e:
        logger.error(f"Error starting process: {e}.")

    # Keep console window open on error
    input()
