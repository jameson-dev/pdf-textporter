#!/venv/bin/python

import multiprocessing
import os.path
import sys
from multiprocessing import Process
from loguru import logger
from module_check import load_requirements, check_modules
from config import Config
from sqlite import monitor_db
from file_watchdog import Watcher

# Constants
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = "../logs"
FONT_PATH = os.path.join(ROOT_DIR, "fonts")
DEFAULT_FONT = "Consolas"  # Intentionally the only font allowed.

logger.add(f"{LOG_DIR}/app.log", rotation="12 hours", format="{time} {level} {message}")

config = Config()


def main():
    try:

        logger.info("\n--------------------\n"
                    "Starting Tasking Sheets application..."
                    "\n--------------------"
                    "\n"
                    )

        required_modules = load_requirements()
        missing_modules = check_modules(required_modules)

        if missing_modules:
            logger.error("The following modules are missing or do not have the correct version:")
            logger.error('\n'.join(missing_modules))
            logger.error('Install the required modules using the following command in the apps root directory:')
            logger.error('  pip install -r requirements')
            sys.exit(1)

        config.check_config()
    except Exception as e:
        logger.error(f"An error occurred: {e}")


def watchdog():
    w = Watcher()
    w.run()


def start_monit():

    logger.info("Starting SQLite database monitoring...")
    monitor_db(config.get('Database', "db_table"))


if __name__ == "__main__":
    # Pyinstaller fix for multiprocessing
    multiprocessing.freeze_support()

    try:
        main()
        process2 = Process(target=watchdog)
        process2.start()
        process3 = Process(target=start_monit)
        process3.start()
    except Exception as e:
        logger.error(f"Error starting process: {e}.")
