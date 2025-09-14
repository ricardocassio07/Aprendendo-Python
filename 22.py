# 22. Crie um programa que calcule o volume de uma esfera.
raio = (float(input("Digite o valor do raio da esfera: ")))
volume = ((4 * 3.14 * (raio ** 3)) / 3)
print("O volume de uma esfera que possui os seu raio medindo {} é igual a {:.2f}".format(raio, volume))