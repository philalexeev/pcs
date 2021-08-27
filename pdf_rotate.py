from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

src_path = Path.cwd() / "pdffiles" / "practice_files" / "ugly.pdf"

pdf_reader = PdfFileReader(str(src_path))
pdf_writer = PdfFileWriter()

for pageNumber in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(pageNumber)
    if (pageNumber % 2 == 0):
        page.rotateClockwise(90)
    pdf_writer.addPage(page)

with (src_path / "../ugly_rotated.pdf").open(mode="wb") as out_file:
    pdf_writer.write(out_file)
