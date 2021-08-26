from PyPDF2 import PdfFileReader
from pathlib import Path

pdf_path = Path.cwd() / "pdffiles" / "practice_files" / "Pride_and_Prejudice.pdf"
pdf = PdfFileReader(str(pdf_path))

# # get number of pages in pdf file
# print(pdf.getNumPages())

# # get pdf info
# print(pdf.documentInfo)
# print(pdf.documentInfo.producer)

# first_page = pdf.getPage(0)
# print()
# print(first_page.extractText())

output_path = Path.cwd() / "pdffiles" / "practice_files" \
/ "Pride_and_Prejudice.txt"

with output_path.open(mode="w") as outfile:
    title = pdf.documentInfo.title
    num_pages = pdf.getNumPages()
    outfile.write(f"{title}\nNumber of pages: {num_pages}\n\n")

    for page in pdf.pages:
        text = page.extractText()
        outfile.write(text)

