# 5. Implemente um gerador de coordenadas para grade 2D usando range aninhado.

def gerador():
    coordenadas = []

    while True:
        try:    
            x_inicio = (int(input("Digite o número inicial da coordenada X: ")))
            x_fim = (int(input("Digite o número final da coordenada X: ")))
            y_inicio = (int(input("Digite o número inicial da coordenada Y: ")))
            y_fim = (int(input("Digite o número final da coordenada Y: ")))
            x_intervalo = (int(input("Digite o valor que deve ser incrementado a coordenada X: ")))
            y_intervalo = (int(input("Digite o valor que deve ser incrementado a coordenada Y: ")))
            break
        except:
            print("Digite apenas números inteiros!!!")

    for x in range(x_inicio, x_fim, x_intervalo):
        for y in range(y_inicio, y_fim, y_intervalo):
            coordenadas.append((x, y))

    cont = 1
    print("\nCOORDENADAS:")
    for coordenada in coordenadas:
        print("{0}º COORDENADA: {1}".format(cont, coordenada))
        cont += 1

gerador()