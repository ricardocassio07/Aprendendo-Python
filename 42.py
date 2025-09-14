# 42. Escreva um programa que determine o quadrante de um ponto no plano cartesiano.
x = (float(input("Digite a coordenada X do ponto: ")))
y = (float(input("Digite a coordenada y do ponto: ")))
if ((x != 0) and (y != 0)):
    if ((x > 0) and (y > 0)):
        resultado = ("PRIMEIRO QUADRANTE")
    elif ((x < 0) and (y > 0)):
        resultado = ("SEGUNDO QUADRANTE")
    elif ((x < 0) and (y < 0)):
        resultado = ("TERCEIRO QUADRANTE")
    elif ((x > 0) and (y < 0)):
        resultado = ("QUARTO QUADRANTE")
    print("O ponto ({},{}) está no {}!".format(x, y, resultado))
else:
    print("O ponto ({},{}) não pertence a nenhum quadrante eles são formados apenas pelos pontos em que as duas coordenadas são diferentes de zero!".format(x, y))