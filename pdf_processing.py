import PyPDF2

with open('file1.pdf', 'rb') as file:
	reader_obj = PyPDF2.PdfFileReader(file)
	page = reader_obj.getPage(0)
	print(f"Total no.of pages: {reader_obj.numPages}")
	page.rotateClockwise(180)

	writer_obj = PyPDF2.PdfFileWriter()
	writer_obj.addPage(page)
	with open('rotated_file.pdf', 'wb') as out_file:
		writer_obj.write(out_file)

	password = "pass123"
	writer_obj.encrypt(password)

"""
	1. getPage(index) - fetch page at index.
	2. rotateClockwise(deg) - Rotates PDF by specified angle.
	3. numPages - total no.of pages in PDF 
	4. addPage - Adds the specified page to the writer_obj 
	5. write - writes the specified content into the file.
	6. encrypt - Encrypts the document with the specified password
"""

