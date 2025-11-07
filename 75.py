'''
    75: Desenvolva um gerador de senhas que crie senhas seguras baseadas em critérios
    específicos, com validação de força e opções de personalização avançadas.
Requisitos técnicos:
    - Use range para controlar comprimento e iterações
    - Implemente try-except para validação de entrada
    - Use if-elif-else para diferentes níveis de segurança
    - Crie função para validação de força da senha
    - Use while para regeneração até atingir critérios
'''
import random

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# print(len(letras))
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# print(len(numeros))
caracteres_especiais = ["@", "$", "#", "&", "/", "!", "?"]

def senha(numero_de_digitos): 
    verificado = False
    while (verificado == False):
        estilo_da_senha = (int(input(
            "\nVOCÊ DESEJA UMA SENHA:"\
            "\nDIGITE:\n"\
            "1- FORTE\n"\
            "2- INTERMEDIÁRIA\n"\
            "3- FRACA\n"\
            "-> "
        )))
        if (1 <= estilo_da_senha <= 3):
            verificado = True
        else:
            print("-> OPÇÃO INVÁLIDA!!! <-")
    
    senha = ""
    if (estilo_da_senha == 1):
        for i in range(numero_de_digitos):
            opcao = random.randint(1, 3)
            if (opcao == 1):
                indexLetra = random.randint(0, 25)
                letra = letras[indexLetra]
                # Determinar se a letra vai ser maiúscula ou minúscula. Caso estilo for igual a 1, troca o estilo para maiúsculo:
                estilo = random.randint(0, 1)
                if (estilo == 1):
                    letra = letra.upper()
                senha += letra
            elif (opcao == 2):
                indexNumero = random.randint(0, 9)
                senha += numeros[indexNumero]
            elif (opcao == 3):
                indexCaractereEspecial = random.randint(0, 6)
                senha += caracteres_especiais[indexCaractereEspecial]
    elif (estilo_da_senha == 2):
        for i in range(numero_de_digitos):
            opcao = random.randint(1, 2)
            if (opcao == 1):
                indexLetra = random.randint(0, 25)
                letra = letras[indexLetra]
                # Determinar se a letra vai ser maiúscula ou minúscula. Caso estilo for igual a 1, troca o estilo para maiúsculo:
                estilo = random.randint(0, 1)
                if (estilo == 1):
                    letra = letra.upper()
                senha += letra
            elif (opcao == 2):
                indexNumero = random.randint(0, 9)
                senha += numeros[indexNumero]
    elif (estilo_da_senha == 3):
        for i in range(numero_de_digitos):
            indexLetra = random.randint(0, 25)
            letra = letras[indexLetra]
            # Determinar se a letra vai ser maiúscula ou minúscula. Caso estilo for igual a 1, troca o estilo para maiúsculo:
            estilo = random.randint(0, 1)
            if (estilo == 1):
                letra = letra.upper()
            senha += letra
            
    senha = senha.strip()
    senha = ("\nSENHA: " + senha)
    return senha

continuar = True
while (continuar == True):
    try:
        verificado = False
        while (verificado == False):
            qtdeDigitos = (int(input("QUANTOS DÍGITOS VOCÊ DESEJA QUE A SENHA CONTENHA?\n-> ")))
            if (qtdeDigitos > 0):
                verificado = True
            else:
                print("-> A SENHA DEVE TER PELO MENOS 1 DÍGITO!!! <-")

        resultado = senha(qtdeDigitos)
        print(resultado)

        valido = False
        while (valido == False):
            desejoContinuar = (int(input(
                "\nDESEJA CONTINUAR:\n"\
                "DIGITE:\n"\
                "1- SIM\n"\
                "2- NÃO\n"\
                "-> "
            )))
            if (1 <= desejoContinuar <= 2):
                valido = True
                if (desejoContinuar == 1):
                    print("VAMOS CONTINUAR ENTÃO...")
                else:
                    print("OK! FOI BOM TER VOCÊ CONOSCO!!!")
                    continuar = False
            else:
                print("-> DIGITE 1 OU 2!!! <-")
        
    except ValueError:
        print("-> DIGITE APENAS NÚMEROS!!! <-")