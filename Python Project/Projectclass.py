from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter
import tkinter as tk
from tkinter import filedialog

merger = PdfWriter()

root = tk.Tk()
class OpenDir:
    def __init__(self) -> None:
        self.pdf_number = int(input("Enter the no of pdf's you want to merge:")) 
        self.pdf_lst = [] 

    def opendir(self,cls):
        self.path = filedialog.askopenfilename(title="Select a File", filetypes=[("PDF Files", "*.pdf"), ("All files", "*.*")])
        self.pdf_lst.append(self.path)



    def read_pages(self,cls):
        for self.pdf_path in self.pdf_lst:
            self.pdfreader = PdfReader(self.pdf_path)
            self.totalpages = len(self.pdfreader.pages)
            print(self.totalpages)

    def merge_pdf(self):
        for self.pdf_path in self.pdf_lst:
            merger.append(self.pdf_path)

        with open("Merged_File.pdf","wb") as pdf:
            merger.write(pdf) 

    def run(self):
        self.i = 0
        for self.i in range(0,self.pdf_number):
            self.opendir(self)

        self.read_pages(self)

file = OpenDir()
file.run()
file.merge_pdf()


