import io
import os.path

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
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

# Register custom font (Consolas) to ReportLib
pdfmetrics.registerFont(TTFont(text_font, FONT_PATH + f"{text_font}.ttf"))

# Create temporary PDF
packet = io.BytesIO()
canvas = canvas.Canvas(filename=packet, pagesize=A4)

# Set string parameters and save
canvas.setFont(text_font, 15)
canvas.drawString(10, 100, displayed_string)
canvas.save()

# Create new PDF
packet.seek(0)
new_pdf = PdfReader(packet)

# Read PDF template
existing_pdf = PdfReader(open(PDF_PATH, "rb"))
output = PdfWriter()

# Overlay string onto to template PDF
page = existing_pdf.get_page(0)
page.merge_page(new_pdf.get_page(0))
output.add_page(page)

# Save output to a file
outputStream = open(pdf_output_name, "wb")
output.write(outputStream)
outputStream.close()
