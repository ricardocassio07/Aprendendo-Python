# 50. Escreva um programa que verifique se três lados podem formar um triângulo e classifique-o.
l1 = (float(input("Digite o valor da medida de um dos lados do triângulo: ")))
l2 = (float(input("Digite o valor da medida do outro lado do triângulo: ")))
l3 = (float(input("Digite o valor da medida do último lado do triângulo: ")))
if ((l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1)):
    print("OS LADOS FORMAM UM TRIÂNGULO!!!")
    if (l1 == l2 == l3):
        resposta = ("EQUILÁTERO")
    elif (l1 != l2 != l3):
        resposta = ("ESCALENO")
    else:
        resposta = ("ISÓSCELES")
    print("O triângulo, cujo seus lados medem {}, {} e {}, é {}!".format(l1, l2, l3, resposta))
else:
    print("OS LADOS NÃO FORMAM UM TRIÂNGULO!!!")
    