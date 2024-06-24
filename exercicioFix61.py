# Dados do usuário
nome = "João Rafael Sturion Mantoanelli"
ra = "1051392411012"
turma = "DSM 1"

def ler_emails(arquivo):
    try:
        with open(arquivo, 'r') as file:
            emails = file.readlines()
        # Remover espaços em branco ou quebras de linha
        emails = [email.strip() for email in emails]
    except FileNotFoundError:
        emails = []
    return emails

def escrever_emails(arquivo, emails):
    with open(arquivo, 'a') as file:
        for email in emails:
            file.write(email + '\n')

def main():
    arquivo = 'email.txt'
    
    # Ler emails já cadastrados
    emails_existentes = ler_emails(arquivo)
    print("Emails cadastrados atualmente:")
    for email in emails_existentes:
        print(email)
    
    # Solicitar novos emails
    novos_emails = []
    for i in range(3):
        novo_email = input(f"Digite o novo e-mail {i + 1}: ")
        novos_emails.append(novo_email)
    
    # Escrever novos emails no arquivo
    escrever_emails(arquivo, novos_emails)
    
    # Ler emails atualizados
    emails_atualizados = ler_emails(arquivo)
    print("\nEmails atualizados:")
    for email in emails_atualizados:
        print(email)

    print(f"\nNome: {nome} | RA: {ra} | Turma: {turma}")

if __name__ == "__main__":
    main()
