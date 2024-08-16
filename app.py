import io
import os.path

from pypdf import PdfReader, PdfWriter
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont

font_dir_name = "fonts/"
text_font = "Consolas"
pdf_template_name = "template.pdf"
pdf_output_name = "output.pdf"
displayed_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor".upper()


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(ROOT_DIR, pdf_template_name)
FONT_PATH = os.path.join(ROOT_DIR, font_dir_name)


def register_font(font, path) -> None:
    pdfmetrics.registerFont(TTFont(font, path + f"{text_font}.ttf"))


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


def overlay_pdfs(overlay_pdf, template_pdf, pdf_name ):
    new_pdf = PdfReader(overlay_pdf)

    # Read existing template PDF
    existing_pdf = PdfReader(open(template_pdf, "rb"))
    output = PdfWriter()

    # Overlay new PDF onto template PDF
    page = existing_pdf.get_page(0)
    page.merge_page(new_pdf.get_page(0))
    output.add_page(page)

    # Save output to a file
    output_stream = open(pdf_name, "wb")
    output.write(output_stream)
    output_stream.close()


def main():

    # Register custom font
    register_font(text_font, FONT_PATH)

    # Create temporary PDF with desired string
    temp_pdf = create_temp_pdf(displayed_string, text_font)

    # Overlay PDFs
    overlay_pdfs(temp_pdf, PDF_PATH, pdf_output_name)


if __name__ == "__main__":
    main()
