# 9. Implemente um calculador de expressões matemáticas que avalie strings com operações básicas.
expressao = input("Digite a expressão matemática que deseja resolver: ")
expressao = expressao.lower()
elementos = expressao.split()
if (len(elementos) > 1):
    i = 0
    while (i < len(elementos)):
        if (elementos[i] == "x" or elementos[i] == "*"):
            n1 = float(elementos[i-1])
            n2 = float(elementos[i+1])
            resultado = n1 * n2
            del elementos[i-1:i+2]
            elementos.insert(i-1, resultado)
            i = 0
        elif (elementos[i] == "/"):
            n1 = float(elementos[i-1])
            n2 = float(elementos[i+1])
            resultado = n1 / n2
            del elementos[i-1:i+2]
            elementos.insert(i-1, resultado)
            i = 0
        else:
            i += 1
    i = 0
    while (i < len(elementos)):
        if (elementos[i] == "+"):
            n1 = float(elementos[i-1])
            n2 = float(elementos[i+1])
            resultado = n1 + n2
            del elementos[i-1:i+2]
            elementos.insert(i-1, resultado)
            i = 0
        elif (elementos[i] == "-"):
            n1 = float(elementos[i-1])
            n2 = float(elementos[i+1])
            resultado = n1 - n2
            del elementos[i-1:i+2]
            elementos.insert(i-1, resultado)
            i = 0
        else:
            i += 1
    print("Resultado: {}".format(elementos[0]))
else:
    print("LEMBRE-SE DE SEPARAR OS TERMOS COM ESPAÇOS!!!")