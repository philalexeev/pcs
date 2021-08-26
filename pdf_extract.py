from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = Path('./pdffiles/practice_files/Pride_and_Prejudice.pdf')
pdf_file = PdfFileReader(str(pdf_path))
pdf_page = pdf_file.getPage(0)

pdf_writer = PdfFileWriter()
pdf_writer.addPage(pdf_page)

with Path('./pdffiles/papfirst.pdf').open(mode="wb") as output_file:
    pdf_writer.write(output_file)

