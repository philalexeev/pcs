from PyPDF2 import PdfFileWriter
from pathlib import Path

pdf_writer = PdfFileWriter()
pdf_writer.addBlankPage(width=80, height=80)

with Path('./pdffiles/blank.pdf').open(mode="wb") as output_file:
    pdf_writer.write(output_file)
