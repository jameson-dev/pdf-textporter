import io
import os.path
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import FreeText
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

PDF_PATH = os.path.join(ROOT_DIR, 'test-doc.pdf')
FONT_PATH = os.path.join(ROOT_DIR, 'fonts/')


packet = io.BytesIO()

canvas = canvas.Canvas(packet, pagesize=letter)
canvas.drawString(10, 100, "CFSRES: INC:S0923 ROAD CRASH RESCUE")
canvas.save()

packet.seek(0)
new_pdf = PdfReader(packet)

existing_pdf = PdfReader(open(pdf_path, "rb"))
existing_pdf = PdfReader(open(PDF_PATH, "rb"))
output = PdfWriter()

page = existing_pdf.get_page(0)
page.merge_page(new_pdf.get_page(0))
output.add_page(page)

outputStream = open("final-pdf.pdf", "wb")
output.write(outputStream)
outputStream.close()
