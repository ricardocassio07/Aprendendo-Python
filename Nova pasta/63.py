# 1. Crie uma função que gere uma sequência personalizada usando range com diferentes parâmetros.

p = (int(input("Digite um número inteiro: ")))
p2 = (int(input("Digite outro número inteiro: ")))

def sequencia(n1, n2):
    pares = 0
    impares = 0
    serie = []
    # Caso o primeiro parãmetro for maior que o segundo, devemos trocar os seus valores:
    if (n1 > n2):
        temporario = 0
        temporario = n1
        n1 = n2
        n2 = temporario
    # Calcular se o número é ímpar ou par:
    for i in range(n1, (n2 + 1)):
        serie.append(i)
        if (i % 2 == 0):
            pares += 1
        else:
            impares += 1

    # Mostrar a quantidade de números pares e ímpares no intervalo:
    print("Na série {0} tem {1} pares e {2} ímpares!".format(serie, pares, impares))
    
sequencia(p, p2)