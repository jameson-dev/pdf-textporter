import io
import os.path

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

PDF_PATH = os.path.join(ROOT_DIR, 'test-doc.pdf')
FONT_PATH = os.path.join(ROOT_DIR, 'fonts/')


packet = io.BytesIO()

canvas = canvas.Canvas(packet, pagesize=letter)
pdfmetrics.registerFont(TTFont("Consolas", FONT_PATH + "Consolas.ttf"))
canvas.setFont("Consolas", 15)
canvas.drawString(10, 100, "CFSRES: INC:S0923 ROAD CRASH RESCUE")
canvas.save()

packet.seek(0)
new_pdf = PdfReader(packet)

existing_pdf = PdfReader(open(PDF_PATH, "rb"))
output = PdfWriter()

page = existing_pdf.get_page(0)
page.merge_page(new_pdf.get_page(0))
output.add_page(page)

outputStream = open("final-pdf.pdf", "wb")
output.write(outputStream)
outputStream.close()
