import sys
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
import os

def image_to_pdf(image_path, pdf_path):
    img = Image.open(image_path)
    img_width, img_height = img.size

    c = canvas.Canvas(pdf_path, pagesize=(img_width, img_height))  # Defina o tamanho da página com base nas dimensões da imagem
    c.drawImage(image_path, 0, 0, width=img_width, height=img_height)
    c.showPage()
    c.save()

cwd = os.getcwd()
path = "\\".join(sys.argv[1:])
image_path = path
pdf_path = os.path.join(cwd, "z.pdf")

image_to_pdf(image_path, pdf_path)

'''with open("C:\\Users\\iantu\\Documents\\Projetos Orulo\\PDFcontexto\\Teste aqui\\informacoes.txt", "w") as arquivo:
    arquivo.write("\\".join(os.sys.argv[1:]))
    arquivo.write("\n fim de um argumento\n")'''
