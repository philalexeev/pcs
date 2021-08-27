from pathlib import Path
from PyPDF2 import PdfFileMerger

pdf_merger = PdfFileMerger()
reports_dir = Path.cwd() / "pdffiles" / "practice_files" / "expense_reports"
expence_reports = list(reports_dir.glob('*.pdf'))
expence_reports.sort()

for path in expence_reports:
    pdf_merger.append(str(path))

out_path = reports_dir / "reports.pdf"

table_of_content = Path.cwd() / "pdffiles" / "practice_files" \
    / "quarterly_report" / "toc.pdf"

pdf_merger.merge(0, str(table_of_content))

with Path(out_path).open(mode="wb") as output_file:
    pdf_merger.write(output_file)

