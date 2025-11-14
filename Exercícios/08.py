# 8. Crie um programa que calcule a média de três notas.
n1 = (float(input("Digite a primeira nota: ")))
n2 = (float(input("Digite a segunda nota: ")))
n3 = (float(input("Digite a terceira nota: ")))
media = ((n1 + n2 + n3) / 3)
print("A média entre as notas {}, {} e {} é igual a {}".format(n1, n2, n3, media))