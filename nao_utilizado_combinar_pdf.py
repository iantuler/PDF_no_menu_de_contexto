import PyPDF2
import re
import os
from tkinter import *

def merge_pdfs(cwd, input_pdfs, output_pdf):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf in input_pdfs:
        pdf_merger.append(pdf)

    with open(os.path.join(cwd, output_pdf), 'wb') as output:
        pdf_merger.write(output)

def encontrar_z_pdf(diretorio):
    '''
    :param diretorio: path da pasta trabalhada
    :return: retorna uma lista com todos os z1, z2, z3, z4 listados
    '''
    pdf_files = []

    if not os.path.isdir(diretorio):
        return pdf_files

    for filename in os.listdir(diretorio):
        match = re.match(r'z(\d+)\.pdf')
        if match:
            pdf_files.append(os.path.join(diretorio,filename))

'''input_pdfs=[]
cwd = os.getcwd()

output_pdf = "z.pdf"
if len(input_pdfs) < 2:
        print("Você deve selecionar pelo menos dois arquivos PDF para mesclar.")
else:
    merge_pdfs(input_pdfs, output_pdf)'''


root= Tk()

class Aplicacao():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()
    def tela(self):
        self.root.title("Combine os pdf's")
        self.root.config(background = "#0233f7")
        self.root.geometry("250x350")

Aplicacao()