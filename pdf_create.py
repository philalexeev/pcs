from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import LETTER

canvas = Canvas("./pdffiles/practice_files/hello.pdf", pagesize=LETTER)

canvas.setFont("Courier", 20)
canvas.drawString(72, 72, "hello, this is jackass and let's get started")
canvas.save()

# full guide https://www.reportlab.com/docs/reportlab-userguide.pdf
