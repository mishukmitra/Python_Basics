import os
from PyPDF2 import PdfWriter 

merger = PdfWriter()


list_files = os.listdir()

# for file in list_files:
#     if file.endswith(".pdf"):
#         print(file)

files = [file for file in list_files if file.endswith(".pdf")]
print(files)


for pdf in files:
    merger.append(pdf)
    
merger.write("my_merged.pdf")
merger.close()


    



