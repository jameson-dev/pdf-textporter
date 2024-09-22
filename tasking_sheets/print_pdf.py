import subprocess
from loguru import logger
from config import Config

config = Config()

printer_name = config.get('General', 'cups_printer_name')


def print_pdf(pdf_name):
    try:
        logger.debug(f"Sending PDF to '{printer_name}' printer...")
        print_cmd = f'lp -d {printer_name} {pdf_name}'
        subprocess.run(print_cmd, shell=True, check=True)
        logger.info("PDF has been sent to the printer")
    except Exception as e:
        logger.error(f"Failed to print: {e}")
