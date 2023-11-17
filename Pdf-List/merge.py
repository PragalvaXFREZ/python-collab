from pypdf import PdfWriter

merger = PdfWriter()

input1 = "Pdf-List/document1.pdf"
input2 = "Pdf-List/document2.pdf"
input3 = "Pdf-List/document3.pdf"



merger.append(input1)
merger.append(input2)
merger.append(input3)

# Write to an output PDF document
output = open("document-output.pdf", "wb")
merger.write(output)

# Close file descriptors
merger.close()
output.close()