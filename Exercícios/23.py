# 23. Escreva um programa que converta uma quantia em reais para dólares.
reais = (float(input("Digite o valor em Reais: R$")))
dolares = (reais * 5.39)
print("Hoje, dia 11/09/2025, R${:.2f} é igual a US${:.2f}".format(reais, dolares))