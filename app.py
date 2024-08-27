import multiprocessing
import os.path

from register_font import register_font
from generate_pdf import create_temp_pdf
from overlay import overlay_pdfs
from multiprocessing import Process
from loguru import logger

from sqlite import monitor_db

from file_watchdog import Watcher

# Constants
# TODO - Config file!
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_TEMPLATE = os.path.join(ROOT_DIR, "template.pdf")
PDF_OUTPUT = os.path.join(ROOT_DIR, "output.pdf")       # TODO - Timestamp generated PDFs
FONT_PATH = os.path.join(ROOT_DIR, "fonts")
DEFAULT_FONT = "Consolas"
DISPLAYED_STRING = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor".upper()


def main():
    try:

        logger.info("\n--------------------\n"
                    "Starting Tasking Sheets application..."
                    "\n--------------------"
                    "\n"
                    )

        logger.info("Registering font(s)...")
        register_font(DEFAULT_FONT, FONT_PATH)

        logger.info("Starting SQLite database monitoring...")
        monitor_db("messages")

        # TODO - To be moved when ready
        # logging.info("Generating temporary PDF...")
        # create_temp_pdf(DISPLAYED_STRING, DEFAULT_FONT)
        #
        # logging.info(f"Overlaying PDFs and saving to {PDF_OUTPUT}...")
        # overlay_pdfs(create_temp_pdf, PDF_TEMPLATE, PDF_OUTPUT)
        #
        # logging.info(f"PDF ({PDF_OUTPUT}) has been generated.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


def watchdog():
    w = Watcher()
    w.run()


if __name__ == "__main__":
    # Pyinstaller fix for multiprocessing
    multiprocessing.freeze_support()
    try:
        process1 = Process(target=watchdog)
        process1.start()
        process2 = Process(target=main)
        process2.start()
    except Exception as e:
        logger.error(f"Error starting process: {e}.")

    # Keep console window open on error
    input()
