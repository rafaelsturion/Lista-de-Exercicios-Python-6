def dados():
    return "João Rafael Sturion Mantoanelli | RA: 1051392411012 | Turma DSM 1"

def adicionar_emails():
    # Nome do arquivo
    nome_arquivo = 'email.txt'

    # Abrir o arquivo no modo de acréscimo
    with open(nome_arquivo, 'a') as arquivo:
        # Solicitar ao usuário para adicionar 3 e-mails
        for i in range(3):
            email = input(f"Digite o {i+1}º e-mail: ")
            # Adicionar o e-mail ao arquivo
            arquivo.write(email + '\n')

    print("3 e-mails foram adicionados com sucesso ao arquivo.")

# Chamar a função para adicionar e-mails
adicionar_emails()

"""
Explicação do Código
Definição da Função adicionar_emails:

nome_arquivo = 'email.txt': Define o nome do arquivo onde os e-mails serão armazenados.
Abrir o Arquivo no Modo de Acréscimo ('a'):

with open(nome_arquivo, 'a') as arquivo: Abre o arquivo email.txt no modo de acréscimo, que permite adicionar novos dados ao final do arquivo sem apagar o conteúdo existente.
Solicitar ao Usuário a Entrada de 3 E-mails:

for i in range(3): Um loop que se repete 3 vezes para solicitar 3 e-mails do usuário.
email = input(f"Digite o {i+1}º e-mail: "): Solicita ao usuário que digite um e-mail e armazena na variável email.
arquivo.write(email + '\n'): Escreve o e-mail no arquivo, adicionando uma nova linha ('\n') após cada e-mail.
Mensagem de Confirmação:

print("3 e-mails foram adicionados com sucesso ao arquivo."): Informa ao usuário que os e-mails foram adicionados com sucesso.
Como Executar o Programa
Criar o Arquivo email.txt: Certifique-se de que o arquivo email.txt existe no mesmo diretório que o seu script Python. Se o arquivo não existir, o Python criará um novo arquivo quando você executar o script.

Executar o Script: Rode o script em um ambiente Python. Ele solicitará a entrada de 3 e-mails e os adicionará ao arquivo email.txt.

Este código é uma maneira simples e eficiente de adicionar novos e-mails a um arquivo existente, mantendo o conteúdo existente intacto.
"""