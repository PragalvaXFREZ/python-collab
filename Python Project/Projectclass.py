from pypdf import PdfWriter

merger = PdfWriter()

input1 = open("Pdf-List\\document1.pdf", "rb")
input2 = open("Pdf-List\\document2.pdf", "rb")
input3 = open("Pdf-List\\document3.pdf", "rb")

# Add the first 3 pages of input1 document to output
merger.append(fileobj=input1, pages=(0, 2))

# Insert the first page of input2 into the output beginning after the second page
merger.merge(position=2, fileobj=input2, pages=(0, 373))

# Append entire input3 document to the end of the output document
merger.append(input3)

# Write to an output PDF document
output = open("document-output.pdf", "wb")
merger.write(output)

# Close file descriptors
merger.close()
output.close()