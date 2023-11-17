import PyPDF2 
  
# opened file as reading (r) in binary (b) mode 
file ='Pdf-List/document2.pdf' 
  
# store data in pdfReader 
pdfReader = PyPDF2.PdfReader(file) 
  
# count number of pages 
totalPages = len(pdfReader.pages)
  
# print number of pages 
print(f"{totalPages}")