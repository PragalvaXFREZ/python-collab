from PyPDF2 import PdfWriter
import tkinter as tk
from tkinter import filedialog
merger = PdfWriter()
class merge():
    def __init__(self) :
        self.pdfCount = int(input("Enter how many pdfs you want to merge:"))
        self.pdf_list = []
    def appendPath(self):
        self.path = filedialog.askopenfilename(title = "Choose your file" , filetypes=[("PDF Files",".pdf"),("All files","*.*")])
        self.pdf_list.append(self.path)
    def mergePdf(self):
        for self.path in self.pdf_list:
            merger.append(self.path)
        self.finalpath = filedialog.askdirectory(title = "Choose where you want to save your file")
        with open (f"{self.finalpath}//Merged_Pdf.pdf","wb") as Mergedpdf:
            merger.write(Mergedpdf)
    def RunMerger(self):
        for self. i in range(0,self.pdfCount):
            self.appendPath()
        self.mergePdf()

if __name__ == "__main__":
    PdfMerger = merge()
    PdfMerger.RunMerger()
        