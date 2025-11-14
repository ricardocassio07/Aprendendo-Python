# 29. Crie um programa que determine o maior entre três números.
n1 = (float(input("Digite um número: ")))
maior = n1
n2 = (float(input("Digite outro número: ")))
n3 = (float(input("Digite mais um número: ")))
if (maior < n2):
    maior = n2
if (maior < n3):
    maior = n3
print("O número {} é o maior entre os números {}, {} e {}".format(maior, n1, n2, n3))
