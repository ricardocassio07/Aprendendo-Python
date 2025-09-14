# 28. Escreva um programa que verifique se um número é par ou ímpar.
n = (float(input("Digite um número: ")))
if (n % 2 == 0):
    resultado = "é par"
else:
    resultado = "é ímpar"
print("O número {} {}!".format(n, resultado))