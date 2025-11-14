# 21. Escreva um programa que calcule a distância entre dois pontos.
x = (float(input("Digite um número: ")))
y = (float(input("Digite outro número: ")))
if (x > y):
    distancia = (x - y)
else:
    distancia = (y - x)
print("Os pontos {} e {} estão a {} unidades um do outro!".format(x, y, distancia))