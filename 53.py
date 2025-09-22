# 53. Implemente um conversor de bases numéricas (decimal, binário, octal, hexadecimal) com validação.
valido = False
while (valido == False):
    try:
        n = int(input("Digite um número: "))
        operacao = (int(input("O que você deseja fazer?\nDigite:\n1- Descobrir o número decimal equivalente;\n2- Descobrir o número binário equivalente;\n3- Descobrir o número octal equivalente;\n4 - Descobrir o número hexadecimal equivalente.\n-> ")))
        if (1 <= operacao <= 4):
            if (operacao == 1):
                conversao = int(n)
            elif (operacao == 2):
                conversao = bin(n)
            elif (operacao == 3):
                conversao = oct(n)
            elif (operacao == 4):
                conversao = hex(n)
            print(conversao)
            valido = True
        else:
            print("VOCÊ DEVE INSERIR 1, 2, 3 OU 4!!!")
    except ValueError:
        print("VOCÊ DEVE DIGITAR APENAS NÚMEROS!!!")