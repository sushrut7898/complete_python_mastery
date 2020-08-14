#import PyPDF2

# with open("first.pdf", "rb") as file:  # Returns a FileStream Object
#    reader = PyPDF2.PdfFileReader(file)
#    print(reader.numPages)
#    page = reader.getPage(0)
#    page.rotateClockwise(90)
#    writer = PyPDF2.PdfFileWriter()
#    writer.addPage(page)
#    with open("rotated.pdf", "wb") as output:
#        writer.write(output)

import PyPDF2

merger = PyPDF2.PdfFileMerger
files_names = ["first.pdf", "second.pdf"]
for files_name in files_names:
    merger.append(file_name)
merger.write("combined.pdf")
