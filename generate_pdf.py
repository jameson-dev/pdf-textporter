import os
import io
from datetime import datetime

from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, BaseDocTemplate, Frame, PageTemplate, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import black
from loguru import logger
from register_font import register_font
from overlay import overlay_pdfs


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_TEMPLATE = os.path.join(ROOT_DIR, "template.pdf")
FONT_PATH = os.path.join(ROOT_DIR, "fonts")
FONT_NAME = "Consolas"


class CustomDocTemplate(BaseDocTemplate):
    def __init__(self, filename, **kwargs):
        super().__init__(filename, **kwargs)

        # Define margins and frame dimensions
        # TODO - Add values to config
        left_margin = cm - 10
        right_margin = cm - 20
        top_margin = 2 * cm  # Adjust top margin as needed
        bottom_margin = 9.75 * inch  # Adjust bottom margin as needed

        # Frame dimensions
        frame_width = A4[0] - left_margin - right_margin
        frame_height = A4[1] - top_margin - bottom_margin

        # Centered Frame Positioning
        x1 = left_margin
        y1 = A4[1] - top_margin

        self.frame = Frame(
            x1=x1,
            y1=y1 - frame_height,
            width=frame_width,
            height=frame_height,
            showBoundary=0  # To use when debugging
        )

    def build(self, flowables, filename=None, canvasmaker=canvas.Canvas):
        self.addPageTemplates([self.createPageTemplate()])
        super().build(flowables)


    def createPageTemplate(self):
        return PageTemplate(id='frame_template', frames=[self.frame])


def create_temp_pdf(string: str) -> None:
    try:
        print(f"string: {string}")
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

        doc = CustomDocTemplate(filename=packet, pagesize=A4)

        # Instantiate styling class
        style = ParagraphStyle(
            name="Default",
            fontName="Consolas",
            fontSize=13,
            leading=15,
            alignment=0
        )

        # Paragraph parameters
        para_pager = Paragraph(string, style=style)

        flowables = [para_pager, Spacer(1, 12)]

        # Build the document with a Frame
        logger.debug("Building PDF document...")
        doc.build(flowables)

        # Build the new PDF we'll be using
        packet.seek(0)
        if not packet.getvalue():
            logger.error("PDF Stream is empty after building.")
            return
        else:
            logger.debug("PDF Stream has data")

        # Debugging output
        logger.debug(f"PDF Template Path: {PDF_TEMPLATE}")
        logger.debug(f"Output PDF Path: {pdf_output}")

        overlay_pdfs(packet, PDF_TEMPLATE, pdf_output)
    except Exception as e:
        logger.error(f"Error creating temporary PDF: {e}")
