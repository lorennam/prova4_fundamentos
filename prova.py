# PROVA 04 - FUNDAMENTOS DA PROGRAMAÇÃO

# PROFESSOR: AUGUSTO CÉSAR OLIVEIRA
# ALUNAS: AMANDA LUZ E LORENNA MENESES

print("Este é o Simulador de Concessionária")
print("\nTemos os seguintes carro:\nAudi A4\nBMW Série Três\nChevrolet Camaro\nCitroën Cê Três\nFiat Uno\nFord Focus\nHonda Civic\nHyundai Tucson\nJeep Renegade\nKia Sportage\nMazda CX-Cinco\nMercedes-Benz Classe Cê\nMitsubishi Outlander\nNissan Sentra\nPeugeot Duzentos e Oito\nRenault Clio\nSubaru Impreza\nToyota Corolla\nVolkswagen Golf\nVolvo XC-Sessenta")
print("\nAs faixas de preço são:\n1) Menor que R$10000,00\n2) Maior que R$10000,00 e menor que R$30000\n3) Maior que R$30000,00 e menor que R$60000\n4) Maior que R$60000,00")

# Questão 01

nome_carro = input("\nDigite o nome do carro que você deseja comprar: ")
preco = float(
    input("Digite o valor do carro que você gostaria de conhecer:  "))


# Questão 02

print("\nO usuário gostaria de saber se o carro", nome_carro,
      "está disponível e gostaria de pagar", preco, "reais nesse carro.")


# Questão 03

carros = ["Audi A4", "BMW Série 3",
          "Chevrolet Camaro",
          "Citroën C3",
          "Fiat Uno",
          "Ford Focus",
          "Honda Civic",
          "Hyundai Tucson",
          "Jeep Renegade",
          "Kia Sportage",
          "Mazda CX-5",
          "Mercedes-Benz Classe C",
          "Mitsubishi Outlander",
          "Nissan Sentra",
          "Peugeot 208",
          "Renault Clio",
          "Subaru Impreza",
          "Toyota Corolla",
          "Volkswagen Golf",
          "Volvo XC60"]


# Questão 04
# Implementada na questão 6
# for carro in carros:
#    if (carro == nome_carro):
#        print("Carro encontrado!")
#        break
#    else:
#        print("Carro não encontrado!")


# Questão 05
# Implementado na questão 07
# if (preco < 10000):
#    print("Mal estado")

# elif (preco < 30000):
#    print("Conservado")

# elif (preco < 60000):
#    print("Seminovo")

# else:
#    print("Carro novo")


# Questão 06

def procurar_carro(nome_carro):
    for carro in carros:
        if (carro == nome_carro):
            return ("Carro encontrado!")
    return ("Carro não encontrado")


carro_existe = procurar_carro(nome_carro)
print(carro_existe)


# Questão 07

def avaliacao_carro(preco):
    if (carro_existe == "Carro encontrado!"):
        if (preco < 10000):
            return "Mal estado"
        elif (preco < 30000):
            return ("Conservado")
        elif (preco < 60000):
            return ("Seminovo")
        else:
            return ("Carro novo")


resultado_avaliacao = avaliacao_carro(preco)
print(resultado_avaliacao)

# Questão 08

if (carro_existe == "Carro encontrado!"):
    print("O usuário gostaria de um carro", nome_carro,
          "na qualidade", resultado_avaliacao,)


# Questão 09

while True:
    nome_carro1 = input("Digite o nome do carro que você deseja comprar: ")
    preco = float(
        input("Digite o valor do carro que você gostaria de conhecer:  "))

    carros1 = ["Audi A4",
               "BMW Série 3",
               "Chevrolet Camaro",
               "Citroën C3",
               "Fiat Uno",
               "Ford Focus",
               "Honda Civic",
               "Hyundai Tucson",
               "Jeep Renegade",
               "Kia Sportage",
               "Mazda CX-5",
               "Mercedes-Benz Classe C",
               "Mitsubishi Outlander",
               "Nissan Sentra",
               "Peugeot 208",
               "Renault Clio",
               "Subaru Impreza",
               "Toyota Corolla",
               "Volkswagen Golf",
               "Volvo XC60"]

    def procurar_carro(nome_carro1):
        for carro in carros1:
            if (carro == nome_carro1):
                return ("Carro encontrado!")
        return ("Carro não encontrado")

    carro_existe = procurar_carro(nome_carro1)
    print(carro_existe)

    def avaliacao_carro(preco):
        if (carro_existe == "Carro encontrado!"):
            if (preco < 10000):
                return "Mal estado"
            elif (preco < 30000):
                return ("Conservado")
            elif (preco < 60000):
                return ("Seminovo")
            else:
                return ("Carro novo")

    resultado_avaliacao = avaliacao_carro(preco)
    print(resultado_avaliacao)

    if (carro_existe == "Carro encontrado!"):
        print("O usuário gostaria de um carro", nome_carro1,
              "na qualidade", resultado_avaliacao,)

    continuar = int(
        input("Digite '1' para continuar ou '2' caso deseje parar: "))
    if (continuar == 2):
        break
