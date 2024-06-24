# Dados do usuário
nome = "João Rafael Sturion Mantoanelli"
ra = "1051392411012"
turma = "DSM 1"

# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Função para determinar o peso ideal baseado no sexo e no IMC
def verificar_peso_ideal(imc, sexo):
    if sexo.lower() == "feminino":
        if imc < 19:
            return "abaixo do peso"
        elif 19 <= imc < 24:
            return "no peso ideal"
        else:
            return "acima do peso"
    elif sexo.lower() == "masculino":
        if imc < 20:
            return "abaixo do peso"
        elif 20 <= imc < 25:
            return "no peso ideal"
        else:
            return "acima do peso"
    else:
        return "Sexo inválido"

# Entrada de dados
peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))
sexo = input("Digite o sexo (masculino/feminino): ")

# Cálculo do IMC
imc = calcular_imc(peso, altura)

# Verificação do peso ideal
resultado = verificar_peso_ideal(imc, sexo)

# Exibição dos resultados
print(f"\nNome: {nome} | RA: {ra} | Turma: {turma}")
print(f" Seu IMC é {imc:.2f} e  você está {resultado}.")
