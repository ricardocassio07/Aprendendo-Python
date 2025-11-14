# 56. Implemente um gerador de senhas seguras com diferentes critérios e validação.
import random
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "J", "K", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
caracteresEspeciais = ["@", "!", "$", "#"]
senha = []
desejoValido = False
while (desejoValido == False):
    try:
        desejoDoUsuario = (int(input("Você deseja que a senha contenha:\nDigite:\n1- Apenas números;\n2- Apenas letras;\n3- Números e letras;\n4- Números, letras e carateres especiais(! @ # $ % )\n-> ")))
        if (desejoDoUsuario == 1):
            i = 0
            while (i < 8):
                s = random.randint(0, 9)
                numero = numeros[s]
                numero = str(numero)
                senha.append(numero)
                i+=1
            print("{}{}{}{}{}{}{}{}".format(senha[0], senha[1], senha[2], senha[3], senha[4], senha[5], senha[6], senha[7]))
            desejoValido = True
        elif (desejoDoUsuario == 2):
            i = 0
            while (i < 8):
                s = random.randint(0, 25)
                letra = letras[s]
                maisculo = random.randint(0, 1)
                if  (maisculo == 1):
                    letra = letra.upper()
                senha.append(letra)
                i+=1
            print("{}{}{}{}{}{}{}{}".format(senha[0], senha[1], senha[2], senha[3], senha[4], senha[5], senha[6], senha[7]))
            desejoValido = True
            desejoValido = True
        elif (desejoDoUsuario == 3):
            i = 0
            while (i < 8):
                letraOuNumero = random.randint(0, 1)
                if (letraOuNumero == 0):
                    s = random.randint(0, 25)
                    letra = letras[s]
                    maisculo = random.randint(0, 1)
                    if  (maisculo == 1):
                        letra = letra.upper()
                    senha.append(letra)
                    i+=1
                else:
                    s = random.randint(0, 9)
                    numero = numeros[s]
                    numero = str(numero)
                    senha.append(numero)
                    i+=1
            print("{}{}{}{}{}{}{}{}".format(senha[0], senha[1], senha[2], senha[3], senha[4], senha[5], senha[6], senha[7]))
            desejoValido = True
        elif (desejoDoUsuario == 4):
            i = 0
            while (i < 8):
                letraOuNumero = random.randint(0, 2)
                if (letraOuNumero == 0):
                    s = random.randint(0, 25)
                    letra = letras[s]
                    maisculo = random.randint(0, 1)
                    if  (maisculo == 1):
                        letra = letra.upper()
                    senha.append(letra)
                    i+=1
                elif (letraOuNumero == 1):
                    s = random.randint(0, 9)
                    numero = numeros[s]
                    numero = str(numero)
                    senha.append(numero)
                    i+=1
                else:
                    s = random.randint(0, 3)
                    caractere = caracteresEspeciais[s]
                    senha.append(caractere)
                    i+=1
            print("{}{}{}{}{}{}{}{}".format(senha[0], senha[1], senha[2], senha[3], senha[4], senha[5], senha[6], senha[7]))
            desejoValido = True
        else:
            print("Digite apenas 1, 2, 3 ou 4!!!")
    except ValueError:
        print("Digite apenas números!!!")