# 32. Escreva um programa que calcule o IMC e classifique o resultado.
peso = (float(input("Digite o peso da pessoa em kilogramas (Kg): ")))
altura = (float(input("Digite a altura da pessoa em metros (m): ")))
IMC = (peso / (altura ** 2))
if (IMC >= 40):
    resultado = "POSSUI OBESIDADE GRAU III"
elif (IMC >= 35):
    resultado = "POSSUI OBESIDADE GRAU II"
elif (IMC >= 30):
    resultado = "POSSUI OBESIDADE GRAU I"
elif (IMC >= 25):
    resultado = "POSSUI SOBREPESO"
elif (IMC >= 18.5):
    resultado = "POSSUI PESO NORMAL"
else:
    resultado = "ESTÁ ABAIXO DO PESO"
print("O IMC dessa pessoa cujo seu peso é igual {} Kg e a sua altura é igual {} m é {:.2f} Kg/m², portanto, ela {}!".format(peso, altura, IMC, resultado))