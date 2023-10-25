import os
import winreg as reg
import subprocess

# Obter o caminho do Python na máquina
def get_python_exe():
    try:
        # Tente executar o comando "where python" para obter o caminho do Python
        result = subprocess.run(['where', 'python'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            # Se o comando foi executado com sucesso, use a primeira linha do resultado
            # que deve ser o caminho do Python
            python_exe = result.stdout.strip().split('\n')[0]
            return python_exe
        else:
            print("Erro ao obter o caminho do Python.")
            print("stderr:", result.stderr)
            return None
    except Exception as e:
        print("Erro ao obter o caminho do Python:", str(e))
        return None

#Antigo main_cadastrar_chaves
def main_cadastrar_chave(nome_pasta_reg, nome_no_menu_contexto, path_script_python, extensao, com_sys_argv):
    # Get path of current working directory and python.exe
    cwd = os.getcwd()

    # Obter o caminho do Python na máquina
    python_exe = get_python_exe()

    # optional hide python terminal in windows
    hidden_terminal = '\\'.join(python_exe.split('\\')[:-1])+"\\pythonw.exe"

   # Caminho para o ícone (substitua pelo seu caminho)
   #icone_path = os.path.join(cwd, "icone.ico")

    pasta_key_path = fr'{extensao}\\{nome_pasta_reg}'

    pasta_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, pasta_key_path)
    reg.SetValue(pasta_key,'', reg.REG_SZ, nome_no_menu_contexto)

    comando_chave = reg.CreateKey(pasta_key, r"command")

    #Dessa forma rodamos com um arquivo .exe
    if com_sys_argv:
        reg.SetValue(comando_chave, '', reg.REG_SZ, '"' + cwd + '\\' + path_script_python + '"' + '"%1"')
    else:
        reg.SetValue(comando_chave, '', reg.REG_SZ, '"' + cwd + '\\' + path_script_python + '"')


    #Abaixo é caso queira rodar com script.py
    #Nesse caso tu precisa rodar o script como argumento do python.exe "argumento"
    '''
    if com_sys_argv:
        reg.SetValue(comando_chave, '', reg.REG_SZ, hidden_terminal + ' "' + cwd + '\\' + path_script_python + '"' + ' "%1" ')
    else:
        reg.SetValue(comando_chave, '', reg.REG_SZ, hidden_terminal + ' "' + cwd + '\\' + path_script_python + '"')
    '''

#Variáveis do script de criação de chaves

#As chaves devem ser padrão chave["nome_pasta"]= "nome escolhido para pasta no regedit"
#[nome_script]= "nome que aparecerá no menu de contexto"
#[script_path]= "nome do script em python na mesma pasta que o criador de chave do windows
#["extensao"] explicação abaixo
# caso seja ao selecionar qualquer arquivo = *\\shell\\
#Caso seja uma extensao específica = .pdf\\shell\\
#Caso seja sem arquivo selecionado extensao= Directory\\Background\\shell

chaves_internas = [
        {"nome_pasta":"&mesclar_pdf", "nome_script": "&PDF Combinar", "script_path": "tkinter_combinador.exe",
         "extensao":"Directory\\Background\\shell", "com_%1": False},
        {"nome_pasta": "&converter_em_pdf", "nome_script": "&PDF Converter em pdf", "script_path": "converter_imagem_pdf.exe",
         "extensao": "*\\shell", "com_%1": True
         }
]

#main

for chaves in chaves_internas:
    main_cadastrar_chave(chaves["nome_pasta"], chaves["nome_script"], chaves["script_path"], chaves["extensao"], chaves["com_%1"])
