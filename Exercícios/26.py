# 26. Escreva um programa que verifique se um número é positivo ou negativo.
n = (float(input("Digite um número: ")))
if (n > 0):
    resultado = "é positivo"
elif (n < 0):
    resultado = "é negativo"
else:
    resultado = "é neutro"
print("O número {} {}".format(n, resultado))