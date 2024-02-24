import os
from datetime import datetime
from pypdf import PdfMerger

print('PDF MERGING SCRIPT')

os.chdir('sources')
PDFs = [f for f in os.listdir() if f.endswith('.pdf') or f.endswith('.PDF')]
PDFs.sort()
print('\nFound {} PDF documents from "sources".'.format(len(PDFs)))

merger = PdfMerger()
for PDF in PDFs:
	merger.append(PDF)
	print('    ' + PDF)

useCustomMetaData = (input('\nUse custom meta data? (Y/N) ').upper() == 'Y')
if useCustomMetaData:
	author = input('    Author: ')
	title = input('    Title: ')
	subject = input('    Subject: ')
	keywords = input('    Keywords: ')
	merger.add_metadata({
		'/Author': author,
		'/Title': title,
		'/Subject': subject,
		'/Keywords': keywords,
		'/Producer': 'Python'
	})
else:
	merger.add_metadata({
		'/Producer': 'Python'
	})

print('\nSaving file…')
os.chdir('..')
now = datetime.now()
dt_string = datetime.now().strftime('%Y%m%d_%H%M%S')
merger.write(dt_string + ' Merged document.pdf')
merger.close()
print('All done!')
