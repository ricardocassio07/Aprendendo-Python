# 17. Escreva um programa que calcule a potência de um número.
base = (float(input("Digite a base: ")))
expoente = (int(input("Digite o expoente: ")))
resultado = (base ** expoente)
print("{}^{} = {:.2f}".format(base, expoente, resultado))