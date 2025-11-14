# 44. Escreva um programa que determine o preço da passagem baseado na idade.
i = (int(input("Digite a sua idade: ")))
preco_passagem = 1000
if (i >= 60 or (0 < i < 10)):
    preco_passagem *= 0.50
elif (i >= 18):
    preco_passagem = preco_passagem
else:
    preco_passagem *= 0.75
print("A pessoa deverá pagar R${:.2f}!".format(preco_passagem))
