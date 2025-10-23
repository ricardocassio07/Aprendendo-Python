# 6. Desenvolva um algoritmo de busca binária usando range para otimizar a busca.
valores = []

def buscaBinaria():
    print("Pense em um número entre 1 e 100: ")
    global valores
    for i in range(1, 100):
        valores.append(i)
    encerra = False
    while (encerra == False):
        indexValorCentral = ((len(valores)) // 2)
        ValorCentral = valores[indexValorCentral]
        valido = False
        while (valido == False):
            try:
                resposta = (int(input("O número é {}:\nDigite:\n1- Sim\n2- Não\n-> ".format(ValorCentral))))
                if (1<=resposta<=2):
                    if (resposta == 1):
                        print("Uhullll!!! (^_^)")
                        valido = True
                        encerra = True
                    else:
                        print("Certo!")   
                        valido = False
                        while (valido == False):
                            try:
                                resposta = (int(input("O número é maior ou menor que {}:\nDigite:\n1- Maior\n2- Menor\n-> ".format(ValorCentral))))
                                if (1<=resposta<=2):
                                    parametro = ValorCentral
                                    print(parametro)
                                    if (resposta == 1):
                                        print("Ok!!!")
                                        # Recriando a lista:
                                        valores = [valor for valor in valores if valor > parametro]
                                        valido = True
                                    elif (resposta == 2):
                                        print("Certo!")
                                        # Recriando a lista:
                                        valores = [valor for valor in valores if valor < parametro]
                                        valido = True
                                else:
                                    print("Digite 1 ou 2!!!")
                            except:
                                print("Digite apenas números inteiros!!!")
                else:
                    print("Digite 1 ou 2!!!")
            except:
                print("Digite apenas números inteiros!!!")
        if ((ValorCentral == 1) or (ValorCentral == 100)):
            print("Estamos no limite das opções!!! Você deve ter escolhido alguma opção errada no caminho (︶︹︺)!!!")
            encerra = True

buscaBinaria()