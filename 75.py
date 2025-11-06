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
print(len(letras))
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
print(len(numeros))
caracteres_especiais = ["@", "$", "#", "&", "/", "!", "?"]

continuar = True
while (continuar == True):
    try:
        qtdeDigitos = (int(input("QUANTOS DÍGITOS VOCÊ DESEJA QUE A SENHA CONTENHA?\n-> ")))
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
        
        senha: str 
        for i in range(qtdeDigitos):
            opcao = random.radiant(1, 3)
            if (opcao == 1)
            elif (opcao == )


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