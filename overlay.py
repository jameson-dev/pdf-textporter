from pypdf import PdfReader, PdfWriter
from loguru import logger
from print_pdf import print_pdf


def overlay_pdfs(overlay_pdf, template_pdf, pdf_name):
    try:
        # Debugging: Print the number of pages in overlay PDF
        if overlay_pdf.getvalue():
            logger.debug(f"Overlay PDF stream contains data: {overlay_pdf.getvalue()}")
        else:
            logger.error("Overlay PDF stream is empty. There is an issue.")

        new_pdf = PdfReader(overlay_pdf)

        # Debugging: Print the number of pages in the overlay PDF
        logger.debug(f"Number of pages in overlay PDF: {len(new_pdf.pages)}")

        # Read existing template PDF
        with open(template_pdf, "rb") as f:
            existing_pdf = PdfReader(f)

            # Ensure both PDFs have at least one page
            if len(new_pdf.pages) < 1:
                raise ValueError("Overlay PDF does not have any pages.")
            if len(existing_pdf.pages) < 1:
                raise ValueError("Template PDF does not have any pages.")

            output = PdfWriter()

            # Overlay new PDF onto template PDF
            page = existing_pdf.get_page(0)
            page.merge_page(new_pdf.get_page(0))
            output.add_page(page)

        # Save output to a file
        with open(pdf_name, "wb") as output_stream:
            output.write(output_stream)
            logger.info(f"PDF created at {pdf_name}")

        # Print PDF
        print_pdf(pdf_name)

    except Exception as e:
        logger.error(f"Unable to overlay PDF: {e}")
