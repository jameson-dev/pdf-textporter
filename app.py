import io
import os.path
from pypdf import PdfReader, PdfWriter
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont

from sqlite import monitor_db

# Constants
# TODO - Config file!
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_TEMPLATE = os.path.join(ROOT_DIR, "template.pdf")
PDF_OUTPUT = os.path.join(ROOT_DIR, "output.pdf")       # TODO - Timestamp generated PDFs
FONT_PATH = os.path.join(ROOT_DIR, "fonts")
DEFAULT_FONT = "Consolas"
DISPLAYED_STRING = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor".upper()


def register_font(font_name: str, font_path: str) -> None:
    full_path = os.path.join(font_path, f"{font_name}.ttf")
    try:
        pdfmetrics.registerFont(TTFont(font_name, full_path))
    except Exception as e:
        raise ValueError(f"Unable to register font '{font_name}' at {full_path}: {e}")


def create_temp_pdf(string, font) -> io.BytesIO:
    # Create temporary PDF
    packet = io.BytesIO()

    doc = SimpleDocTemplate(filename=packet, pagesize=A4)

    # Instantiate styling class
    style = ParagraphStyle(
        name="Default",
        fontName=font,
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

    return packet


def overlay_pdfs(overlay_pdf, template_pdf, pdf_name):
    new_pdf = PdfReader(overlay_pdf)

    # Read existing template PDF
    with open(template_pdf, "rb") as f:
        existing_pdf = PdfReader(f)
        output = PdfWriter()

    # Overlay new PDF onto template PDF
    page = existing_pdf.get_page(0)
    page.merge_page(new_pdf.get_page(0))
    output.add_page(page)

    # Save output to a file
    with open(pdf_name, "wb") as output_stream:
        output.write(output_stream)


def main():
    monitor_db("messages")

    # TO BE MOVED TO ANOTHER MODULE

    # # Register custom font
    # register_font(text_font, FONT_PATH)
    #
    # # Create temporary PDF with desired string
    # temp_pdf = create_temp_pdf(displayed_string, text_font)
    #
    # # Overlay PDFs
    # overlay_pdfs(temp_pdf, PDF_PATH, pdf_output_name)


if __name__ == "__main__":
    main()
