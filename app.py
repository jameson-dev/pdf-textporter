import io
import os.path


from register_font import register_font
from generate_pdf import create_temp_pdf
from overlay import overlay_pdfs


from sqlite import monitor_db

# Constants
# TODO - Config file!
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_TEMPLATE = os.path.join(ROOT_DIR, "template.pdf")
PDF_OUTPUT = os.path.join(ROOT_DIR, "output.pdf")       # TODO - Timestamp generated PDFs
FONT_PATH = os.path.join(ROOT_DIR, "fonts")
DEFAULT_FONT = "Consolas"
DISPLAYED_STRING = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor".upper()


def main():
    monitor_db("messages")

    register_font(DEFAULT_FONT, FONT_PATH)
    create_temp_pdf(DISPLAYED_STRING, DEFAULT_FONT)
    overlay_pdfs(create_temp_pdf, PDF_TEMPLATE, PDF_OUTPUT)


if __name__ == "__main__":
    main()
