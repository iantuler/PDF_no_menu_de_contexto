import os
import tkinter as tk
from PyPDF2 import PdfMerger

def encontrar_z_pdf(diretorio):
    '''
    :param diretorio: path da pasta trabalhada
    :return: retorna uma lista com todos os z1, z2, z3, z4 listados
    '''
    pdf_files = []

    if not os.path.isdir(diretorio):
        return pdf_files

    for filename in os.listdir(diretorio):
        if filename.endswith(".pdf"):
            pdf_files.append(os.path.join(diretorio, filename))

    return pdf_files


def merge_pdfs(cwd, input_pdfs, output_pdf):
    '''
    :param cwd: caminho do working directory onde estão os pdf's
    :param input_pdfs: Lista contendo os pdf's ex: [caminho//exemplo//pdf1.pdf, caminho//exemplo//pdf2.pdf]
    :param output_pdf: nome do pdf que será output na pasta cwd, ex: "output.pdf"
    :return: os pdfs são mesclados e não retorna nada
    '''
    pdf_merger = PdfMerger()

    for pdf in input_pdfs:
        pdf_merger.append(pdf)

    with open(os.path.join(cwd, output_pdf), 'wb') as output:
        pdf_merger.write(output)

def botao_comando():
    '''
    Essa é a função associada ao botão do interface
    caso não tenha nenhum pdf marcado, ele irá encerrar o programa
    caso tenha 2 ou mais pdfs será combinado através da função merge pdf
    :return:
    '''
    selected_files = [file for file, var in zip(pdf_files, checkboxes) if var.get() == 1]
    if len(selected_files)<2:
        root.quit()
    merge_pdfs("C:\\Users\\iantu\\Documents\\Projetos Orulo\\PDFcontexto\\Teste aqui", selected_files, "combinado.pdf")
    root.quit()


#Cria o objeto Tkinter
root = tk.Tk()
root.title("Combinador PDF")

#Diretório onde se encontra os pdfs, substituimos por os.getcwd()
directory = "C:\\Users\\iantu\\Documents\\Projetos Orulo\\PDFcontexto\\Teste aqui"  # Change this to your directory path
#Retorna uma lista com todos pdf's
pdf_files = encontrar_z_pdf(directory)
#Lista vazia que serão adicionados os vários pdfs
checkboxes = []

#Aqui são criados os checkboxes e labels
for file in pdf_files:

    #Cria uma variável de controle var que contém a informação se a checkboxe foi marcado ou nao
    var = tk.IntVar(value=1)
    checkboxes.append(var)

    #Cria um frame onde será adicionado tanto a checkbox quanto o label
    frame = tk.Frame(root)
    frame.pack()

    #Cria o label com o nome do file e também cria o checkboxe associando a variável var criada anteriormente no FRAME criado acima
    label = tk.Label(frame, text=os.path.basename(file))
    checkbox = tk.Checkbutton(frame, variable=var)

    #Empacota o label e checkbox dentro do frame recém criado
    label.pack(side="right")
    checkbox.pack(side="right")

generate_button = tk.Button(root, text="Combinar!!", command=botao_comando)
generate_button.pack()

root.mainloop()