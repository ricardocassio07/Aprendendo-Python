# 35. Crie um programa que determine o tipo de triângulo.
l1 = (float(input("Digite o valor da medida de um dos lados do triângulo: ")))
l2 = (float(input("Digite o valor da medida do outro lado do triângulo: ")))
l3 = (float(input("Digite o valor da medida do último lado do triângulo: ")))
if (l1 == l2 == l3):
    resultado = ("A medida dos três lados do triângulo são iguais, portanto, ele é EQUILÁTERO!")
elif (l1 != l2 != l3):
    resultado = ("A medida dos três lados do triângulo são diferentes, portanto, ele é ESCALENO!")
else:
    resultado = "O triãngulo possui dois lados com medidas iguais e um terceiro com medidada diferente, portanto, ele é ISÓSCELES!"
print(resultado)