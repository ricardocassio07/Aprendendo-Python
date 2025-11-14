# 25. Escreva um programa que calcule a hipotenusa de um triângulo retângulo.
c1 = (float(input("Digite o valor de um dos catetos do triângulo: ")))
c2 = (float(input("Digite o valor do outro cateto do triângulo: ")))
hip = (((c1 ** 2) + (c2 ** 2)) ** 0.5)
print("O valor da hipotenusa de um triângulo cujo seus catetos medem {} e {} é igual a {}".format(c1, c2, hip))