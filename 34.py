# 34. Escreva um programa que simule uma calculadora simples.
n1 = (float(input("Digite um número: ")))
operacao = (int(input("Qual operação deseja realizar:\nDigite: 1- Soma 2- Subtração 3- Multiplicação 4- Divisão\n-> ")))
n2 = (float(input("Digite mais um número: ")))
if (operacao == 1):
    resultado = (n1 + n2)
    print("{} + {} = {}".format(n1, n2, resultado))
elif (operacao == 2):
    resultado = (n1 - n2)
    print("{} - {} = {}".format(n1, n2, resultado))
elif (operacao == 3):
    resultado = (n1 * n2)
    print("{} * {} = {}".format(n1, n2, resultado))
elif (operacao == 4):
    resultado = (n1 / n2)
    print("{} / {} = {}".format(n1, n2, resultado))
else:
    print("VOCÊ DIGITOU UMA OPERAÇÃO INVÁLIDA!!!")