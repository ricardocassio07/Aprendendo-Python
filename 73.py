'''
    1: Crie uma função que receba uma lista de valores (que podem ser números, strings ou
    outros tipos) e retorne uma nova lista contendo apenas os números primos válidos. A
    função deve tratar exceções para valores inválidos e usar estruturas condicionais para
    validação.
Requisitos técnicos:
    - Use try-except para tratar conversões inválidas
    - Implemente verificação de primo com for e range
    - Use if-elif-else para diferentes casos de validação
    - A função deve aceitar qualquer iterável como entrada
Exemplo:
    entrada = [2, 3, "4", 5, "abc", 7.0, 11, "13", None, 17]
    saida_esperada = [2, 3, 5, 7, 11, 13, 17] 
'''

def lista():
    # Criação da lista:
    lista = []
    # Inserção do conteúdo:
    continuar = True
    while continuar:
        valor = (input("Digite o conteúdo que deseja inserir inserir na lista:\n-> "))
        lista.append(valor)
        valido = False
        while (valido == False):
            try:
                opcao = (int(input("Você deseja inserir mais algum conteúdo na lista?\nDigite:\n1 - Sim\n2 - Não\n-> ")))
                if (1 <= opcao <= 2):
                    valido = True
                    if (opcao == 2):
                        print("Ok! Vamos para a próxima etapa!")
                        continuar = False
                else:
                    print("DIGITE: 1- SIM OU 2- NÃO!!!")
            except:
                print("VOCÊ DEVE DIGITAR APENAS NÚMEROS!!!")
    # print(lista)
    # Criação da lista para armazenar os númmeros primos:
    lista_primos = []
    # Verificar quais valores são números primos:
    for posicao in range(len(lista)):
        try:
            num = lista[posicao]
            # print(num)
            num = int(num)
            # print(num)
            numero_de_divisores = 0
            if (num > 1):
                for divisor in range(2, num):
                    # print(divisor)
                    if ((num % divisor) == 0):
                        numero_de_divisores += 1
                if (numero_de_divisores == 0):
                    lista_primos.append(num)
                else:
                    print("O NÚMERO {0} NÃO É PRIMO!".format(num))
            elif (num == 1):
                print("O NÚMERO 1 NÃO É PRIMO!!!")
            elif (num < 0):
                print("NÚMEROS NEGATIVOS NÃO SÃO PRIMOS!!!")
        except:
            print("O VALOR '{0}' NÃO É UM NÚMERO!!!".format(lista[posicao]))
    # Retorna lista com os números primos:
    return lista_primos

resultado = lista()
print(resultado)