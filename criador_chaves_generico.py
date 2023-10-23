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
'''def main_cadastrar_chave(nome_pasta_reg, nome_no_menu_contexto, path_script_python, extensao):
    # Get path of current working directory and python.exe
    cwd = os.getcwd()

    # Obter o caminho do Python na máquina
    python_exe = get_python_exe()

    # optional hide python terminal in windows
    hidden_terminal = '\\'.join(python_exe.split('\\')[:-1])+"\\pythonw.exe"

   # Caminho para o ícone (substitua pelo seu caminho)
    icone_path = os.path.join(cwd, "icone.ico")

    pasta_key_path = fr'{extensao}\\{nome_pasta_reg}'

    pasta_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, pasta_key_path)
    reg.SetValue(pasta_key,'', reg.REG_SZ, nome_no_menu_contexto)

    comando_chave = reg.CreateKey(pasta_key, r"command")
    reg.SetValue(comando_chave, '', reg.REG_SZ, hidden_terminal + ' "' + cwd + '\\' + path_script_python + '"')
    '''

def main_cadastrar_chave(nome_pasta_reg, nome_no_menu_contexto, path_script_python, extensao):

    # Obter o caminho do Python na máquina
    python_exe = get_python_exe()

    pasta_key_path = fr'Software\Classes\{extensao}'

    # Crie as chaves no registro
    with reg.OpenKey(reg.HKEY_CLASSES_ROOT, pasta_key_path, 0, reg.KEY_SET_VALUE) as pasta_key:
        reg.SetValue(pasta_key, '', reg.REG_SZ, nome_pasta_reg)

    with reg.OpenKey(reg.HKEY_CLASSES_ROOT, fr'{pasta_key_path}\shell\{nome_no_menu_contexto}', 0, reg.KEY_SET_VALUE) as contexto_key:
        reg.SetValue(contexto_key, '', reg.REG_SZ, nome_no_menu_contexto)

    with reg.OpenKey(reg.HKEY_CLASSES_ROOT, fr'{pasta_key_path}\shell\{nome_no_menu_contexto}\command', 0, reg.KEY_SET_VALUE) as comando_key:
        reg.SetValue(comando_key, '', reg.REG_SZ, f'"{python_exe}" "{os.path.abspath(path_script_python)}" %*')


#Variáveis do script de criação de chaves

#As chaves devem ser padrão chave["nome_pasta"]= "nome escolhido para pasta no regedit"
#[nome_script]= "nome que aparecerá no menu de contexto"
#[script_path]= "nome do script em python na mesma pasta que o criador de chave do windows
#["extensao"] explicação abaixo
# caso seja ao selecionar qualquer arquivo = *\\shell\\
#Caso seja uma extensao específica = .pdf
#Caso seja sem arquivo selecionado extensao= Directory\\Background\\shell

chaves_internas = [
        {"nome_pasta":"&mesclar_pdf", "nome_script": "&PDF Combinar", "script_path": "combinar_pdf.py",
         "extensao":".pdf"},
        {"nome_pasta": "&converter_em_pdf", "nome_script": "&PDF Converter em pdf", "script_path": "converter_imagem.py",
         "extensao": ".pdf"
         }
]

#main

for chaves in chaves_internas:
    main_cadastrar_chave(chaves["nome_pasta"], chaves["nome_script"], chaves["script_path"], chaves["extensao"])
