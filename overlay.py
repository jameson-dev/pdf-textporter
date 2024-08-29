from pypdf import PdfReader, PdfWriter
from loguru import logger


def overlay_pdfs(overlay_pdf, template_pdf, pdf_name):
    try:
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
            logger.info("PDF created")
    except Exception as e:
        logger.error(f"Unable to overlay PDF: {e}")
