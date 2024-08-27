import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from loguru import logger


def register_font(font_name: str, font_path: str) -> None:
    full_path = os.path.join(font_path, f"{font_name}.tftf")
    try:
        pdfmetrics.registerFont(TTFont(font_name, full_path))
    except Exception as e:
        logger.error(f"Unable to register font: {e}")
