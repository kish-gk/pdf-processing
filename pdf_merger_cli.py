import sys
import PyPDF2
from time import time

pdf_list = sys.argv[1:]


def merge_pdf(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        t1 = time()
        merger.append(pdf)
        t2 = time()
    merger.write("combined_file.pdf")
    print(f"Combined {len(pdf_list)} PDF's Successfully, within {(t2 - t1)} seconds !")


merge_pdf(pdf_list)

""" 
To run this script in console:
	> python pdf_merger_cli.py "file1" "file2".. so on
"""
