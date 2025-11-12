'''
    5: Desenvolva uma calculadora que calcule impostos progressivos baseados em
    diferentes faixas de renda, com simulações de cenários e comparações anuais.
Requisitos técnicos:
    - Use range para iterar pelas faixas de imposto
    - Implemente try-except para validação de valores monetários
    - Use if-elif-else para aplicar diferentes alíquotas
    - Crie função para cálculos de cada faixa
    - Use while para simulações múltiplas 
'''
import random
def calculo_de_imposto(valor):
    aliquotas = [0.05, 0.10, 0.15, 0.20]
    # print(aliquotas)
    mult = random.uniform(1, 3)
    for i in range(len(aliquotas)):
        valorAnterior = aliquotas[i]
        valorReajustado = (valorAnterior * mult)
        aliquotas.insert(i, valorReajustado)
    # print(aliquotas)
    if (valor <= 10000):
        imposto = (valor * aliquotas[0])
        aliquota = aliquotas[0]
    elif (valor <= 20000):
        imposto = (valor * aliquotas[1])
        aliquota = aliquotas[1]
    elif (valor <= 30000):
        imposto = (valor * aliquotas[2])
        aliquota = aliquotas[2]
    else:
        imposto = (valor * aliquotas[3])
        aliquota = aliquotas[3]
    return (imposto, (aliquota / 100))

valores = {}
diferencasBienais = {}

rendasInseridas = 0
continuar = True
while (continuar == True):
    valido = False
    while (valido == False):
        try:
            renda = (int(input("Digite o valor da renda que deseja verificar:\n-> ")))
            if (renda > 0):
                valido =  True
        except ValueError:
            print("DIGITE APENAS NÚMEROS!")
    valido = False
    while (valido == False):
        try:
            qtdeAnosTotal = (int(input("Digite qunatos anos você deseja verificar o valor a ser pago de impostos:\n-> ")))
            if (qtdeAnosTotal > 0):
                valido =  True
        except ValueError:
            print("DIGITE APENAS NÚMEROS!")
    ano = 0
    while (ano < qtdeAnosTotal):
        imposto, aliquota = calculo_de_imposto(renda)
        valores[ano] = (renda, aliquota, renda)
        rendasInseridas += 1
        print(valores)
        if (rendasInseridas > 1):
            # print("p")
            for i in range(0, len(valores)):
                # print("0")
                if ((i % 2 == 0) and ((i + 1) < len(valores))):
                    # print("oi")
                    diferenca = (valores[(i + 1)][1] - valores[i][1])
                    percentual = ((diferenca / valores[i][1]) * 100)
                    diferencasBienais[i] = (diferenca, percentual)
                    print(diferencasBienais)
        ano += 1
    # Mostrar:
    valido = False
    while (valido == False):
        try:
            desejo = (int(input("Deseja verificar outra renda?\nDigite:\n1- Sim\n2- Não\n-> ")))
            if (1 <= desejo <= 2):
                valido =  True
                if (desejo == 2):
                    print("OK! FOI BOM TER VOCÊ CONOSCO!")
                    continuar = False
            else:
                print("DIGITE 1(SIM) OU 2(NÃO)!")
        except ValueError:
            print("DIGITE APENAS NÚMEROS!")
