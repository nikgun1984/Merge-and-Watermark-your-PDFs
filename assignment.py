import PyPDF2

with open('super.pdf','rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)

    with open('wtr.pdf', 'rb') as file_wtm:
        watermark = PyPDF2.PdfFileReader(file_wtm)
        lst = []
        for page in range(0,reader.numPages):
            n_page = reader.getPage(page)
            n_page_watermark = watermark.getPage(0)
            n_page.mergePage(n_page_watermark)
            lst.append(n_page)

        pdf_writer = PyPDF2.PdfFileWriter()

        for i in lst:
            pdf_writer.addPage(i)

        with open('output.pdf','wb') as output_file:
            pdf_writer.write(output_file)

#Or this way --> more elegant way :)

template = PyPDF2.PdfFileReader(open('super.pdf','rb'))
watermark2 = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark2.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf','wb') as file:
        output.write(file)
