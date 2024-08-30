import os
import subprocess
from loguru import logger
from config import read_config

config_values = read_config()


def print_pdf(pdf_name):
    try:
        sumatra_path = config_values['sumatra_path']
        logger.debug(f"PDF install path set to '{sumatra_path}'")

        logger.debug("Sending PDF to printer...")
        print_cmd = f'"{sumatra_path}" -print-to-default "{pdf_name}"'

        subprocess.run(print_cmd, shell=True, check=True)
        logger.info("PDF has been sent to the printer")
    except Exception as e:
        logger.error(f"Failed to print: {e}")
