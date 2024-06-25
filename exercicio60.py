def dados():
    return "João Rafael Sturion Mantoanelli | RA: 1051392411012 | Turma DSM 1"

def calcular_imc(peso,altura):
   imc = peso / (altura ** 2)
   return imc

def verificar_peso(imc,sexo):
    if sexo.lower() == "feminino":
        if imc < 19:
            return "Abaixo do peso"
        elif imc >= 19 and imc < 24:
            return "Peso ideal"
        else:
            return "Acima do peso"
    elif sexo.lower() == "masculino":
        if imc < 10:
            return "Abaixo do peso"
        elif imc >= 20 and imc < 25:
            return "Peso ideal"
        else:
            return "Acima do peso"
    else: 
        return "Sexo inválido"
    

print(dados())

peso = float(input("Digite o seu peso em kilogramas: "))
altura = float(input("Digite a sua altura em metros: "))
sexo = str(input("Digite o seu sexo(masculino/feminino): "))

imc = calcular_imc(peso, altura)

# Verificação do peso ideal
resultado = verificar_peso(imc, sexo)
print(resultado)