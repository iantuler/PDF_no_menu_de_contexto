import PyPDF2
import sys
import os

def merge_pdfs(cwd, input_pdfs, output_pdf):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf in input_pdfs:
        pdf_merger.append(pdf)

    with open(os.path.join(cwd, output_pdf), 'wb') as output:
        pdf_merger.write(output)


#teste = ["systema", "carteira.pdf", "cuidados_agua_consumo_humano_2011.pdf", "historico academico.pdf"]
cwd = os.getcwd()

input_pdfs = sys.argv[1:]
input_pdfs.sort()
output_pdf = "z.pdf"
if len(input_pdfs) < 2:
        print("Você deve selecionar pelo menos dois arquivos PDF para mesclar.")
else:
    merge_pdfs(input_pdfs, output_pdf)