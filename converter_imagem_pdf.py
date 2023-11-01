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

def qual_output(cwd):
    lista_arquivos = os.listdir(cwd)
    if not ("z.pdf") in lista_arquivos:
        return "z.pdf"
    else:
        for k in range(1,10):
            nome_z = "z" + str(k) + ".pdf"
            if not(nome_z in lista_arquivos):
                return nome_z

        return "zz.pdf"


cwd = os.getcwd()
path = "\\".join(sys.argv[1:])

#Testes
# cwd = rf"C:\Users\iantu\Documents\Projetos Orulo\PDFcontexto\Teste aqui"
# path = rf"C:\Users\iantu\Documents\Projetos Orulo\PDFcontexto\Teste aqui\merhy.jpeg"

image_path = path

#Tenho que adicionar aqui a possibilidade de criação de z1, z2, z3...

pdf_path = os.path.join(cwd, qual_output(cwd))

image_to_pdf(image_path, pdf_path)

'''with open("C:\\Users\\iantu\\Documents\\Projetos Orulo\\PDFcontexto\\Teste aqui\\informacoes.txt", "w") as arquivo:
    arquivo.write("\\".join(os.sys.argv[1:]))
    arquivo.write("\n fim de um argumento\n")'''
