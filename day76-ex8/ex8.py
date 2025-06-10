
# pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.

# Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities

from pypdf import PdfWriter
import os

merger = PdfWriter()
pdf_files = []

no_of_pdf = int(input("Enter how many pdf you merger: "))

for i in range(0, no_of_pdf):
  pdf_input = input(f"Enter {i+1} pdf file name: ")
  pdf_files.append(pdf_input)

for pdfFile in pdf_files:
  if pdfFile.endswith(".pdf"):
    inputs = open(f"pdf/{pdfFile}", "rb")
    merger.append(fileobj=inputs)

output = open("pdf/new-output.pdf", "wb")
merger.write(output)

merger.close()
output.close()