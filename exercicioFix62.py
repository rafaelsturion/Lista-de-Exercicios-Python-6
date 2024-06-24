def ler_senhas(arquivo):
    try:
        with open(arquivo, 'r') as file:
            senhas = file.readlines()
        # Remover espaços em branco ou quebras de linha
        senhas = [senha.strip() for senha in senhas]
    except FileNotFoundError:
        senhas = []
    return senhas

def escrever_senhas(arquivo, senhas):
    with open(arquivo, 'a') as file:
        for senha in senhas:
            file.write(senha + '\n')

def main():
    arquivo = 'senha.txt'
    
    # Ler senhas já cadastradas
    senhas_existentes = ler_senhas(arquivo)
    print("Senhas cadastradas atualmente:")
    for senha in senhas_existentes:
        print(senha)
    
    # Solicitar novas senhas
    novas_senhas = []
    for i in range(5):
        nova_senha = input(f"Digite a nova senha {i + 1}: ")
        novas_senhas.append(nova_senha)
    
    # Escrever novas senhas no arquivo
    escrever_senhas(arquivo, novas_senhas)
    
    # Ler senhas atualizadas
    senhas_atualizadas = ler_senhas(arquivo)
    print("\nSenhas atualizadas:")
    for senha in senhas_atualizadas:
        print(senha)

if __name__ == "__main__":
    main()
