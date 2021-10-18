import PyPDF2

src = PyPDF2.PdfFileReader(open("file3.pdf", "rb"))
watermark = PyPDF2.PdfFileReader(open("template.pdf", "rb"))
output_obj = PyPDF2.PdfFileWriter()

for i in range(src.getNumPages()):
	page = src.getPage(i)
	page.mergePage(watermark.getPage(0))
	output_obj.addPage(page)

with open("watermarked.pdf",'wb') as file:
	output_obj.write(file)