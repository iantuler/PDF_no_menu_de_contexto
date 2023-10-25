import os
import tkinter as tk
from tkinter.font import Font
from PyPDF2 import PdfMerger
import configparser

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


def merge_pdfs(cwd, input_pdfs):
    '''
    :param cwd: caminho do working directory onde estão os pdf's
    :param input_pdfs: Lista contendo os pdf's ex: [caminho//exemplo//pdf1.pdf, caminho//exemplo//pdf2.pdf]
    :param output_pdf: nome do pdf que será output na pasta cwd, ex: "output.pdf"
    :return: os pdfs são mesclados e não retorna nada
    '''
    pdf_merger = PdfMerger()

    for pdf in input_pdfs:
        pdf_merger.append(pdf)

    output_pdf = output_filename_entry.get()
    if not(output_pdf.endswith(".pdf")):
        output_pdf= output_pdf + ".pdf"

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

    global directory
    merge_pdfs(directory, selected_files)
    root.quit()

#Vamos fazer de forma que usuário consiga salvar os valores de output

def save_last_entry_value(entry_value):
    config = configparser.ConfigParser()
    config.read('config.ini')
    config['LastEntry'] = {'value': entry_value}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def get_last_entry_value():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config.get('LastEntry', 'value', fallback='z.pdf')

def update_entry_value():
    new_value = output_filename_entry.get()
    save_last_entry_value(new_value)


#Cria o objeto Tkinter
root = tk.Tk()
root.title("Combinador PDF")
root.configure(background="#0233f7")

#Diretório onde se encontra os pdfs, substituimos por os.getcwd()

directory = os.getcwd()  # Change this to your directory path

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
    frame = tk.Frame(root, bg="lightblue")
    frame.pack()

    #Cria o label com o nome do file e também cria o checkboxe associando a variável var criada anteriormente no FRAME criado acima
    label = tk.Label(frame, text=os.path.basename(file), background="lightblue")
    checkbox = tk.Checkbutton(frame, variable=var, background="lightblue")

    #Empacota o label e checkbox dentro do frame recém criado
    label.pack(side="right")
    checkbox.pack(side="right")

#Last entry está relacionado a salvar o ultimo nome de pdf utilizado
#Get_last é a função que utiliza o config.ini pra realizar essa config
last_entry_value = get_last_entry_value()

#Vamo colocar um frame para o save e output
frame = tk.Frame(root)
frame.pack()

#output filename = o nome que o pdf será salvo
output_filename_entry = tk.Entry(frame)
output_filename_entry.insert(0, last_entry_value)
output_filename_entry.pack(side= "right")


save_button = tk.Button(frame, text="Save", command=update_entry_value)
save_button.pack(side="right")

#E um frame apenas pro combinar sozinho
frame_combinar= tk.Frame()
frame_combinar.pack()

#Botao de combinar!
font_button = Font(weight="bold")
generate_button = tk.Button(frame_combinar, text="Combinar!!", command=botao_comando, background="white", font=font_button)
generate_button.pack()

#Pra colocar o tab no combinar
generate_button.focus_set()

root.mainloop()