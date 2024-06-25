def dados():
    return "João Rafael Sturion Mantoanelli | RA: 1051392411012 | Turma DSM 1"

def cadastrar_senhas():
    
    # Abrir o arquivo 'senha.txt' no modo de adição
    with open('senha.txt', 'a') as arquivo:
        # Coletar 5 novas senhas do usuário
        for i in range(5):
            senha = input(f"Digite a senha {i+1}: ")
            # Escrever cada senha no arquivo, adicionando uma nova linha
            arquivo.write(senha + '\n')

    print("Senhas cadastradas com sucesso!")

# Chamar a função para cadastrar as senhas
cadastrar_senhas()

print(dados())