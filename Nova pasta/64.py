# 2. Implemente um gerador de progressões aritméticas e geométricas usando range de forma criativa.
def progressao():   
    verificado = False
    while (verificado == False):
        try:  
            inicio = (float(input("Digite o número inicial da progressão: ")))
            try:
                nTermos = (int(input("Digite o número de termos da progressão: ")))
                razao = (float(input("Digite a razão da progressão: ")))

                if (nTermos > 1):
                    print("Ok! A progressão irá começar com o número inicial do intervalo ({0}) e mostrará ele manipulado com a razão {1} veze(s)!".format(inicio, nTermos))

                    verificado = True
                else:
                    print("O número de termos deve ser maior que 1 (um)!!!")
            except ValueError:
                print("Você deve digitar apenas números inteiros!")
        except:
            print("Você deve digitar apenas números!")   

    verificado = False
    while (verificado == False):
        try:
            tipo = (int(input("Qual progressão deseja obter?\nDigite:\n1. Progressão Aritmética\n2. Progressão Geométrica\n->  ")))
            if (1 <= tipo <= 2):
                verificado = True
            else:
                print("Você deve digitar 1 ou 2!!!")
        except:
            print("Você deve digitar apenas número e apenas números inteiros!")

    progressao = []
    n = inicio
    r = razao
    inicio = int(inicio)
    # Variável para utilizar no range(), soma o número inicial com o número de termos para sabermos a quantidade de vezes que a função irá se repetir!
    fim = (inicio + nTermos)
    fim = int(fim)
    
    if (tipo == 1):
        if (inicio > fim):
            temporario = fim
            fim = inicio
            inicio = temporario
        for i in range((inicio), (fim)):
            progressao.append(n)
            n += r
        print("\nA PROGRESSÃO ARITMÉTICA É {}!!!\n".format(progressao))
        
    elif (tipo == 2):
        if (inicio > fim):
            temporario = fim
            fim = inicio
            inicio = temporario
        for i in range((inicio), (fim)):
            progressao.append(n)
            n *= r
        print("\nA PROGRESSÃO GEOMÉTRICA É {}!!!\n".format(progressao))

progressao()