import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from loguru import logger


def register_font(font_name: str, font_path: str) -> None:
    full_path = os.path.join(font_path, f"{font_name}.ttf")
    try:
        logger.debug(f"Registering font at {full_path}")
        pdfmetrics.registerFont(TTFont(font_name, full_path))
        logger.info(f"Font '{font_name}' has been registered")
    except Exception as e:
        logger.warning(f"Unable to register font: {e}")
        logger.info("Falling back to default font...")
