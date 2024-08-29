import io
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from loguru import logger


def create_temp_pdf(string, font) -> io.BytesIO:
    # Create temporary PDF
    packet = io.BytesIO()

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
    doc.build([top_spacer, para_pager])

    # Build the new PDF we'll be using
    packet.seek(0)

    overlay_pdfs(packet, PDF_TEMPLATE, PDF_OUTPUT)

