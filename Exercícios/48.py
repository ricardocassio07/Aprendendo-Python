# 48. Escreva um programa que determine o maior e menor entre três números
n1 = (float(input("Digite um número: ")))
menor = n1
maior = n1
n2 = (float(input("Digite outro número: ")))
n3 = (float(input("Digite mais um número: ")))
if (maior < n2):
    maior = n2
if (n2 < menor):
    menor = n2
if (maior < n3):
    maior = n3
if (n3 < menor):
    menor = n3
print("O número {} é o menor e o número {} é o maior entre os números {}, {} e {}".format(menor, maior, n1, n2, n3))
