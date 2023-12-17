import os
from datetime import datetime
from pypdf import PdfMerger

os.chdir('sources')
PDFs = [f for f in os.listdir() if f.endswith('.pdf') or f.endswith('.PDF')]
PDFs.sort()

merger = PdfMerger()
for PDF in PDFs:
	merger.append(PDF)

os.chdir('..')
now = datetime.now()
dt_string = datetime.now().strftime('%Y%m%d_%H%M%S')
merger.write(dt_string + ' Merged document.pdf')
merger.close()
