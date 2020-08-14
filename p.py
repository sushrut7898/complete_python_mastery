import PyPDF2

merger = PyPDF2.PdfFileMerger
files_names = ["first.pdf", "second.pdf"]
for files_name in files_names:
    merger.append(file_name)
merger.write("combined.pdf")
merger.close()
