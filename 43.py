# 43. Crie um programa que verifique se um número é divisível por 3 e por 5
n = (float(input("Digite um número: ")))
if ((n % 3 == 0) and (n % 5 == 0)):
    print("O número {} é divísivel por 3 e 5!".format(n))
else:
    print("O número {} não é divísivel por 3 e 5!".format(n))