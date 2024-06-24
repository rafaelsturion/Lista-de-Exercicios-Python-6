import tempfile
import os

# Criar um arquivo temporário e escrever algumas palavras nele
with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
    temp_file.write("Olá, este é um arquivo de teste.\nContém algumas palavras para exemplificar.\nPython é uma linguagem de programação poderosa.\n")
    temp_file.seek(0)  # Voltar ao início do arquivo
    nome_arquivo_temporario = temp_file.name

# a) Determinar o tamanho do arquivo temporário
tamanho_arquivo = os.path.getsize(nome_arquivo_temporario)
print(f'O tamanho do arquivo {nome_arquivo_temporario} é {tamanho_arquivo} bytes.')

# b) Criar uma lista com as palavras encontradas no arquivo temporário
with open(nome_arquivo_temporario, 'r') as arquivo:
    conteudo = arquivo.read()

# Remover caracteres especiais e quebrar o texto em palavras
palavras = conteudo.replace('\n', ' ').split()

print('Lista de palavras encontradas no arquivo:')
print(palavras)

# Remover o arquivo temporário após o uso
os.remove(nome_arquivo_temporario)
