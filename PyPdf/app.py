import PyPDF2

with open("PyPdf/first.pdf", "rb") as file:
  reader = PyPDF2.PdfFileReader(file)
  print(reader.numPages)
  page = reader.getPage(0)
  page.rotateClockwise(90)
  writer = PyPDF2.PdfFileWriter()
  writer.addPage(page)

with open("PyPdf/rotated.pdf", "wb") as output:
  writer.write(output)

merger = PyPDF2.PdfFileMerger()
file_names = ['PyPdf/first.pdf', 'PyPdf/second.pdf']
for file_name in file_names:
  merger.append(file_name)
merger.write("PyPdf/combined.pdf")