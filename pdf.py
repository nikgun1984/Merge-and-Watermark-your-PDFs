import PyPDF2
import sys

args = sys.argv[1:]# any number of arguments

def pdf_combiner(pdf_lst):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_lst:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')
pdf_combiner(args)
