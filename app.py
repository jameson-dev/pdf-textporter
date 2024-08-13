import io
import os.path

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont

font_dir_name = "fonts/"
text_font = "Consolas"
pdf_template_name = "template.pdf"

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(ROOT_DIR, pdf_template_name)
FONT_PATH = os.path.join(ROOT_DIR, font_dir_name)


pdfmetrics.registerFont(TTFont(text_font, FONT_PATH + f"{text_font}.ttf"))

packet = io.BytesIO()
canvas = canvas.Canvas(filename=packet, pagesize=letter)

canvas.setFont(text_font, 15)
canvas.save()

packet.seek(0)
new_pdf = PdfReader(packet)

existing_pdf = PdfReader(open(PDF_PATH, "rb"))
output = PdfWriter()

page = existing_pdf.get_page(0)
page.merge_page(new_pdf.get_page(0))
output.add_page(page)

outputStream = open(pdf_output_name, "wb")
output.write(outputStream)
outputStream.close()
