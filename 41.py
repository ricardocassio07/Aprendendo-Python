# 41. Crie um programa que verifique se um número é múltiplo de outro.
n1 = (float(input("Digite um número: ")))
n2 = (float(input("Digite mais um número: ")))
if (n1 % n2 == 0):
    print("O número {} é múltiplo de {}!".format(n1, n2))
else:
    print("O número {} não é múltiplo de {}!".format(n1, n2))