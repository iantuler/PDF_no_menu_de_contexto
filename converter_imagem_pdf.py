import sys

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
import os

def image_to_pdf(image_path, pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=letter)
    img = Image.open(image_path)
    width, height = img.size

    c.drawImage(image_path, 0, 0, width, height)
    c.showPage()
    c.save()


cwd = os.getcwd()
image_path = sys.argv[1]
# Substitua pelo caminho da sua imagem
pdf_path = os.path.join(cwd, "z.pdf")    # Caminho para salvar o arquivo PDF

image_to_pdf(image_path, pdf_path)

