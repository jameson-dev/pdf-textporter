import os.path
import logging
import time

from register_font import register_font
from generate_pdf import create_temp_pdf
from overlay import overlay_pdfs

from sqlite import monitor_db

# Constants
# TODO - Config file!
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_TEMPLATE = os.path.join(ROOT_DIR, "template.pdf")
PDF_OUTPUT = os.path.join(ROOT_DIR, "output.pdf")       # TODO - Timestamp generated PDFs
FONT_PATH = os.path.join(ROOT_DIR, "fonts")
DEFAULT_FONT = "Consolas"
DISPLAYED_STRING = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor".upper()


def init_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def main():
    init_logging()

    try:
        logging.info("Starting SQLite database monitoring...")
        monitor_db("messages")

        logging.info("Registering font(s)...")
        register_font(DEFAULT_FONT, FONT_PATH)

        logging.info("Generating temporary PDF...")
        create_temp_pdf(DISPLAYED_STRING, DEFAULT_FONT)

        logging.info(f"Overlaying PDFs and saving to {PDF_OUTPUT}...")
        overlay_pdfs(create_temp_pdf, PDF_TEMPLATE, PDF_OUTPUT)

        logging.info(f"PDF ({PDF_OUTPUT}) has been generated.")
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)


def watchdog():
    w = Watcher()
    w.run()


if __name__ == "__main__":
    main()
