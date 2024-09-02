import os
import io
from datetime import datetime

from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from loguru import logger
from register_font import register_font
from overlay import overlay_pdfs


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_TEMPLATE = os.path.join(ROOT_DIR, "template.pdf")
FONT_PATH = os.path.join(ROOT_DIR, "fonts")
FONT_NAME = "Consolas"


def create_temp_pdf(string: str) -> None:
    try:
        logger.debug("Registering font...")
        register_font(FONT_NAME, font_path=FONT_PATH)

        # Create temporary PDF
        logger.debug("Generating PDF in memory as binary string")
        packet = io.BytesIO()

        # Timestamp generated PDF files
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        pdf_output = os.path.join(ROOT_DIR, f"output_{timestamp}.pdf")

        # Increment file names if there is more than one file with the same timestamp
        counter = 1
        while os.path.exists(pdf_output):
            pdf_output = os.path.join(pdf_output, f"output_{timestamp}_{counter}.pdf")
            counter += 1

        doc = SimpleDocTemplate(filename=packet, pagesize=A4)

        # Instantiate styling class
        style = ParagraphStyle(
            name="Default",
            fontName="Consolas",
            fontSize=13,
            borderColor="#000000",
            borderWidth=1,
            leading=15,
            borderPadding=20
        )

        # Paragraph parameters
        para_pager = Paragraph(string, style=style)

        # Create a vertical spacer
        top_spacer = Spacer(0, 50)

        # Build the document with specified flowables
        logger.debug("Building PDF document...")
        doc.build([top_spacer, para_pager])

        # Build the new PDF we'll be using
        packet.seek(0)

        overlay_pdfs(packet, PDF_TEMPLATE, pdf_output)
    except Exception as e:
        logger.error(f"Error creating temporary PDF: {e}")
