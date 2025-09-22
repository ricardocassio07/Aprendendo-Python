# 58. Desenvolva um sistema de cadastro de pessoas com validação de dados e busca.
pessoas = {
    "123.456.789-09": {"nome": "Ana", "idade": 25, "cidade": "São Paulo"},
    "987.654.321-00": {"nome": "Carlos", "idade": 30, "cidade": "Rio de Janeiro"},
    "456.789.123-32": {"nome": "Mariana", "idade": 22, "cidade": "Belo Horizonte"},
    "321.654.987-76": {"nome": "João", "idade": 28, "cidade": "Curitiba"}
}
try:
    encerrarSessao = False
    while encerrarSessao == False:
        opcao = int(input("O que deseja fazer?\nDigite:\n1- Cadastrar pessoas;\n2- Listar pessoas;\n3-Buscar pessoas;\n4- Atualizar dados;\n 5- Encerrar sessão.\n-> "))
        if (1 <= opcao <= 5):
            print("OPÇÃO VÁLIDA!!!")
            if (opcao == 1):
                nome = input("Digite o nome da pessoa que deseja cadastrar:\n-> ")
                while (nome == " "):
                    print("NOME INVÁLIDO!!!")
                    nome = input("Digite o nome da pessoa que deseja cadastrar:\n-> ")

                try:
                    CPF = (int(input("Digite o CPF (SEM TRAÇOS OU PONTOS): ")))
                    CPF = str(CPF)
                    if (len(CPF) == 11):
                        n1 = CPF[0]
                        n1 = int(n1)
                        n2 = CPF[1]
                        n2 = int(n2)
                        n3 = CPF[2]
                        n3 = int(n3)
                        n4 = CPF[3]
                        n4 = int(n4)
                        n5 = CPF[4]
                        n5 = int(n5)
                        n6 = CPF[5]
                        n6 = int(n6)
                        n7 = CPF[6]
                        n7 = int(n7)
                        n8 = CPF[7]
                        n8 = int(n8)
                        n9 = CPF[8]
                        n9 = int(n9)
                        n10 = CPF[9]
                        n10 = int(n10)
                        n11 = CPF[10]
                        n11 = int(n11)
                        if (n1 == n2 == n3 == n4 == n5 == n6 == n7 == n8 == n9 == n10 == n11):
                            print("CPF INVÁLIDO!!! ELE NÃO PODE SER UMA SEQUÊNCIA JÁ CONHECIDA!!!")
                        else:
                            digito10 = ((n1 * 10) + (n2 * 9) + (n3 * 8) + (n4 * 7) + (n5 * 6) + (n6 * 5) + (n7 * 4) + (n8 * 3) + (n9 * 2))
                            r = (digito10 % 11)
                            if (r < 2):
                                digito10 = 0
                            else:
                                digito10 = (11 - r)
                            digito11 = ((n1 * 11) + (n2 * 10) + (n3 * 9) + (n4 * 8) + (n5 * 7) + (n6 * 6) + (n7 * 5) + (n8 * 4) + (n9 * 3) + (n10 * 2))
                            r = (digito11 % 11)
                            if (r < 2):
                                digito11 = 0
                            else:
                                digito11 = (11 - r)

                            if ((n10 != digito10) or (n11 != digito11)):
                                print("CPF INVÁLIDO!!!")
                            else:
                                print("O CPF {}{}{}.{}{}{}.{}{}{}-{}{} É VÁLIDO!!!".format(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11))
                    else:
                        print("O CPF É INVÁLIDO, POIS ELE DEVE CONTER EXATAMENTE 11 DIGITOS!!!")
                except ValueError:
                    print("DIGITE APENAS NÚMEROS!!!")

                try:
                    idade = (int(input("Digite a idade dessa pessoa:\n-> ")))
                    while (idade <= 0):
                        print("IDADE INVÁLIDA!!!")
                        idade = (int(input("Digite a idade dessa pessoa:\n-> ")))
                except ValueError:
                    print("DIGITE APENAS NÚMEROS!!!")

                cidade = input("Em qual cidade essa pessoa mora:\n-> ")
                while (cidade == " "):
                    cidade = input("Em qual cidade essa pessoa mora:\n-> ")

                pessoas[CPF] = [f"nome:{nome}", f"idade: {idade}", f"cidade: {cidade}"]
                
            elif (opcao == 2):

            elif (opcao == 3): 

            elif (opcao == 4):

            elif (opcao == 5):
                print("OK!!!\nFOI ÓTIMO TER VOCÊ CONOSCO!!!")
                encerrarSessao = True
        else:
            print("DIGITE 1, 2, 3, 4 OU 5!!!")

except ValueError:
    print("DIGITE APENAS NÚMEROS!!!")
